# IPSEC over GRE

IPSEC over GRE

2011年8月2日

22:02

IPSEC over GRE Configuration

技术特点:利用tunnel跑动态路由协议

实验 1 :

![IPSEC%20over%20GRE%2097144285dd1046bdb37c76554e47a262/image1.png](IPSEC%20over%20GRE/image1.png)

R2(config)#interface tunnel 23

R2(config-if)#ip address 23.1.1.2 255.255.255.0 <===起tunnel地址

R2(config-if)#tunnel source 12.1.1.2

R2(config-if)#tunnel destination 13.1.1.3

R2(config-if)#tunnel key 12345 <=== "tunnel key" 只是用于标识Tunnel,两端要对称,不是用于加密,在这可以不输入这条命令

R2(config-if)# router eigrp 90 <===不用宣告连接Internet的接口

R2(config-router)#no auto-summary

R2(config-router)#network 2.2.2.0 0.0.0.255 <====宣告环回口网络

R2(config-router)#network 100.2.2.0 0.0.0.255 <====宣告内部网络

R2(config-router)#network 23.1.1.0 0.0.0.255 <====宣告tunnel地址

- --------------------------------------------------

R3(config)#interface tunnel 23

R3(config-if)#ip address 23.1.1.3 255.255.255.0

R3(config-if)#tunnel source 13.1.1.3

R3(config-if)#tunnel destination 12.1.1.2

R3(config-if)#tunnel key 12345

R3(config-if)#router eigrp 90

R3(config-router)#no auto-summary

R3(config-router)#network 3.3.3.0 0.0.0.255

R3(config-router)#network 100.3.3.0 0.0.0.255

R3(config-router)#network 23.1.1.0 0.0.0.255

IKE Phase I Policy:

R2(config)#crypto isakmp policy 1

R2(config-isakmp)#authentication pre-share

R2(config-isakmp)#hash md5

R2(config-isakmp)#encryption 3des

R2(config-isakmp)#group 2

R2(config)#crypto isakmp key 0 wolf address 3.3.3.3 <===一定要用环回口地址

- ----------------------------------------------------

R3(config)#crypto isakmp policy 1

R3(config-isakmp)#authentication pre-share

R3(config-isakmp)#hash md5

R3(config-isakmp)#encryption 3des

R3(config-isakmp)#group 2

R3(config)#crypto isakmp key 0 wolf address 2.2.2.2

IPSec Phase II Policy:

R2(config)#crypto ipsec transform-set cisco esp-des esp-sha-hmac

R2(config)#access-list 101 permit ip 100.2.2.0 0.0.0.255 100.3.3.0 0.0.0.255

R2(config)#crypto map huawei local-address Loopback0 <===将"peer"改用"Loopback0"协商建立IPSEC通道(默认以物理口协商建立IPSEC通道)

R2(config)#crypto map huawei 10 ipsec-isakmp

R2(config-crypto-map)#set peer 3.3.3.3 <===可用公网接口地址,也可用环回口地址(与第一阶段设置无关)

以下四种情况每一次封装,先查路由表,再决定封装什么:

Peer设置为物理口,Map应用到公网接口时:

包结构: ...|tunnel source tunnel destination |GRE|source:100.2.2.2 destination:100.3.3.3|icmp...

由于应用到公网接口的Map,没有匹配到感兴趣流,所以没有加密直接发出.

Peer设置为物理口,Map应用到tunnel接口时:

包结构: ...|peer source peer destination |ESP|source:100.2.2.2 destination:100.3.3.3|icmp...

由于应用到tunnel接口的Map,匹配到感兴趣流,根据PEER的目标地址发出.(不经过tunnel,就出去了)

Peer设置为环回口,Map应用到公网接口时:

包结构: ...|tunnel source tunnel destination |GRE|source:100.2.2.2 destination:100.3.3.3|icmp...

由于应用到公网接口的Map,没有匹配到感兴趣流,所以没有加密直接发出.

Peer设置为环回口,Map应用到tunnel接口时:

包结构: ...|tunnel source tunnel destination |GRE|peer source peer destination |ESP|source:100.2.2.2 destination:100.3.3.3|icmp...

由于应用到tunnel接口的Map,匹配到感兴趣流,然后加密,根据PEER的目标地址,继续查路由表,得出下一跳为Tunnel...(经过tunnel,从物理接口发出)

R2(config-crypto-map)#set transform-set cisco

R2(config-crypto-map)#set pfs

R2(config-crypto-map)#match address 101

- ----------------------------------------------------------------------------

R3(config)#crypto ipsec transform-set cisco esp-des esp-sha-hmac

R3(config)#access-list 101 permit ip 100.3.3.0 0.0.0.255 100.2.2.0 0.0.0.255

R3(config)#crypto map huawei local-address Loopback0

R3(config)#crypto map huawei 10 ipsec-isakmp

R3(config-crypto-map)#set peer 2.2.2.2

