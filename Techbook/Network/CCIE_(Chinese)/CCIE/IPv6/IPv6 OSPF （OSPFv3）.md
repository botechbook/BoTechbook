# IPv6 OSPF （OSPFv3）

IPv6 OSPF （OSPFv3）

2011年6月27日

17:22

**IPv6 OSPF （OSPFv3）**

> OSPFv3与OSPFv2（IPv4 OSPF）的原理都是相同的，OSPFv3选举Router-ID的规则与OSPFv2相同，OSPFv3也是选择路由器上的IPv4地址作为Router-ID，如果设备上没有配置IPv4地址，那么必须手工指定Router-ID。在配置OSPFv3时，先配置进程，然后需要让哪些接口运行在OSPFv3下，就必须到相应的接口下明确指定，并不像OSPFv2那样在进程下通过network来发布。
> 

**配置OSPFv3**

![IPv6%20OSPF%20%EF%BC%88OSPFv3%EF%BC%89%208f44cc9012ef44d79842f773cda50739/image1.png](IPv6%20OSPF%20（OSPFv3）/image1.png)

**1.初始配置**

**（1）R1初始配置：**

r1(config)#ipv6 unicast-routing

r1(config)#interface f0/0

r1(config-if)#ipv6 address 2012:1:1:11::1/64

r1(config)#int loopback 1

r1(config-if)#ipv6 address 3011:1:1:11::1/64

r1(config)#int loopback 2

r1(config-if)#ipv6 address 3011:1:1:12::1/64

r1(config)#int loopback 3

r1(config-if)#ipv6 address 3011:1:1:13::1/64

**（2）R2初始配置：**

r2(config)#ipv6 unicast-routing

r2(config)#interface f0/0

r2(config-if)#ipv6 address 2012:1:1:11::2/64

r2(config)#interface s1/0

r2(config-if)#encapsulation frame-relay

r2(config-if)#no frame-relay inverse-arp

r2(config-if)#no arp frame-relay

r2(config-if)#ipv6 address 2023:1:1:11::2/64

r2(config-if)#frame-relay map ipv6 2023:1:1:11::3 203 broadcast

r2(config-if)#

**（3）R3初始配置：**

r3(config)#ipv6 unicast-routing

r3(config)#interface s1/0

r3(config-if)#encapsulation frame-relay

r3(config-if)#no frame-relay inverse-arp

r3(config-if)#no arp frame-relay

r3(config-if)#ipv6 address 2023:1:1:11::3/64

r3(config-if)#frame-relay map ipv6 2023:1:1:11::2 302 broadcast

**2.启动OSPFv3进程**

**（1）启动R1的OSPFv3进程**

r1(config)#ipv6 router ospf 2

r1(config-rtr)#router-id 1.1.1.1

**说明：**由于没有配置IPv4地址，所以必须手工配置Router-ID

**（2）启动R2的OSPFv3进程**

r2(config)#ipv6 router ospf 2

r2(config-rtr)#router-id 2.2.2.2

（3）启动R3的OSPFv3进程

r3(config)#ipv6 router ospf 2

r3(config-rtr)#router-id 3.3.3.3

**3.配置OSPFv3接口**

**（1）将R1上的接口放进OSPFv3进程**

r1(config)#int f0/0

r1(config-if)#ipv6 ospf 2 area 0

r1(config)#int loopback 1

r1(config-if)#ipv6 ospf 2 area 0

**（2）将R2上的接口放进OSPFv3进程**

r2(config)#int f0/0

r2(config-if)#ipv6 ospf 2 area 0

r2(config)#int s1/0

r2(config-if)#ipv6 ospf 2 area 1

**（3）将R3上的接口放进OSPFv3进程**

r3(config)#int s1/0

r3(config-if)#ipv6 ospf 2 area 1

**4.查看OSPFv3邻居**

**（1）查看r1邻居：**

r1#show ipv6 ospf neighbor

Neighbor ID     Pri   State           Dead Time   Interface ID    Interface

2.2.2.2           1   FULL/BDR        00:00:39    4               FastEthernet0/0

r1#

