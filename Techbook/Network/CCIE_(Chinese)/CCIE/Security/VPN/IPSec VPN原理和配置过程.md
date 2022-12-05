# IPSec VPN原理和配置过程

IPSec VPN原理和配置过程

2011年8月2日

22:07

IPSec VPN原理和配置过程

IPSec协议

**IKE**

Internet Key Exchage, 用于互联网中密钥的安全交换

又包括下面二个协议

ISAKMP

定义SA生成,建立等参数.

Oakley

利用Diffie-Hellman算法管理密钥交换.

DH协议保证了在不安全的环境中,密钥可以被安全的交换

**ESP**

Encryption Security Payload, 用于加密净荷

又包括以下加密协议

DES: IBM创造, 56位,已不安全.尽量少用

3DES: 对DES进行三次重复操作, 密钥长度变为168位, 安全性高. 但存在固有缺陷

AES: 目前最安全的加密算法, 相应的耗时也久一点.

**AH**

Authertication Header, 用于验证数据完整性.

所使用的Hash算法为

MD5:输入长度可变,生成特征字符串128bit.

SHA-1:输入长度可变, 生成特征字符串160bit,但IPSec只使用前96bit.

虽然SHA-1仅使用了96bit,但是安全性依然比MD5高, 同时计算速度也要慢一些.

ESP既可以加密数据,也可以通过Hash算法计算数据完整性. 而AH仅能验证完整性,不支持加密.

因而目前主要使用ESP.

IPSec模式

传送模式

L2 | L3 | ESP头 |净荷| ESP尾 | ESP认证

在ESP头和ESP尾之间的部分将被加密, 也就是三层协议以上部分.

在ESP头和ESP认证部分的数据将被验证.

隧道模式

L2 | 新L3 | ESP头 |L3 | 净荷| ESP尾 | ESP认证

此时生成一个新的L3头, 原有的L3头也将被加密.

与传送模式相同,

在ESP头和ESP尾之间的部分将被加密, 也就是二层协议以上部分.

在ESP头和ESP认证部分的数据将被验证.

VPN总是优先选择隧道模式.

IPSec过程

IPSec可以分为以下5个阶段

- 指定兴趣流量: 定义需要保护的流量.
- IKE阶段1: 协商ISAKMP参数,生成双向SA, 用于交换密钥
- IKE阶段2: 协商IPSec参数, 生成二个单向SA数据通道.
- 安全数据传送: 数据通过单向SA通道进行安全传送
- IPSec隧道终结:

指定兴趣流量

由ACL完成,定义需要经过IPSec加密的流量.由于这些都是在路由器上完成,对于用户来说是一切透明的.因此不需要VPN客户端或者新建连接.从用户PC发出的所有流量都交给路由器,由路由器来实现普通流量与VPN流量的分离.

IKE阶段1

VPN二端的路由器交换isamp参数, 称为isakmp变换集.包括

IKE加密算法: DES 3DES AES

IKE验证算法: MD5 SHA-1

IKE认证方式: 预共享密钥 RSA签名 临时密码

隧道周期: 时间(s) 流量(bit)

DH群: 2 5 7

只有路由器间有相同的isamp变换集, 才能形成IKE通道. 这个SA是双向的.

IKE阶段2

VPN二端的路由器交换ipsec参数, 称为ipsec变换集.与isakmp变换集非常类似,包括

ipsec协议: ESP AH

ipsec加密算法: DES 3DES AES

ipsec验证算法: MD5 SHA-1

ipsec模式: 隧道 传送

ipsec生命期: 时间(s) 流量(bit)

与IKE阶段1相同, 必须完全相同的ipsec变换集才能形成ipsec通道.此处会生成二个单向SA通道, 分别用于发送和接收.

安全数据传送

当ipsec隧道生成后,兴趣流量就会经由ipsec隧道进行发送.

IPSec隧道终结

分为二种情况:

自动终结: 通常是ipsec生命期过期

手动终结: 由用户手动删除.

IPSec VPN配置

![IPSec%20VPN%E5%8E%9F%E7%90%86%E5%92%8C%E9%85%8D%E7%BD%AE%E8%BF%87%E7%A8%8B%20f2660a32808b488d943009fe597a7a65/image1.png](IPSec%20VPN原理和配置过程/image1.png)

