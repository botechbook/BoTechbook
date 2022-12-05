# Backup peers

Backup peers

2011年8月2日

22:05

Geographic HA using ipsec Backup peers

技术特点:

通过设置多个Peer的方式,Client能够自动切换Server的地址.

Peer是一个一个尝试,从上往下的顺序进行.

实验1:

![Backup%20peers%20f00e6957d29e4cf3a6f138513b3e4283/image1.png](Backup%20peers/image1.png)

IKE Phase I Policy:

R2(config)#crypto isakmp policy 1

R2(config-isakmp)#authentication pre-share

R2(config-isakmp)#hash md5

R2(config-isakmp)#encryption 3des

R2(config-isakmp)#group 2

R2(config)#crypto isakmp keepalive 20 3 <===当第一个PEER断掉后,DPD开始侦测{过了60(20*3)秒后,开始切换}

R2(config)#crypto isakmp key 0 wolf address 123.1.1.1

R2(config)#crypto isakmp key 0 wolf address 123.1.1.3

....

IPSec Phase II Policy:

R2(config)#crypto ipsec transform-set cisco esp-des esp-sha-hmac

R2(cfg-crypto-trans)#mode tunnel

R2(config)#access-list 101 permit ip 3.3.3.0 0.0.0.255 2.2.2.0 0.0.0.255

R2(config)#crypto map huawei 10 ipsec-isakmp

R2(config-crypto-map)#set peer 123.1.1.1 <===先和第一个建立

R2(config-crypto-map)#set peer 123.1.1.3 <====当第一个断掉后,再和第二个建立

R2(config-crypto-map)#set transform-set cisco

R2(config-crypto-map)#set pfs

R2(config-crypto-map)#match address 101

...

Apply VPN Configuration

R2(config)#interface ethernet 0/0

R2(config-if)#crypto map huawei

- -----------------------------------

R3(config)#interface ethernet 0/0

R3(config-if)#crypto map huawei

Redundancy VPN

![Backup%20peers%20f00e6957d29e4cf3a6f138513b3e4283/image2.png](Backup%20peers/image2.png)

HSRP:

R2(config)#int e0/0.123

R2(config-subif)#standby 1 ip 221.1.123.100

组名 virtual IP

R2(config-subif)#standby 1 preempt <====允许抢占

R2(config-subif)#standby 1 priority 105 <====设置优先级(默认为100)

R2(config-subif)#standby 1 name HSRP <====起一个名字(Redundancy VPN需要用到)

R2(config-subif)#standby 1 track e0/0.100 <===当R2的"e0/0.100"接口down掉后,立刻切换到standby路由器

- ----------------------------------------------------------------

R3(config)#int e0/0.123

R3(config-subif)#standby 1 ip 221.1.123.100

R3(config-subif)#standby 1 preempt

R3(config-subif)#standby 1 name HSRP

R3(config-subif)#standby 1 track e0/0.100

- -----------------------------------------------------

R2#show standby

Ethernet0/0.123 - Group 1

State is Active

2 state changes, last state change 00:37:58

Virtual IP address is 221.1.123.100

Active virtual MAC address is 0000.0c07.ac01

Local virtual MAC address is 0000.0c07.ac01 (default)

Hello time 3 sec, hold time 10 sec

Next hello sent in 1.276 secs

Preemption enabled

Active router is local

Standby router is 221.1.123.3, priority 100 (expires in 9.360 sec)

Priority 105 (configured 105)

Track interface Ethernet0/0.100 state Up decrement 10

IP redundancy name is "HSRP" (cfgd)

R1#ping 221.1.123.100

Type escape sequence to abort.

Sending 5, 100-byte ICMP Echos to 221.1.123.100, timeout is 2 seconds:

.!!!!

Success rate is 80 percent (4/5), round-trip min/avg/max = 4/4/4 ms

- -----------------------------------------------------------------------------

配置路由:

R1(config)#ip route 192.168.4.0 255.255.255.0 221.1.123.100 <====也可用反向路由注入

- ---------------------------

R2(config)#router ospf 110

R2(config-router)#net 1.1.234.0 0.0.0.255 area 0

