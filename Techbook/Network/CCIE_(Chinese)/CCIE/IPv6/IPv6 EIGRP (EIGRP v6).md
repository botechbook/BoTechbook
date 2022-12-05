# IPv6 EIGRP (EIGRP v6)

IPv6 EIGRP (EIGRP v6)

2011年6月27日

17:32

**IPv6 EIGRP (EIGRP v6)**

> EIGRP v6与IPv4 EIGRP的原理都是相同的，但是EIGRP v6必须有router-id才能运行，所以在EIGRP v6不能获得router-id时，请手工配置router-id；更多的是EIGRP v6进程有个shutdown的特性，要用no shutdown开启进程；在配置EIGRP v6时，先配置进程，然后需要让哪些接口运行在EIGRP v6下，就必须到相应的接口下明确指定，并不像IPv4 EIGRP那样通过network来发布。
> 

**EIGRP hello时间默认是5秒一个，在低链路是60秒一个，比如NBMA，或者所有低于或等于T1的链路（1.544M）。Hold time是hello的三倍。**

**配置EIGRP v6**

![IPv6%20EIGRP%20(EIGRP%20v6)%20ee074ddaa91f4628b51287d4603a5fb0/image1.png](IPv6%20EIGRP%20(EIGRP%20v6)/image1.png)

**1.初始配置**

**（1）R1初始配置：**

**r1(config)#ipv6 unicast-routing**

**r1(config)#int f0/0**

**r1(config-if)#ipv6 address 2012:1:1:11::1/64**

**r1(config)#int loopback 1**

**r1(config-if)#ipv6 address 3001:1:1:11::1/64**

**r1(config)#int loopback 2**

**r1(config-if)#ipv6 address 3002:1:1:11::1/64**

**r1(config)#int loopback 3**

**r1(config-if)#ipv6 address 3003:1:1:11::1/64**

**（2）R2初始配置：**

**r2(config)#ipv6 unicast-routing**

**r2(config)#int f0/0**

**r2(config-if)#ipv6 address 2012:1:1:11::2/64**

**r2(config)#int loopback 0**

**r2(config-if)#ipv6 address 2022:2:2:22::2/64**

**2.配置EIGRP v6进程**

**（1）在R1上启动EIGRP v6进程**

**r1(config)#ipv6 router eigrp 10**

**r1(config-rtr)#router-id 1.1.1.1**

**（2）在R1上启动EIGRP v6进程**

**r2(config)#ipv6 router eigrp 10**

**r2(config-rtr)#router-id 2.2.2.2**

**3.配置EIGRP v6接口**

**（1）将R1上的接口放进EIGRP v6进程**

**r1(config)#interface f0/0**

**r1(config-if)#ipv6 eigrp 10**

**r1(config)#int loopback 1**

**r1(config-if)#ipv6 eigrp 10**

**（2）将R2上的接口放进EIGRP v6进程**

**r2(config)#int f0/0**

**r2(config-if)#ipv6 eigrp 10**

**r2(config)#int loopback 0**

**r2(config-if)#ipv6 eigrp 10**

**（3）查看EIGRP v6邻居状态**

**r1#show ipv6 eigrp neighbors**

**IPv6-EIGRP neighbors for process 10**

**% EIGRP 10 is in SHUTDOWN**

**r1#**

**说明：从结果中看出，EIGRP v进程默认是shutdown的，必须手工开启。**

**（4）开启EIGRP v6进程**

**r1(config)#ipv6 router eigrp 10**

**r1(config-rtr)#no shutdown**

**（5）查看邻居**

**r1#show ipv6 eigrp neighbors**

**IPv6-EIGRP neighbors for process 10**

**H   Address                 Interface       Hold Uptime   SRTT   RTO  Q  Seq**

**(sec)         (ms)       Cnt Num**

**0   Link-local address:     Fa0/0             11 00:00:36  192  1152  0  2**

> FE80::C200:AFF:FE50:0
> 

**说明：开启EIGRP v6进程后，邻居正常建立。**

**4.查看EIGRP v6路由**

**（1）查看R1的EIGRP v6路由**

**r1#show ipv6 route eigrp**

**IPv6 Routing Table - 11 entries**

**Codes: C - Connected, L - Local, S - Static, R - RIP, B - BGP**

**U - Per-user Static route**

**I1 - ISIS L1, I2 - ISIS L2, IA - ISIS interarea, IS - ISIS summary**

