# IPv6 RIP (RIPng)

IPv6 RIP (RIPng)

2011年6月27日

17:20

> IPv6的RIP，所有路由规则与IPv4 RIPv2基本相同，不同之处是IPv4 RIPv2使用UDP 端口520，而RIPng使用UDP端口521，IPv4 RIPv2数据包更新使用地址224.0.0.9，而RIPng使用更新地址为FF02::9。
> 

**在配置RIPng时，方法不同于IPv4 RIP，RIPng是采用先配置进程，然后需要让哪些接口运行在RIPng下，就必须到相应的接口下明确指定，并不像IPv4 RIP那样在进程下通过network来发布。**

**配置RIPng**

![IPv6%20RIP%20(RIPng)%20dc2614af8bc74cc6a4fed74f6f2d6807/image1.png](IPv6%20RIP%20(RIPng)/image1.png)

**1.初始配置**

**（1）R1初始配置：**

r1(config)#ipv6 unicast-routing

r1(config)#int f0/0

r1(config-if)#ipv6 address 2012:1:1:11::1/64

r1(config)#int loopback 1

r1(config-if)#ipv6 address 3001:1:1:11::1/64

r1(config)#int loopback 2

r1(config-if)#ipv6 address 3002:1:1:11::1/64

r1(config)#int loopback 3

r1(config-if)#ipv6 address 3003:1:1:11::1/64

**（2）R2初始配置：**

r2(config)#ipv6 unicast-routing

r2(config)#int f0/0

r2(config-if)#ipv6 address 2012:1:1:11::2/64

r2(config)#int loopback 0

r2(config-if)#ipv6 address 2022:2:2:22::2/64

**2.启动RIPng进程**

**说明：**Cisco IOS最多同时支持4个RIPng进程，不同进程使用不同名字来区分，并且进程名为本地有效。

**（1）在R1上启动RIPng进程**

r1(config)#ipv6 router rip ccie

（2）在R2上启动RIPng进程

r2(config)#ipv6 router rip ccie

**3.配置RIPng接口**

**（1）将R1上的接口放进RIPng进程**

r1(config)#int f0/0

r1(config-if)#ipv6 rip ccie enable

r1(config)#int loopback 1

r1(config-if)#ipv6 rip ccie enable

**（2）将R2上的接口放进RIPng进程**

r2(config)#int f0/0

r2(config-if)#ipv6 rip ccie enable

r2(config)#int loopback 0

r2(config-if)#ipv6 rip ccie enable

**4.查看RIPng路由**

**（1）查看R1的RIPng路由**

r1#show ipv6 route rip

IPv6 Routing Table - 11 entries

Codes: C - Connected, L - Local, S - Static, R - RIP, B - BGP

U - Per-user Static route

I1 - ISIS L1, I2 - ISIS L2, IA - ISIS interarea, IS - ISIS summary

O - OSPF intra, OI - OSPF inter, OE1 - OSPF ext 1, OE2 - OSPF ext 2

ON1 - OSPF NSSA ext 1, ON2 - OSPF NSSA ext 2

D - EIGRP, EX - EIGRP external

R   2022:2:2:22::/64 [120/2]

via FE80::C200:DFF:FEC4:0, FastEthernet0/0

r1#

**说明：**由于RIPng配置正确，成功收到对方路由条目，并且可以看出，动态路由学习到的IPv6路由条目，下一跳地址均为对端的链路本地地址。

**（2）查看R2的RIPng路由**

r2#show ipv6 route rip

IPv6 Routing Table - 7 entries

Codes: C - Connected, L - Local, S - Static, R - RIP, B - BGP

U - Per-user Static route

I1 - ISIS L1, I2 - ISIS L2, IA - ISIS interarea, IS - ISIS summary

O - OSPF intra, OI - OSPF inter, OE1 - OSPF ext 1, OE2 - OSPF ext 2

ON1 - OSPF NSSA ext 1, ON2 - OSPF NSSA ext 2

D - EIGRP, EX - EIGRP external

R   3001:1:1:11::/64 [120/2]

via FE80::C200:BFF:FE48:0, FastEthernet0/0

r2#

**说明：**由于RIPng配置正确，成功收到对方路由条目。

**5.测试连通性**

**说明：**因为动态路由学习到的IPv6路由条目，下一跳地址均为对端的链路本地地址，所以如果到对端的链路本地地址不通，那么到对端IPv6网络也不会通。

