# Easy VPN

Easy VPN

2011年8月2日

22:09

Easy VPN

1. 简化client端的配置

2. 对client端进行集中化管理,向client端推送一些策略.

3. client端有一些预配置(IKE Policy & IPSEC transform sets)

4. 由client端发起连接(IKE Phase 1 process).

5. 不支持group 1,支持group 2；不支持AH,支持ESP；支持Tunnel mode ,不支持Transport mode

6. 使用Group Policy只能使用RADIUS服务器

Easy VPN server:Router/PIX/VPN

Easy VPN remote:Router/PIX/VPN(3002)/Software client

实验 1 :

![Easy%20VPN%2061dae62c24b147a298e261e6ee259b5c/image1.png](Easy%20VPN/image1.png)

环境:

Internet(config)#line vty 0 4

Internet(config-line)#no login <===不使用登录密码

Internet(config-line)#privilege level 15 <====将权限提到第15级(telnet进去时,直接进入特权模式)

PAT(config)#ip access-list extended P

PAT(config-ext-nacl)#permit ip 218.18.100.0 0.0.0.255 any

PAT(config)#int e0/0.218

PAT(config-subif)#ip nat inside

PAT(config)#int e0/0.100

PAT(config-subif)#ip nat outside

PAT(config)#ip nat inside source list P interface ethernet 0/0.100 overload

PC机:

Internet#show user

Line User Host(s) Idle Location

0 con 0 idle 01:01:44

- 66 vty 0 idle 00:00:00 100.1.1.1
- ---------------------------------------------------------------------

PAT#show ip nat translations

Pro Inside global Inside local Outside local Outside global

icmp 100.1.1.1:1024 218.18.100.241:1024 100.1.1.3:1024 100.1.1.3:1024

tcp 100.1.1.1:2501 218.18.100.241:2501 100.1.1.3:23 100.1.1.3:23

VpnServer(config)#username ciscovpn password ciscovpn

以上的用户名和密码应用于以下图中:

![Easy%20VPN%2061dae62c24b147a298e261e6ee259b5c/image2.png](Easy%20VPN/image2.png)

VpnServer(config)#aaa new-model <====起用AAA

VpnServer(config)#aaa authentication login NOAU none <===定义"NOAU"

VpnServer(config)#line con 0

VpnServer(config-line)#login authentication NOAU <===调用"NOAU"

VpnServer(config)#line vty 0 4

VpnServer(config-line)#login authentication NOAU

VpnServer(config)#aaa authentication login xauth local <===login的名字"xauth",本地

VpnServer(config)#aaa authorization network modeconf local <===网络的授权名字:"modeconf",本地

IKE Phase I Policy:

VpnServer(config)#crypto isakmp policy 10

VpnServer(config-isakmp)#authentication pre-share

VpnServer(config-isakmp)#group 2 <==="group"必须为"2"(在EasyVPN中)

VpnServer(config-isakmp)#hash md5 <===软件作为client,必须为"MD5"；硬件作为client,则没规定

VpnServer(config)#crypto isakmp client configuration group EZVPN <===相当于"pre-share"KEY的名字

VpnServe(config-isakmp-group)#key cisco123 <===基于证书时不需要KEY <==相当于"pre-share"KEY的密码

以上两条命令的"group"和"key"用于以下图中:

![Easy%20VPN%2061dae62c24b147a298e261e6ee259b5c/image3.png](Easy%20VPN/image3.png)

VpnServe(config-isakmp-group)#pool ezvpnpool <===地址池的名字

VpnServe(config-isakmp-group)#acl 101 <===如不调用此列表,将是Tunnel everything；如调用此列表,将是split Tunnel(即：定义了哪种流量，哪种流量才加密)

VpnServe(config-isakmp-group)#?

ISAKMP group policy config commands:

access-restrict Restrict clients in this group to an interface <==限制client从哪一个接口拨入VPN服务器

acl Specify split tunneling inclusion access-list number

dns Specify DNS Addresses <===给client端推送一个DNS的地址

domain Set default domain name to send to client

exit Exit from ISAKMP client group policy configuration mode

group-lock Enforce group lock feature <===用户和组的绑定(即:这个用户必须属于这个组才能用)

key pre-shared key/IKE password

no Negate a command or set its defaults

pool Set name of address pool

wins Specify WINS Addresses