**说明：**R1与R2的OSPFv3邻居正常。

**（2）查看r2邻居：**

r2#show ipv6 ospf neighbor

Neighbor ID     Pri   State           Dead Time   Interface ID    Interface

1.1.1.1           1   FULL/DR         00:00:35    4               FastEthernet0/0

r2#

**说明：**R2与R2的OSPFv3邻居正常，但与R3的邻居没有。

（3）**（3）查看r3邻居：**

r3#show ipv6 ospf neighbor

r3#

**说明：**R3没有OSPFv3邻居。

**5.解决OSPFv3邻居问题**

**说明：**由于R2与R3之间属于NBMA非广播网络，所以无法自动建邻居，要解决邻居问题，有两种方法：第一，手工指定邻居，在指定时，只须在一方指定即可，并且OSPFv3在手工指定邻居时，需要到接口下指定而不是在进程下指定，并且指定的为对方链路本地地址。第二，将网络类型从非广播网络类型改为允许广播的网络类型，如改为Point-to-point类型。

**（1）查看R3连R2接口的链路本地地址**

r3#show ipv6 interface brief s1/0

Serial1/0                  [up/up]

FE80::C200:DFF:FEAC:0

2023:1:1:11::3

r3#

**（2）在R2上指定R3为邻居，在接口下指定对方的链路本地地址**

r2(config)#int s1/0

r2(config-if)#ipv6 ospf neighbor FE80::C200:DFF:FEAC:0

r2(config-if)#

**（3）测试R2到R3接口链路本地地址的连通性**

r2#ping FE80::C200:DFF:FEAC:0

Output Interface: Serial1/0

Type escape sequence to abort.

Sending 5, 100-byte ICMP Echos to FE80::C200:DFF:FEAC:0, timeout is 2 seconds:

Packet sent with a source address of FE80::C200:BFF:FE94:0

.....

Success rate is 0 percent (0/5)

r2#

**说明：**由于指定邻居时，指定为对方接口的链路本地地址，所以双方接口的链路本地地址不通，邻居将仍然不能建立。

**（4）解决帧中继网络下双方接口的链路本地地址的PVC映射**

注：必须互相映射

R2:

r2(config)#int s1/0

r2(config-if)#fram map ipv6 FE80::C200:DFF:FEAC:0 203 broadcast

R3:

R3(config)#int s1/0

R3config-if)#fram map ipv6 FE80::C200:BFF:FE94:0 302 broadcast

**(5)查看邻居**

r3#show ipv6 ospf neighbor

Neighbor ID     Pri   State           Dead Time   Interface ID    Interface

2.2.2.2           1   FULL/BDR        00:01:42    6               Serial1/0

r3#

**说明：**由于已经手工指定邻居，并且也映射了双方的链路本地地址，所以邻居成功建立。

**6.查看OSPFv3路由**

**（1）在R1上查看OSPFv3路由**

r1#sh ipv6 route ospf

IPv6 Routing Table - 11 entries

Codes: C - Connected, L - Local, S - Static, R - RIP, B - BGP

U - Per-user Static route

I1 - ISIS L1, I2 - ISIS L2, IA - ISIS interarea, IS - ISIS summary

O - OSPF intra, OI - OSPF inter, OE1 - OSPF ext 1, OE2 - OSPF ext 2

ON1 - OSPF NSSA ext 1, ON2 - OSPF NSSA ext 2

D - EIGRP, EX - EIGRP external

OI  2023:1:1:11::/64 [110/74]

via FE80::C200:BFF:FE94:0, FastEthernet0/0

r1#

**说明：**由于邻居已经全部正常建立，所以学习到了远程网络的路由条目。

**（2）在R2上查看OSPFv3路由**

r2#show ipv6 route ospf

IPv6 Routing Table - 7 entries

Codes: C - Connected, L - Local, S - Static, R - RIP, B - BGP

U - Per-user Static route

I1 - ISIS L1, I2 - ISIS L2, IA - ISIS interarea, IS - ISIS summary

O - OSPF intra, OI - OSPF inter, OE1 - OSPF ext 1, OE2 - OSPF ext 2