- -------------------------------------------------

R3(config)#router ospf 110

R3(config-router)#net 1.1.234.0 0.0.0.255 area 0

- -------------------------------------------------

R4(config)#router ospf 110

R4(config-router)#net 1.1.234.0 0.0.0.255 area 0

R4(config-router)#net 192.168.4.0 0.0.0.255 area 0

IKE Phase I Policy:

R2(config)#crypto isakmp policy 1

R2(config-isakmp)#authentication pre-share

R2(config)#crypto isakmp key wolf address 221.1.123.1

IPSec Phase II Policy:

R2(config)#crypto ipsec transform-set cisco esp-des esp-sha-hmac

R2(config)#crypto map huawei 10 ipsec-isakmp <===在"show run"时出现"! Incomplete",就是没有配置完

R2(config-crypto-map)#set peer 221.1.123.1

R2(config-crypto-map)#set transform-set cisco

R2(config-crypto-map)#match address VPN

R2(config-crypto-map)#reverse-route <====反向路由注入

R2(config)#ip access-list extended VPN

R2(config-ext-nacl)#permit ip 192.168.4.0 0.0.0.255 192.168.1.0 0.0.0.255

接口调用:

R2(config)#int e0/0.123

R2(config-subif)#crypto map huawei redundancy HSRP <===在此命令应用到接口后,查路由时:会出现一条静态路由("S 192.168.1.0/24 [1/0] via 221.1.123.1")

以上R3的配置和R2类同 <===但R3没有一条静态路由,因为R3为"standby"

重分布:

R2(config)#router ospf 110

R2(config-router)#redistribute static subnets route-map s2o

R2(config)#route-map s2o

R2(config-route-map)#match ip address s2o

R2(config)#ip access-list standard s2o

R2(config-std-nacl)#permit 192.168.1.0

- ------------------------------------------

R3(config)#router ospf 110

R3(config-router)#redistribute static subnets route-map s2o

R3(config)#route-map s2o

R3(config-route-map)#match ip address s2o

R3(config)#ip access-list standard s2o

R3(config-std-nacl)#permit 192.168.1.0

R2(config)#crypto isakmp keepalive 20 <===发送DPD帧,检测

- -------------------------------------

R3(config)#crypto isakmp keepalive 20

- -------------------------------------

R1(config)#crypto isakmp keepalive 20

R1(config)#crypto isakmp policy 10

R1(config-isakmp)#authentication pre-share

R1(config)#crypto isakmp key wolf address 221.1.123.100

R1(config)#crypto ipsec transform-set cisco esp-des esp-sha-hmac

R1(config)#crypto map huawei 10 ipsec-isakmp

R1(config-crypto-map)#set peer 221.1.123.100

R1(config-crypto-map)#set transform-set cisco

R1(config-crypto-map)#match address VPN

R1(config)#ip access-list extended VPN

R1(config-ext-nacl)#permit ip 192.168.1.0 0.0.0.255 192.168.4.0 0.0.0.255

R1(config)#int e0/0

R1(config-if)#crypto map huawei

反向路由注入:

1. Lan to Lan RRI 规则:

以感兴趣流的目的为网络,以 PEER 地址为下一跳,注入这么一条静态路由

2. Soft Client / EZVPN client mode

Server端的RRI规则:

以分配给Client 的地址为网络(32位),以这个client的公网IP为下一跳,注入一条32位主机路由

3. EZVPN Hardware network-extension mode

Server 端 RRI 注入规则:

以Client端的内部网络为网络,以这个client的公网IP为下一跳,注入一条静态路由

4. Remote VPN 的 RRI 跟 Lan-to-Lan 不同:

Remote VPN 是当client 拨入VPN 时注入的

Lan-to-Lan 是配置完就马上注入的

问题1: 一个有crypto map 的接口,收到一个明文的数据包?

答: 收到明文 如果满足接口map的 感兴趣流 drop了,不满足 就当没做vpn

问题2: 一个没有crypto map 的接口,收到一个ESP的数据包?

答: 他回去查看他的SA数据库,然后就解密了.