VpnServer(config)#ip local pool ezvpnpool 192.168.168.100 192.168.168.200 <===定义地址池(分配地址给client端)

VpnServer(config)#access-list 101 permit ip 192.168.4.0 0.0.0.255 any

VpnServer(config)#crypto isakmp profile ISA

VpnServer(conf-isa-prof)#match identity group EZVPN

VpnServer(conf-isa-prof)#client authentication list xauth

VpnServer(conf-isa-prof)#isakmp authorization list modeconf

地址的推送方式:

VpnServer(conf-isa-prof)#client configuration address respond <===cisco的client软件版本为3.0以上使用(respond/pull),客户端去询问服务器端要地址.

或者: VpnServer(conf-isa-prof)#client configuration address initiate <===cisco的client软件版本为3.0以下使用(push),服务器端向客户端推送地址.

IPSec Phase II Policy:

VpnServer(config)#crypto ipsec transform-set MYSET esp-des esp-md5-hmac

VpnServer(config)#crypto dynamic-map DMAP 10

VpnServer(config-crypto-map)#set transform-set MYSET

VpnServer(config-crypto-map)#set isakmp-profile ISA

VpnServer(config-crypto-map)#reverse-route

VpnServer(config)#crypto map SMAP 10 ipsec-isakmp dynamic DMAP

Apply VPN Configuration:

VpnServer(config)#interface e0/0

VpnServer(config-if)#crypto map SMAP

- -------------------------------------------------

VpnServer#show ip local pool

Pool Begin End Free In use

ezvpnpool 192.168.168.100 192.168.168.200 100 1

- ---------------------------------------------------

VpnServer#show ip local pool ezvpnpool

Pool Begin End Free In use

ezvpnpool 192.168.168.100 192.168.168.200 100 1

Available addresses:

192.168.168.105

192.168.168.106

......

192.168.168.100 IKE Addr IDB

192.168.168.101 IKE Addr IDB

192.168.168.102 IKE Addr IDB

192.168.168.103 IKE Addr IDB

Inuse addresses:

192.168.168.104 IKE Addr IDB

- ------------------------------------------------------

VpnServer#show ip route

100.0.0.0/24 is subnetted, 1 subnets

C 100.1.1.0 is directly connected, Ethernet0/0

C 192.168.4.0/24 is directly connected, Loopback0

192.168.168.0/32 is subnetted, 1 subnets

S 192.168.168.104 [1/0] via 100.1.1.1 <===反向路由注入第二条规则

硬件CLIENT端：

BranchCompany(config)#crypto ipsec client ezvpn cisco <===名字

BranchCompany(config-crypto-ezvpn)#peer 100.1.1.4

BranchCompany(config-crypto-ezvpn)#group EZVPN key cisco123 <===group名字和密码

BranchCompany(config-crypto-ezvpn)#mode client

BranchCompany(config-crypto-ezvpn)#connect manual <===可选自动/手动

Apply VPN Configuration:

BranchCompany(config)#int e0/0

BranchCompany(config-if)#crypto ipsec client ezvpn cisco outside <===调用

BranchCompany(config)#int loopback 0

BranchCompany(config-if)#crypto ipsec client ezvpn cisco inside

拨号:

BranchCompany#crypto ipsec client ezvpn connect

出现提示:

BranchCompany#

- Mar 1 13:00:06.827: EZVPN(cisco): Pending XAuth Request, Please enter the following command:
- Mar 1 13:00:06.827: EZVPN: crypto ipsec client ezvpn xauth

BranchCompany#crypto ipsec client ezvpn xauth

Username: ciscovpn

Password: ciscovpn

- --------------------------------------------------

BranchCompany#show crypto ip client ezvpn <===以下是拨不成功的(Password: Disallowed)

Easy VPN Remote Phase: 4

Tunnel name : cisco

Inside interface list: Loopback0

Outside interface: Ethernet0/0

Current State: CONNECT_REQUIRED

Last Event: RESET

Save Password: Disallowed

Current EzVPN Peer: 100.1.1.4

- --------------------------------------------------

BranchCompany#show crypto ipsec client ezvpn <===以下是拨成功的

Easy VPN Remote Phase: 4

Tunnel name : cisco

Inside interface list: Loopback0

Outside interface: Ethernet0/0

Current State: IPSEC_ACTIVE

Last Event: SOCKET_UP

Address: 192.168.168.105 <===这是分配的IP地址