ON1 - OSPF NSSA ext 1, ON2 - OSPF NSSA ext 2

D - EIGRP, EX - EIGRP external

O   3011:1:1:11::1/128 [110/10]

via FE80::C200:AFF:FE28:0, FastEthernet0/0

r2#

**说明：**由于邻居已经全部正常建立，所以学习到了远程网络的路由条目。

**（3）在R3上查看OSPFv3路由**

r3#show ipv6 route ospf

IPv6 Routing Table - 6 entries

Codes: C - Connected, L - Local, S - Static, R - RIP, B - BGP

U - Per-user Static route

I1 - ISIS L1, I2 - ISIS L2, IA - ISIS interarea, IS - ISIS summary

O - OSPF intra, OI - OSPF inter, OE1 - OSPF ext 1, OE2 - OSPF ext 2

ON1 - OSPF NSSA ext 1, ON2 - OSPF NSSA ext 2

D - EIGRP, EX - EIGRP external

OI  2012:1:1:11::/64 [110/74]

via FE80::C200:BFF:FE94:0, Serial1/0

OI  3011:1:1:11::1/128 [110/74]

via FE80::C200:BFF:FE94:0, Serial1/0

r3#

**说明：**由于邻居已经全部正常建立，所以学习到了远程网络的路由条目。

**7.解决OSPFv3路由掩码问题**

**说明：**由于学习到的路由中，属于loopback接口的网段原本为64位，而学习到的为128位，为主机路由，所以应让路由掩码与原来的掩码一致，需要将网络类型改为Point-to-point类型。

**（1）在R1改loopback接口的网络类型改为Point-to-point**

r1(config)#int loopback 1

r1(config-if)#ipv6 ospf network point-to-point

r1(config-if)#

**（2）查看改后的路由情况**

r2#show ipv6 route ospf

IPv6 Routing Table - 9 entries

Codes: C - Connected, L - Local, S - Static, R - RIP, B - BGP

U - Per-user Static route

I1 - ISIS L1, I2 - ISIS L2, IA - ISIS interarea, IS - ISIS summary

O - OSPF intra, OI - OSPF inter, OE1 - OSPF ext 1, OE2 - OSPF ext 2

ON1 - OSPF NSSA ext 1, ON2 - OSPF NSSA ext 2

D - EIGRP, EX - EIGRP external

O   3011:1:1:11::/64 [110/11]

via FE80::C200:AFF:FE28:0, FastEthernet0/0

r2#

**说明：**已经成功变成原来的掩码位数。

**8.重分布IPv6网段**

**说明：**将R1上的剩余网段重分布进OSPFv3

**（1）在R1上配置重分布剩余网段进OSPFv3**

r1(config)#route-map con permit 10

r1(config-route-map)#match interface loopback 2

r1(config-route-map)#exit

r1(config)#route-map con permit 20

r1(config-route-map)#match interface loopback 3

r1(config-route-map)#exit

r1(config)#ipv6 router ospf 2

r1(config-rtr)#redistribute connected route-map con

**（2）在R2上查看重分布进OSPFv3的剩余网段**

r2#show ipv6 route ospf

IPv6 Routing Table - 9 entries

Codes: C - Connected, L - Local, S - Static, R - RIP, B - BGP

U - Per-user Static route

I1 - ISIS L1, I2 - ISIS L2, IA - ISIS interarea, IS - ISIS summary

O - OSPF intra, OI - OSPF inter, OE1 - OSPF ext 1, OE2 - OSPF ext 2

ON1 - OSPF NSSA ext 1, ON2 - OSPF NSSA ext 2

D - EIGRP, EX - EIGRP external

O   3011:1:1:11::/64 [110/11]

via FE80::C200:AFF:FE28:0, FastEthernet0/0

OE2  3011:1:1:12::/64 [110/20]

via FE80::C200:AFF:FE28:0, FastEthernet0/0

OE2  3011:1:1:13::/64 [110/20]

via FE80::C200:AFF:FE28:0, FastEthernet0/0

r2#

**说明：**可以看到，R1上的剩余网段成功被重分布进OSPFv3。