R3(config-crypto-map)#set transform-set cisco

R3(config-crypto-map)#set pfs

R3(config-crypto-map)#match address 101

Apply VPN Configuration

R2(config)#interface ethernet 0/0

R2(config-if)#crypto map huawei

R2(config-if)#interface tunnel 23

R2(config-if)#crypto map huawei

- --------------------------------------------

R3(config)#interface tunnel 23

R3(config-if)#crypto map huawei

R3#show crypto engine connections active

ID Interface IP-Address State Algorithm Encrypt Decrypt

1 Tunnel23 23.1.1.3 set HMAC_MD5+3DES_56_C 0 0

2001 Tunnel23 3.3.3.3 set DES+SHA 0 8

2002 Tunnel23 3.3.3.3 set DES+SHA 8 0

- -----------------------------------------------------------

R2#show crypto isakmp sa

dst src state conn-id slot status

1.1.1.1 2.2.2.2 QM_IDLE 1 0 ACTIVE

- -----------------------------------

R2#show crypto isakmp peers

Peer: 1.1.1.1 Port: 500 Local: 2.2.2.2

Phase1 id: 1.1.1.1

- -------------------------------

R2#show crypto ipsec sa

interface: Ethernet0/0

Crypto map tag: cisco, local addr 2.2.2.2

protected vrf: (none)

local ident (addr/mask/prot/port): (10.1.2.0/255.255.255.0/0/0)

remote ident (addr/mask/prot/port): (10.1.1.0/255.255.255.0/0/0)

current_peer 1.1.1.1 port 500

PERMIT, flags={origin_is_acl,}

#pkts encaps: 4, #pkts encrypt: 4, #pkts digest: 4

#pkts decaps: 4, #pkts decrypt: 4, #pkts verify: 4

#pkts compressed: 0, #pkts decompressed: 0

#pkts not compressed: 0, #pkts compr. failed: 0

#pkts not decompressed: 0, #pkts decompress failed: 0

#send errors 1, #recv errors 0

local crypto endpt.: 2.2.2.2, remote crypto endpt.: 1.1.1.1

path mtu 1500, ip mtu 1500

current outbound spi: 0x12D1DDFE(315743742)

inbound esp sas:

spi: 0xC2686DB7(3261623735)

transform: esp-des esp-sha-hmac ,

in use settings ={Tunnel, }

conn id: 2001, flow_id: 1, crypto map: cisco

sa timing: remaining key lifetime (k/sec): (4386784/3492)

IV size: 8 bytes

replay detection support: Y

Status: ACTIVE

inbound ah sas:

inbound pcp sas:

outbound esp sas:

spi: 0x12D1DDFE(315743742)

transform: esp-des esp-sha-hmac ,

in use settings ={Tunnel, }

conn id: 2002, flow_id: 2, crypto map: cisco

sa timing: remaining key lifetime (k/sec): (4386784/3490)

IV size: 8 bytes

replay detection support: Y

Status: ACTIVE

outbound ah sas:

outbound pcp sas:

interface: Tunnel21

Crypto map tag: cisco, local addr 2.2.2.2

protected vrf: (none)

local ident (addr/mask/prot/port): (10.1.2.0/255.255.255.0/0/0)

remote ident (addr/mask/prot/port): (10.1.1.0/255.255.255.0/0/0)

current_peer 1.1.1.1 port 500

PERMIT, flags={origin_is_acl,}

#pkts encaps: 4, #pkts encrypt: 4, #pkts digest: 4

#pkts decaps: 4, #pkts decrypt: 4, #pkts verify: 4

#pkts compressed: 0, #pkts decompressed: 0

#pkts not compressed: 0, #pkts compr. failed: 0

#pkts not decompressed: 0, #pkts decompress failed: 0

#send errors 1, #recv errors 0

local crypto endpt.: 2.2.2.2, remote crypto endpt.: 1.1.1.1

path mtu 1500, ip mtu 1500

current outbound spi: 0x12D1DDFE(315743742)

inbound esp sas:

spi: 0xC2686DB7(3261623735)

transform: esp-des esp-sha-hmac ,

in use settings ={Tunnel, }

conn id: 2001, flow_id: 1, crypto map: cisco

sa timing: remaining key lifetime (k/sec): (4386784/3488)

IV size: 8 bytes

replay detection support: Y

Status: ACTIVE

inbound ah sas:

inbound pcp sas:

outbound esp sas:

spi: 0x12D1DDFE(315743742)

transform: esp-des esp-sha-hmac ,

in use settings ={Tunnel, }

conn id: 2002, flow_id: 2, crypto map: cisco

sa timing: remaining key lifetime (k/sec): (4386784/3487)

IV size: 8 bytes

replay detection support: Y

Status: ACTIVE

outbound ah sas:

outbound pcp sas:

![IPSEC%20over%20GRE%2097144285dd1046bdb37c76554e47a262/image2.jpg](IPSEC%20over%20GRE/image2.jpg)