在R1的ethernet0/0和R3的ethernet0/1接口间建立IPSec隧道,加密PC1和PC2间的流量.

首先测试下PC1和PC2的连通性

VPCS 1 >ping 192.168.2.2

192.168.2.2 icmp_seq=1 time=16.126 ms

192.168.2.2 icmp_seq=2 time=49.369 ms

192.168.2.2 icmp_seq=3 time=48.297 ms

192.168.2.2 icmp_seq=4 time=16.966 ms

192.168.2.2 icmp_seq=5 time=50.147 ms

VPCS 2 >ping 10.1.2.2

10.1.2.2 icmp_seq=1 time=50.358 ms

10.1.2.2 icmp_seq=2 time=80.953 ms

10.1.2.2 icmp_seq=3 time=48.220 ms

10.1.2.2 icmp_seq=4 time=53.387 ms

10.1.2.2 icmp_seq=5 time=48.299 ms

与上面的过程相对应,也可将配置分为以下几步

1.定义兴趣流量

2.定义isakmp策略 (IKE阶段1)

3.定义ipsec策略 (IKE阶段2)

4.配置密码映射

5.应用策略到接口

定义兴趣流量

.

可以通过扩展ACL实现.

R1(config)#access-list 101 permit ip 10.1.2.0 0.0.0.255 192.168.2.0 0.0.0.255

R1(config)#access-list 101 permit icmp 10.1.2.0 0.0.0.255 192.168.2.0 0.0.0.255

R3(config)#access-list 101 permit ip 192.168.2.0 0.0.0.255 10.1.2.0 0.0.0.25

R3(config)#access-list 101 permit icmp 192.168.2.0 0.0.0.255 10.1.2.0 0.0.0.25

定义isakmp策略

R1(config)#crypto isakmp policy 55

R1(config-isakmp)#encryption 3des

R1(config-isakmp)#hash md5

R1(config-isakmp)#authentication pre-share

R1(config-isakmp)#lifetime 3600

R1(config-isakmp)#group 2

R1(config-isakmp)#exit

R1(config)#crypto isakmp key ccna address 192.168.1.2

R3(config)#crypto isakmp policy 66

R3(config-isakmp)#encryption 3des

R3(config-isakmp)#hash md5

R3(config-isakmp)#group 2

R3(config-isakmp)#lifetime 3600

R3(config-isakmp)#authentication pre-share

R3(config-isakmp)#exit

R3(config)#crypto isakmp key ccna address 10.1.1.1

定义ipsec策略

R1(config)#crypto ipsec transform-set vpn esp-3des esp-md5-hmac

R1(cfg-crypto-trans)#mode tunnel

R1(cfg-crypto-trans)#exit

R1(config)#crypto ipsec security-association lifetime seconds 6400

R3(config)#crypto ipsec transform-set vpn esp-3des esp-md5-hmac

R3(cfg-crypto-trans)#mode tunnel

R3(cfg-crypto-trans)#exit

R3(config)#crypto ipsec security-association lifetime seconds 6400

配置密码映射

R1(config)#crypto map vpn1 15 ipsec-isakmp

R1(config-crypto-map)#match address 101

R1(config-crypto-map)#set peer 192.168.1.2

R1(config-crypto-map)#set transform-set vpn

R1(config-crypto-map)#exit

R3(config)#crypto map vpn2 44 ipsec-isakmp

R3(config-crypto-map)#match address 101

R3(config-crypto-map)#set peer 10.1.1.1

R3(config-crypto-map)#set transform-set vpn

R3(config-crypto-map)#exit

应用策略到接口

R1(config)#interface ethernet 0/0

R1(config-if)#crypto map vpn1

R1(config-if)#end

R1#

- Mar 1 00:17:23.519: %CRYPTO-6-ISAKMP_ON_OFF: ISAKMP is ON
- Mar 1 00:17:24.115: %SYS-5-CONFIG_I: Configured from console by console

R3(config)#interface ethernet 0/1

R3(config-if)#crypto map vpn2

R3(config-if)#end

R3#

- Mar 1 00:17:28.311: %CRYPTO-6-ISAKMP_ON_OFF: ISAKMP is ON
- Mar 1 00:17:29.467: %SYS-5-CONFIG_I: Configured from console by console