Mask: 255.255.255.255

Save Password: Disallowed

Split Tunnel List: 1 <===访问以下网络要加密

Address : 192.168.4.0

Mask : 255.255.255.0

Protocol : 0x0

Source Port: 0

Dest Port : 0

Current EzVPN Peer: 100.1.1.4

- ----------------------------------------------

BranchCompany#telnet 192.168.4.1 /source-interface loopback 0 <===以client端的内部网络去上网(client的内部网络必须要有去server端的内部网络的路由)

BranchCompany#show ip nat translations

Pro Inside global Inside local Outside local Outside global

tcp 100.1.1.2:43004 192.168.2.1:43004 100.1.1.3:23 100.1.1.3:23

tcp 192.168.168.108:55185 192.168.2.1:55185 192.168.4.1:23 192.168.4.1:23

- ---------------------------------------------------------------------

BranchCompany#telnet 192.168.4.1 /source-interface loopback 0

Trying 192.168.4.1 ... Open

VpnServer>show users

Line User Host(s) Idle Location

0 con 0 idle 00:01:45

- 66 vty 0 idle 00:00:00 192.168.168.108
- --------------------------------------------------------------------------

BranchCompany#show ip nat statistics

Total active translations: 1 (0 static, 1 dynamic; 1 extended)

Outside interfaces:

Ethernet0/0

Inside interfaces:

Loopback0

Hits: 533 Misses: 0

CEF Translated packets: 254, CEF Punted packets: 0

Expired translations: 7

Dynamic mappings:

- - Inside Source

[Id: 4] access-list internet-list interface Ethernet0/0 refcount 0

[Id: 3] access-list enterprise-list pool cisco refcount 1

pool cisco: netmask 255.255.255.0

start 192.168.168.108 end 192.168.168.108

type generic, total addresses 1, allocated 1 (100%), misses 0

Queued Packets: 0

- ---------------------------------------------------------------------

清除连接:

BranchCompany#clear crypto ipsec client ezvpn <===清除EZVPN的连接(好像只能在CLIENT端做)

或者: BranchCompany#clear crypto sa

BranchCompany#clear crypto isakmp

- -----------------------------------------------------------------------

网络扩展模式: <====server端不会再下发IP地址,更像一个LAN-TO-LAN

BranchCompany(config)#crypto ipsec client ezvpn cisco

BranchCompany(config-crypto-ezvpn)#mode network-extension <===网络扩展模式

BranchCompany#show ip nat statistics

Total active translations: 0 (0 static, 0 dynamic; 0 extended)

Outside interfaces:

Ethernet0/0

Inside interfaces:

Loopback0

Hits: 699 Misses: 0

CEF Translated packets: 335, CEF Punted packets: 0

Expired translations: 8

Dynamic mappings:

- - Inside Source

[Id: 9] access-list internet-list interface Ethernet0/0 refcount 0 <===上面是PAT成两个,现在是PAT一个

Queued Packets: 0

BranchCompany#show ip nat translations <===没有将"192.168.2.1"PAT成别的

Pro Inside global Inside local Outside local Outside global

tcp 100.1.1.2:13702 192.168.2.1:13702 100.1.1.3:23 100.1.1.3:23

BranchCompany#telnet 192.168.4.1 /source-interface loopback 0

Trying 192.168.4.1 ... Open <=====原地址(192.168.2.1)没更改,直接过去,更像是Lan-to-Lan

VpnServer>show user

Line User Host(s) Idle Location

0 con 0 idle 00:21:05

- 66 vty 0 idle 00:00:00 192.168.2.1 <===这个地址没有更改

easy VPN又明ezVPN，是Cisco专用VPN技术。它分为EASY VPN SERVER和EASY VPN REMOTE两种，EASY VPN SERVER 是REMOT--ACCESS VPN专业设备。配置复杂，支持POLICY PUSHING等特性，现在的900、1700、PIX、VPN3002和ASA等很多设备都支持。此种技术应用在中小企业居多。如Cisco金睿系类的路由器都有整合easy VPN。

![Easy%20VPN%2061dae62c24b147a298e261e6ee259b5c/image4.png](Easy%20VPN/image4.png)

环境：路由器（cisco）r1在一个公司的总部为EZVPN的server,远程internet用户要访问总部的内网，远程用户用的是cisco的EZVPN软件。

要求：配置server端，并在client端拨到总部，能够访问内网

