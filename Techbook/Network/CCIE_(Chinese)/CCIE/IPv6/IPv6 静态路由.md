# IPv6 静态路由

静态路由

2011年6月27日

17:17

在IPv6中，静态路由的写法分三种，分别为：

**1.直连静态路由（Directly Attached Static Routes）**

写法为只指定路由的出口，目标网络被认为是和此接口直连的，但此方法在接口为多路访问时，会有问题。

**例配：**

ipv6 route 2022:2:2:22::/64 s1/1

**说明：**到达目标网络2022:2:2:22::/64 的数据包从接口s1/1发出去。

**2.递归静态路由（Recursive Static Routes ）**

写法为只指定路由的下一跳地址，此方法在任何网络环境中可行。

**例配：**

r1(config)#ipv6 route 2022:2:2:22::/64 2012:1:1:11::2

**说明：**到达目标网络2022:2:2:22::/64 的数据包发给下一跳地址2012:1:1:11::2。

**3.完全静态路由（Fully Specified Static Routes）**

写法为同时指定出口和下一跳地址，只有当出口为多路访问时，并且确实需要明确指定下一跳时，才需要写完全静态路由，下一跳必须是和出口同网段的。

**例配：**

r1(config)#ipv6 route 2022:2:2:22::/64 f0/0 2012:1:1:11::2

**说明：**到达目标网络2022:2:2:22::/64 的数据包从接口F0/0发出去，并且交给下一跳地址2012:1:1:11::2。

=========================================================================================================

![IPv6%20%E9%9D%99%E6%80%81%E8%B7%AF%E7%94%B1%201503e31343e543dcb13f84fe3205c59f/image1.png](IPv6%20静态路由/image1.png)

**说明：**配置静态路由，使双方都能ping通互相loopback接口的网段。

由于是多路访问接口，所以省去配置直连静态路由的方法。

**1.网络初始配置：**

**（1）R1初始配置：**

r1(config)#ipv6 unicast-routing

r1(config)#int f0/0

r1(config-if)#ipv address 2012:1:1:11::1/64

r1(config)#int loopback 0

r1(config-if)#ipv6 address 2011:1:1:11::1/64

r1(config-if)#

**（2）R2初始配置：**

r2(config)#ipv unicast-routing

r2(config)#int f0/0

r2(config-if)#ipv address 2012:1:1:11::2/64

r2(config)#int loopback 0

r2(config-if)#ipv6 address 2022:2:2:22::2/64

r2(config-if)#

**2.在R1上配置递归静态路由**

**（1）配置递归静态路由**

r1(config)#ipv6 route 2022:2:2:22::/64 2012:1:1:11::2

**说明：**到达目标网络2022:2:2:22::/64 的数据包发给下一跳地址2012:1:1:11::2。

**（2）检查静态路由**

r1#show ipv6 route static

IPv6 Routing Table - 7 entries

Codes: C - Connected, L - Local, S - Static, R - RIP, B - BGP

U - Per-user Static route

I1 - ISIS L1, I2 - ISIS L2, IA - ISIS interarea, IS - ISIS summary

O - OSPF intra, OI - OSPF inter, OE1 - OSPF ext 1, OE2 - OSPF ext 2

ON1 - OSPF NSSA ext 1, ON2 - OSPF NSSA ext 2

D - EIGRP, EX - EIGRP external

S   2022:2:2:22::/64 [1/0]

via 2012:1:1:11::2

r1#

**说明：**从结果中看出，手工配置的递归静态路由已生效。

**（3）测试连通性**

r1#ping 2022:2:2:22::2

Type escape sequence to abort.

Sending 5, 100-byte ICMP Echos to 2022:2:2:22::2, timeout is 2 seconds:

!!!!!

Success rate is 100 percent (5/5), round-trip min/avg/max = 12/48/140 ms

r1#

**说明：**由于正确配置静态路由，R1到R2的loopback接口的网段通信正常。

**3.在R2上配置完全静态路由**

**（1）配置完全静态路由**

r2(config)#ipv6 route 2011:1:1:11::/64 f0/0 2012:1:1:11::1

**说明：**到达目标网络2011:1:1:11::/64  的数据包从接口F0/0发出去，并且交给下一跳地址2012:1:1:11::1。

**（2）检查静态路由**

r2#show ipv6 route static

IPv6 Routing Table - 7 entries

Codes: C - Connected, L - Local, S - Static, R - RIP, B - BGP

U - Per-user Static route

I1 - ISIS L1, I2 - ISIS L2, IA - ISIS interarea, IS - ISIS summary

O - OSPF intra, OI - OSPF inter, OE1 - OSPF ext 1, OE2 - OSPF ext 2

ON1 - OSPF NSSA ext 1, ON2 - OSPF NSSA ext 2

D - EIGRP, EX - EIGRP external

S   2011:1:1:11::/64 [1/0]

via 2012:1:1:11::1, FastEthernet0/0

r2#

**说明：**从结果中看出，手工配置的完全静态路由已生效。

**（3）测试连通性**

r2#ping 2011:1:1:11::1

Type escape sequence to abort.

Sending 5, 100-byte ICMP Echos to 2011:1:1:11::1, timeout is 2 seconds:

!!!!

- Mar 1 00:36:50.387: %CDP-4-DUPLEX_MISMATCH: duplex mismatch discovered on FastEthernet0/0 (not full duplex), with Router FastEthernet0/2 (full duplex).!

Success rate is 100 percent (5/5), round-trip min/avg/max = 16/92/156 ms

r2#

**说明：**由于正确配置静态路由，R2到R1的loopback接口的网段通信正常。