**（3）在R3上查看重分布进OSPFv3的剩余网段**

r3#show ipv6 route ospf

IPv6 Routing Table - 8 entries

Codes: C - Connected, L - Local, S - Static, R - RIP, B - BGP

U - Per-user Static route

I1 - ISIS L1, I2 - ISIS L2, IA - ISIS interarea, IS - ISIS summary

O - OSPF intra, OI - OSPF inter, OE1 - OSPF ext 1, OE2 - OSPF ext 2

ON1 - OSPF NSSA ext 1, ON2 - OSPF NSSA ext 2

D - EIGRP, EX - EIGRP external

OI  2012:1:1:11::/64 [110/74]

via FE80::C200:BFF:FE94:0, Serial1/0

OI  3011:1:1:11::/64 [110/75]

via FE80::C200:BFF:FE94:0, Serial1/0

OE2  3011:1:1:12::/64 [110/20]

via FE80::C200:BFF:FE94:0, Serial1/0

OE2  3011:1:1:13::/64 [110/20]

via FE80::C200:BFF:FE94:0, Serial1/0

r3#

**说明：**可以看到，R1上的剩余网段成功被重分布进OSPFv3。

**9.过滤IPv6路由**

**说明：**在R3上过滤掉IPv6路由，只留想要的网段，使用distribute-list过滤

**（1）配置只留3011打头的网段**

r3(config)#ipv6 prefix-list abc permit 3011::/16 ge 64 le 64

r3(config)#ipv6 router ospf 2

r3(config-rtr)#distribute-list prefix-list abc in s1/0

**（2）查看过滤后的路由表情况**

r3#show ipv6 route ospf

IPv6 Routing Table - 7 entries

Codes: C - Connected, L - Local, S - Static, R - RIP, B - BGP

U - Per-user Static route

I1 - ISIS L1, I2 - ISIS L2, IA - ISIS interarea, IS - ISIS summary

O - OSPF intra, OI - OSPF inter, OE1 - OSPF ext 1, OE2 - OSPF ext 2

ON1 - OSPF NSSA ext 1, ON2 - OSPF NSSA ext 2

D - EIGRP, EX - EIGRP external

OI  3011:1:1:11::/64 [110/75]

via FE80::C200:BFF:FE94:0, Serial1/0

OE2  3011:1:1:12::/64 [110/20]

via FE80::C200:BFF:FE94:0, Serial1/0

OE2  3011:1:1:13::/64 [110/20]

via FE80::C200:BFF:FE94:0, Serial1/0

r3#

**说明：**路由表中只剩3011打头的网段了，说明过滤成功。

**10.汇总OSPFv3外部路由**

**说明：**对从外部重分布进OSPFv3的路由进行汇总，OSPF内的路由汇总，命令格式基本同IPv4，需要注意的是，汇总必须在重分布的路由器上配置，即必须在ASBR上配置。

**（1）在ASBR（R1）上配置外部路由的汇总**

**说明：**将3011:1:1:11::/64 ，3011:1:1:12::/64 ，3011:1:1:13::/64三条路由汇总成3011:1:1::/48

r1(config)#ipv6 router ospf 2

r1(config-rtr)#summary-prefix 3011:1:1::/48

r1(config-rtr)#

**(2)在R2上查看汇总后的路由表情况**

r2#show ipv6 route ospf

IPv6 Routing Table - 8 entries

Codes: C - Connected, L - Local, S - Static, R - RIP, B - BGP

U - Per-user Static route

I1 - ISIS L1, I2 - ISIS L2, IA - ISIS interarea, IS - ISIS summary

O - OSPF intra, OI - OSPF inter, OE1 - OSPF ext 1, OE2 - OSPF ext 2

ON1 - OSPF NSSA ext 1, ON2 - OSPF NSSA ext 2

D - EIGRP, EX - EIGRP external

OE2  3011:1:1::/48 [110/20]

via FE80::C200:AFF:FE28:0, FastEthernet0/0

O   3011:1:1:11::/64 [110/11]

via FE80::C200:AFF:FE28:0, FastEthernet0/0

r2#

**说明：**可以看到，汇总成功。