步骤一：server端的接口配置

r1(config)#interface e0 //外网接口配置,主机和路由器直连即可

r1(config-if)#ip add 150.100.1.182 255.255.255.0

r1(config-if)#no sh

r1(config)#int loo 0

r1(config-if)#ip add 10.1.1.1 255.255.255.0 //模拟内网地址

r1(config)#int loo 1

r1(config-if)#ip add 10.1.2.1 255.255.255.0

步骤二：配置验证以及EZVPN

r1(config)#username cisco pass cisco //用于验证的用户名和密码

r1(config)#aaa new-model //开启AAA

r1(config)#aaa authorization network **easyvpn** local

//授权访问列表名字为esayvpn，本地数据库

r1(config)#aaa authentication login ccxx local

//登录验证列表名为ccxx,本地数据库

r1(config)#ip local pool ippool 10.1.1.14 10.1.1.30 //推送给拨上来用户的地址池

r1(config)#crypto isakmp policy 10 //定义IKE1阶段策略

r1(config-isakmp)#encryption 3des //客户端只支持3DES

r1(config-isakmp)#authentication pre-share //使用预共享密钥

r1(config-isakmp)#group 2 //客户端只支持group 2

r1(config-isakmp)#hash md5 //哈希用MD5

r1(config)#crypto isakmp client configuration group cisco //客户端组的配置

r1(config-isakmp-group)#key cisco //预共享密钥

r1(config-isakmp-group)#pool ippool //加载地址池

r1(config-isakmp-group)#acl 100 //加载隧传分离列表

r1(config-isakmp-group)#exit

r1(config)#crypto ipsec transform-set myset esp-3des esp-md5-hmac

//定义IKE2阶段的转换集

r1(cfg-crypto-trans)#exit

r1(config)#access-list 100 permit ip 10.1.1.0 0.0.0.255 any //定义列表

r1(config)#access-list 100 permit ip 10.1.2.0 0.0.0.255 any

r1(config)#crypto dynamic-map dyn 1 //定义动态加密映射，客户端不固定

r1(config-crypto-map)#set transform myset //将转换集加载

r1(config-crypto-map)#reverse-route //反向路由注入，客户到server，server会生成一条静态路由列表

r1(config-crypto-map)#exit

r1(config)#crypto map mymap 10 ipsec-isakmp dynamic dyn

//将动态映射到静态映射

r1(config)#crypto map mymap client authentication list ccxx

//扩展验证使用ccxx

r1(config)#crypto map mymap isakmp authorization list easyvpn

//授权使用easyvpnAAA列表

r1(config)#crypto map mymap client configuration address respond

//向客户端推送配置

r1(config)#int e0/0

r1(config-if)#crypto map mymap //将静态映射加载到接口

以上配置server完毕

步骤三：客户端PC的配置（使用cisco vpn client软件）

1、安装好的软件，打开，点击new新建，输入组名和密码及server地址

![Easy%20VPN%2061dae62c24b147a298e261e6ee259b5c/image5.png](Easy%20VPN/image5.png)

2、建好后，点击连接，提示输入用户名和密码，此为扩展认证

![Easy%20VPN%2061dae62c24b147a298e261e6ee259b5c/image6.png](Easy%20VPN/image6.png)

3、点击OK，如果成功，所有的框消失

4、在PC上查看地址，server是否分配过来了地址

SERVER(R1)------------pc（R2）

R1,R2各起一个loop口 IP分别为10.1.1.1 192.168..23.2（模拟内网） 实现拨号连接

Server#sh run

aaa new-model

!

!

aaa authentication login **remote-vpn** local 验证用户组允许接入

aaa authorization network **remote-vpn** local 给用户组授权

!

username cisco privilege 15 password 0 cisco 具体的用户名和密码

!

!

!

crypto isakmp policy 1------------------------- ----创建身份验证策略

encr 3des

hash md5

authentication pre-share

group 2

!

crypto isakmp client configuration group **cisco1**-------------创建isakmp客户端认证组

key cisco

dns 219.150.32.132

pool DHCP

acl 100 判断哪些数据要加密

max-users 10

netmask 255.255.255.0

crypto isakmp profile cisco

match identity group **cisco1**

client authentication list **remote-vpn** 要与前面的用户匹配

isakmp authorization list **remote-vpn**

client configuration address respond 会分配IP给PC

!

!