**(1)测试R1到对端链路本地地址的连通性**

r1#ping FE80::C200:DFF:FEC4:0

Output Interface: FastEthernet0/0

Type escape sequence to abort.

Sending 5, 100-byte ICMP Echos to FE80::C200:DFF:FEC4:0, timeout is 2 seconds:

Packet sent with a source address of FE80::C200:DFF:FEC4:0

!!!!!

Success rate is 100 percent (5/5), round-trip min/avg/max = 32/70/184 ms

r1#

**说明：**到对端链路本地地址的通信正常。

**（2）测试R1到对端IPv6网络的连通性**

r1#ping 2022:2:2:22::2

Type escape sequence to abort.

Sending 5, 100-byte ICMP Echos to 2022:2:2:22::2, timeout is 2 seconds:

!!!!!

Success rate is 100 percent (5/5), round-trip min/avg/max = 12/75/240 ms

r1

**说明：**由于到对端链路本地地址的通信正常，所以到对端IPv6网络的通信也正常。

**（3）测试R2到对端IPv6网络的连通性**

r2#ping 3001:1:1:11::1

Type escape sequence to abort.

Sending 5, 100-byte ICMP Echos to 3001:1:1:11::1, timeout is 2 seconds:

!!!!!

Success rate is 100 percent (5/5), round-trip min/avg/max = 12/84/248 ms

r2#

**说明：**到对端IPv6网络的通信也正常。

**6.重分布IPv6网段**

**说明：**将R1上的剩余网段重分布进RIPng

**（1）在R1上配置重分布剩余网段进RIPng**

r1(config)#route-map con permit 10

r1(config-route-map)#match interface loopback 2

r1(config-route-map)#exit

r1(config)#route-map con permit 20

r1(config-route-map)#match interface loopback 3

r1(config-route-map)#exit

r1(config)#ipv6 router rip ccie

r1(config-rtr)#redistribute connected route-map con

r1(config-rtr)#

**（2）在R2上查看重分布进RIPng的剩余网段**

r2#show ipv6 route rip

IPv6 Routing Table - 9 entries

Codes: C - Connected, L - Local, S - Static, R - RIP, B - BGP

U - Per-user Static route

I1 - ISIS L1, I2 - ISIS L2, IA - ISIS interarea, IS - ISIS summary

O - OSPF intra, OI - OSPF inter, OE1 - OSPF ext 1, OE2 - OSPF ext 2

ON1 - OSPF NSSA ext 1, ON2 - OSPF NSSA ext 2

D - EIGRP, EX - EIGRP external

R   3001:1:1:11::/64 [120/2]

via FE80::C200:BFF:FE48:0, FastEthernet0/0

R   3002:1:1:11::/64 [120/2]

via FE80::C200:BFF:FE48:0, FastEthernet0/0

R   3003:1:1:11::/64 [120/2]

via FE80::C200:BFF:FE48:0, FastEthernet0/0

r2#

**说明：**可以看到，R1上的剩余网段成功被重分布进RIPng。

**7.过滤IPv6路由**

**说明：**在R2上过滤掉IPv6路由，只留想要的网段，使用distribute-list过滤

**（1）配置只留3002:1:1:11::/64网段**

r2(config)#ipv6 prefix-list abc permit 3002:1:1:11::/64

r2(config)#ipv6 router rip ccie

r2(config-rtr)#distribute-list prefix-list abc in f0/0

**注：**ipv6的 prefix-list同样支持ge , le等关键字来匹配范围。

**（2）查看过滤后的路由表情况**

r2#show ipv6 route rip

IPv6 Routing Table - 7 entries

Codes: C - Connected, L - Local, S - Static, R - RIP, B - BGP

U - Per-user Static route

I1 - ISIS L1, I2 - ISIS L2, IA - ISIS interarea, IS - ISIS summary

O - OSPF intra, OI - OSPF inter, OE1 - OSPF ext 1, OE2 - OSPF ext 2

ON1 - OSPF NSSA ext 1, ON2 - OSPF NSSA ext 2

D - EIGRP, EX - EIGRP external

R   3002:1:1:11::/64 [120/2]

via FE80::C200:BFF:FE48:0, FastEthernet0/0

r2#

**说明：**路由表中只剩想要的网段，说明过滤成功。