**O - OSPF intra, OI - OSPF inter, OE1 - OSPF ext 1, OE2 - OSPF ext 2**

**ON1 - OSPF NSSA ext 1, ON2 - OSPF NSSA ext 2**

**D - EIGRP, EX - EIGRP external**

**D   2022:2:2:22::/64 [90/409600]**

**via FE80::C200:AFF:FE50:0, FastEthernet0/0**

**r1#**

**说明：由于EIGRP v6配置正确，成功收到对方路由条目。**

**（2）查看R2的EIGRP v6路由**

**r2#sh ipv6 route eigrp**

**IPv6 Routing Table - 7 entries**

**Codes: C - Connected, L - Local, S - Static, R - RIP, B - BGP**

**U - Per-user Static route**

**I1 - ISIS L1, I2 - ISIS L2, IA - ISIS interarea, IS - ISIS summary**

**O - OSPF intra, OI - OSPF inter, OE1 - OSPF ext 1, OE2 - OSPF ext 2**

**ON1 - OSPF NSSA ext 1, ON2 - OSPF NSSA ext 2**

**D - EIGRP, EX - EIGRP external**

**D   3001:1:1:11::/64 [90/409600]**

**via FE80::C200:9FF:FE54:0, FastEthernet0/0**

**r2#**

**说明：由于EIGRP v6配置正确，成功收到对方路由条目。**

**5.重分布IPv6网段**

**说明：将R1上的剩余网段重分布进EIGRP v6**

**（1）在R1上配置重分布剩余网段进EIGRP v6**

**r1(config)#route-map con permit 10**

**r1(config-route-map)#match interface loopback 2**

**r1(config-route-map)#exit**

**r1(config)#route-map con permit 20**

**r1(config-route-map)#match interface loopback 3**

**r1(config)#ipv6 router eigrp 10**

**r1(config-rtr)#redistribute connected route-map con**

**r1(config-rtr)#exit**

**（2）在R2上查看重分布进EIGRP v6的剩余网段**

**r2#sh ipv6 route eigrp**

**IPv6 Routing Table - 9 entries**

**Codes: C - Connected, L - Local, S - Static, R - RIP, B - BGP**

**U - Per-user Static route**

**I1 - ISIS L1, I2 - ISIS L2, IA - ISIS interarea, IS - ISIS summary**

**O - OSPF intra, OI - OSPF inter, OE1 - OSPF ext 1, OE2 - OSPF ext 2**

**ON1 - OSPF NSSA ext 1, ON2 - OSPF NSSA ext 2**

**D - EIGRP, EX - EIGRP external**

**D   3001:1:1:11::/64 [90/409600]**

**via FE80::C200:9FF:FE54:0, FastEthernet0/0**

**EX  3002:1:1:11::/64 [170/409600]**

**via FE80::C200:9FF:FE54:0, FastEthernet0/0**

**EX  3003:1:1:11::/64 [170/409600]**

**via FE80::C200:9FF:FE54:0, FastEthernet0/0**

**r2#**

**说明：可以看到，R1上的剩余网段成功被重分布进EIGRP v6。**

**6.过滤IPv6路由**

**说明：在R2上过滤掉IPv6路由，只留想要的网段，使用distribute-list过滤**

**（1）配置只留3002:1:1:11::/64网段**

**r2(config)#ipv6 prefix-list abc permit 3002:1:1:11::/64**

**r2(config)#ipv6 router eigrp 10**

**r2(config-rtr)#distribute-list prefix-list abc in f0/0**

**r2(config-rtr)#**

**（2）查看过滤后的路由表情况**

**r2#sh ipv6 route eigrp**

**IPv6 Routing Table - 7 entries**

**Codes: C - Connected, L - Local, S - Static, R - RIP, B - BGP**

**U - Per-user Static route**

**I1 - ISIS L1, I2 - ISIS L2, IA - ISIS interarea, IS - ISIS summary**

**O - OSPF intra, OI - OSPF inter, OE1 - OSPF ext 1, OE2 - OSPF ext 2**

**ON1 - OSPF NSSA ext 1, ON2 - OSPF NSSA ext 2**

**D - EIGRP, EX - EIGRP external**

**EX  3002:1:1:11::/64 [170/409600]**

**via FE80::C200:9FF:FE54:0, FastEthernet0/0**

**r2#**

**说明：路由表中只剩想要的网段，说明过滤成功。**