crypto ipsec transform-set cisco esp-3des esp-md5-hmac

!

crypto dynamic-map zzq 创建一个动态MAP表

set transform-set cisco

set isakmp-profile cisco

reverse-route 反射路由，自动添加一条路由到你拨的地方来

!

!

crypto map cisco 10 ipsec-isakmp dynamic zzq

!

!

!

!

!

interface Ethernet2/0

ip address 192.168.1.111 255.255.255.0

half-duplex

crypto map cisco

!

interface loo 1

ip address 10.1.1.1 255.255.255.0

half-duplex

!

ip local pool chen 10.1.2.1 10.1.2.50

no ip http server

no ip http secure-server

!

!

!

access-list 100 permit ip 10.1.1.0 0.0.0.255 10.0.0.0 0.255.255.255

!

vpn client的配置：

crypto ipsec client ezvpn cisco

connect manual

group cisco1 key cisco ------------和seerver的要一致

mode client

peer 192.168.12.1

exit

int lo 1

crypto ipsec client ezvpn cisco inside

int s1/3

crypto ipsec client ezvpn cisco outside

exit

ip route 0.0.0.0 0.0.0.0 192.168.12.1

连接（特权下）

crypto ipsec client ezvpn connect （会自动弹出叫你输入如下命令）

crypto ipsec client ezvpn xauth

输入用户名\密码

客户端会自动进行NAT转换,会把内网自动进行pat转换成服务端分配给客户端的地址

show ip nat translation（可以看到内网的192.168.23.2自动转换为10..12.1）

在server查看路由，可以发现自动生成一条静态路由

EzVPN client可分为硬件客户端（路由器或VPN 3000作客户端），软件客户端（PC中运行客户端软件），不管是那种情况，在客户端需要的配置非常少，主要配置在服务器端。VPN无法建立起来的原因很多，比如路由，NAT，地址池，验证等等，如果在实验环境中可以通过3个debug命令去发现问题：debug crypto isakmp、debug crypto engine、debug crypto ipsec，而这里以路由器分别作客户端和服务器，完整配置如下：

服务器：

第一步：配置XAUTH

R1(config)#aaa new-model

R1(config)#aaa authentication login ccxx local

R1(config)#username yjj password yjj

R1(config)#enable secret cisco

R1(config)#crypto map test client authentication list ccxx

R1(config)#crypto isakmp xauth timeout 30

第二步：建立IP地址池

R1(config)#ip local pool p1 100.1.1.100 100.1.1.200

第三步：配置组策略查找

R1(config)#crypto isakmp policy 1

R1(config-isakmp)#authentication pre-share

R1(config-isakmp)#encryption 3des

R1(config-isakmp)#group 2

R1(config-isakmp)#exit

第四步：为MC推定义组策略

R1(config)#crypto isakmp client configuration group ccie

R1(config-isakmp-group)#key ccie

R1(config-isakmp-group)#dns 100.1.1.10 100.1.1.11

R1(config-isakmp-group)#wins 100.1.1.12 100.1.1.13

R1(config-isakmp-group)#domain yjj.com

R1(config-isakmp-group)#pool p1

R1(config-isakmp-group)#exit

第五步：建立变换集

R1(config)#crypto ipsec transform-set myset esp-3des esp-sha-hmac

R1(cfg-crypto-trans)#exit

第六步：用RRI建立动态加密映射

R1(config)#crypto dynamic-map dy 1

R1(config-crypto-map)#set transform-set myset

R1(config-crypto-map)#reverse-route

R1(config-crypto-map)#exit

第七步：将MC应用到动态映射

R1(config)#crypto map test client configuration address respond

R1(config)#crypto map test isakmp authorization list ccie

R1(config)#crypto map test 1 ipsec-isakmp dynamic dy

第八步：将动态加密映射应用到接口

R1(config)#int s0/0

R1(config-if)#crypto map test

R1(config-if)#exit

R1(config)#crypto isakmp keepalive 30 3

如果需要遂传某些网段，把这些网段的访问控制列表写出来，在crypto isakmp client configuration group ccie模式下调用即可，它将自动推送到客户端。

客户端：

R2:

crypto ipsec client ezvpn jj

connect auto

mode client

group ccie

key ccie

peer 10.1.1.1

interfac e0/0

crypto ipsec client ezvpn jj inside

interface s0/0

crypto ipsec client ezvpn jj outside