配置完毕,现在开始测试下

首先PC1 ping 下 PC2

VPCS 1 >ping 192.168.2.2

192.168.2.2 icmp_seq=1 timeout

192.168.2.2 icmp_seq=2 timeout

192.168.2.2 icmp_seq=3 time=107.683 ms

192.168.2.2 icmp_seq=4 time=46.449 ms

192.168.2.2 icmp_seq=5 time=16.452 ms

开始二个包丢失, 正是因为隧道还未开启的缘故.

查看下当前的isakmp sa连接状态

R1#sh crypto isakmp sa

dst src state conn-id slot

192.168.1.2 10.1.1.1 QM_IDLE 1 0

可以看到连接已建立,vpn二端分别为10.1.1.1和192.168.1.2

查看下当前的ipsec sa连接状态

R1#sh crypto ipsec sa

interface: Ethernet0/0

Crypto map tag: vpn1, local addr. 10.1.1.1

protected vrf:

local ident (addr/mask/prot/port): (10.1.2.0/255.255.255.0/0/0)

remote ident (addr/mask/prot/port): (192.168.2.0/255.255.255.0/0/0)

current_peer: 192.168.1.2:500

PERMIT, flags={origin_is_acl,ipsec_sa_request_sent}

#pkts encaps: 8, #pkts encrypt: 8, #pkts digest 8

#pkts decaps: 8, #pkts decrypt: 8, #pkts verify 8

#pkts compressed: 0, #pkts decompressed: 0

#pkts not compressed: 0, #pkts compr. failed: 0

#pkts not decompressed: 0, #pkts decompress failed: 0

#send errors 2, #recv errors 0

local crypto endpt.: 10.1.1.1, remote crypto endpt.: 192.168.1.2

path mtu 1500, ip mtu 1500, ip mtu idb Ethernet0/0

current outbound spi: 7D94C0D5

inbound esp sas:

spi: 0xC8FEB295(3372135061)

transform. esp-3des esp-md5-hmac ,

in use settings ={Tunnel, }

slot: 0, conn id: 2000, flow_id: 1, crypto map: vpn1

sa timing: remaining key lifetime (k/sec): (4414350/6389)

IV size: 8 bytes

replay detection support: Y

inbound ah sas:

inbound pcp sas:

outbound esp sas:

spi: 0x7D94C0D5(2106900693)

transform. esp-3des esp-md5-hmac ,

in use settings ={Tunnel, }

slot: 0, conn id: 2001, flow_id: 2, crypto map: vpn1

sa timing: remaining key lifetime (k/sec): (4414350/6387)

IV size: 8 bytes

replay detection support: Y

outbound ah sas:

outbound pcp sas:

protected vrf:

local ident (addr/mask/prot/port): (10.1.2.0/255.255.255.0/1/0)

remote ident (addr/mask/prot/port): (192.168.2.0/255.255.255.0/1/0)

current_peer: 192.168.1.2:500

PERMIT, flags={origin_is_acl,}

#pkts encaps: 0, #pkts encrypt: 0, #pkts digest 0

#pkts decaps: 0, #pkts decrypt: 0, #pkts verify 0

#pkts compressed: 0, #pkts decompressed: 0

#pkts not compressed: 0, #pkts compr. failed: 0

#pkts not decompressed: 0, #pkts decompress failed: 0

#send errors 0, #recv errors 0

local crypto endpt.: 10.1.1.1, remote crypto endpt.: 192.168.1.2

path mtu 1500, ip mtu 1500, ip mtu idb Ethernet0/0

current outbound spi: 0

inbound esp sas:

inbound ah sas:

inbound pcp sas:

outbound esp sas:

outbound ah sas:

outbound pcp sas:

可以看到有数据包通过并被加密

再查看下当前活动的IPSec连接

R1#sh crypto engine connections active

ID Interface IP-Address State Algorithm Encrypt Decrypt

1 Ethernet0/0 10.1.1.1 set HMAC_MD5+3DES_56_C 0 0

2000 Ethernet0/0 10.1.1.1 set HMAC_MD5+3DES_56_C 0 8

2001 Ethernet0/0 10.1.1.1 set HMAC_MD5+3DES_56_C 8 0