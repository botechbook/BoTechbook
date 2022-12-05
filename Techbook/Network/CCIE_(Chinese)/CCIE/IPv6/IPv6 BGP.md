# IPv6 BGP

IPv6 BGP

2011年6月27日

17:36

**IPv6 BGP**

**普通情况下配置的BGP，是用来传递IPv4路由的，所传递的信息是IPv4的协议，如果要让BGP传递其它路由或协议，这就需要将BGP扩展为支持更多协议的BGP，如扩展BGP支持IPv6协议，支持vpnv4，这样的支持多协议的BGP，称为Multiprotocol BGP，即MP-BGP**

**要配置MP-BGP，就需要为除IPv4之外的协议单独创建address-family，但是建立BGP邻居和正常情况下一样，当邻居建立之后，还得到address-family下活动，这是MP-BGP的特性，而需要发布的网段，也需要到address-family下发布。传递单播IPv6的address-family应该是address-family ipv6 unicast，但关键字unicast如果省略，默认就是address-family ipv6 unicast。下面根据以上特征，来配置MP-BGP传递IPv6路由。**

**配置IPv6 MP-BGP**

![IPv6%20BGP%20a050f47a60f94e5fadd8ab6979c779e3/image1.png](IPv6%20BGP/image1.png)

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

**2.配置MP-BGP中的IPv6邻居**

**说明：所有邻居正常配置，但需要到IPv6的address-family下激活邻居。**

**（1）在R1上配置BGP邻居**

**r1(config)#router bgp 100**

**r1(config-router)#bgp router-id 1.1.1.1**

**r1(config-router)#neighbor 2012:1:1:11::2 remote-as 100**

**r1(config-router)#address-family ipv6**

**r1(config-router-af)#neighbor 2012:1:1:11::2 activate**

**r1(config-router-af)#exit**

**（2）在R2上配置BGP邻居**

**r2(config)#router bgp 100**

**r2(config-router)#bgp router-id 2.2.2.2**

**r2(config-router)#neighbor 2012:1:1:11::1 remote-as 100**

**r2(config-router)#address-family ipv6**

**r2(config-router-af)#neighbor 2012:1:1:11::1 activate**

**r2(config-router-af)#exit**

**3.查看IPv6 BGP邻居**

**（1）在R1上查看IPv6 BGP邻居**

**r1#show bgp sum**

**BGP router identifier 1.1.1.1, local AS number 100**

**BGP table version is 1, main routing table version 1**

**Neighbor        V    AS MsgRcvd MsgSent   TblVer  InQ OutQ Up/Down  State/PfxRcd**

**2012:1:1:11::2  4   100       5       4        1    0    0 00:01:35        0**

**r1#**

**说明：由于配置正确，所以已正常建立IPv6 BGP邻居命令。命令show bgp sum为隐藏命令。**

**（2）在R2上查看IPv6 BGP邻居**

**r2#show bgp sum**

**BGP router identifier 2.2.2.2, local AS number 100**

**BGP table version is 1, main routing table version 1**

**Neighbor        V    AS MsgRcvd MsgSent   TblVer  InQ OutQ Up/Down  State/PfxRcd**

**2012:1:1:11::1  4   100       5       6        1    0    0 00:02:02        0**

**r2#**

**说明：由于配置正确，所以已正常建立IPv6 BGP邻居命令。**

**4.发布IPv6路由进IPv6 BGP**

**(1)在R1上发布路由进IPv6 BGP**

**r1(config)#router bgp 100**

**r1(config-router)#address-family ipv6**

**r1(config-router-af)#network 3001:1:1:11::/64**

**(2)在R2上发布路由进IPv6 BGP**

**r2(config)#router bgp 100**

**r2(config-router)#address-family ipv6**

**r2(config-router-af)#network 2022:2:2:22::/64**

**(3)在R1上查看IPv6 BGP路由**

**r1#show bgp all**

**For address family: IPv6 Unicast**

**BGP table version is 3, local router ID is 1.1.1.1**

**Status codes: s suppressed, d damped, h history, * valid, > best, i - internal,**

**r RIB-failure, S Stale**

**Origin codes: i - IGP, e - EGP, ? - incomplete**

**Network          Next Hop            Metric LocPrf Weight Path**

- **>i2022:2:2:22::/64 2012:1:1:11::2 0 100 0 i**
- **> 3001:1:1:11::/64 :: 0 32768 i**

**r1#**

**说明：已成功学习到对方邻居发来的IPv6路由。**

**(4)在R2上查看IPv6 BGP路由**

**r2#show bgp all**

**For address family: IPv6 Unicast**

**BGP table version is 3, local router ID is 2.2.2.2**

**Status codes: s suppressed, d damped, h history, * valid, > best, i - internal,**

**r RIB-failure, S Stale**

**Origin codes: i - IGP, e - EGP, ? - incomplete**

**Network          Next Hop            Metric LocPrf Weight Path**

- **> 2022:2:2:22::/64 :: 0 32768 i**
- **>i3001:1:1:11::/64 2012:1:1:11::1 0 100 0 i**

**r2#**

**说明：已成功学习到对方邻居发来的IPv6路由。**

**（5）测试网络连通性**

**r1#ping 2022:2:2:22::2**

**Type escape sequence to abort.**

**Sending 5, 100-byte ICMP Echos to 2022:2:2:22::2, timeout is 2 seconds:**

**!!!!!**

**Success rate is 100 percent (5/5), round-trip min/avg/max = 12/96/208 ms**

**r1#**

**r2#ping 3001:1:1:11::1**

**Type escape sequence to abort.**

**Sending 5, 100-byte ICMP Echos to 3001:1:1:11::1, timeout is 2 seconds:**

**!!!!!**

**Success rate is 100 percent (5/5), round-trip min/avg/max = 24/88/200 ms**

**r2#**

**说明：由于双方路由学习正常，所以网络连通性正常。**

**5.重分布IPv6网段**

**说明：将R1上的剩余网段重分布进IPv6 BGP**

**（1）在R1上配置重分布剩余网段进IPv6 BGP**

**r1(config)#route-map con permit 10**

**r1(config-route-map)#match interface loopback 2**

**r1(config-route-map)#exit**

**r1(config)#route-map con permit 20**

**r1(config-route-map)#match interface loopback 3**

**r1(config-route-map)#exit**

**r1(config)#router bgp 100**

**r1(config-router)#address-family ipv6**

**r1(config-router-af)#redistribute connected route-map con**

**（2）在R2上查看重分布进IPv6 BGP的剩余网段**

**r2#show bgp all**

**For address family: IPv6 Unicast**

**BGP table version is 11, local router ID is 2.2.2.2**

**Status codes: s suppressed, d damped, h history, * valid, > best, i - internal,**

**r RIB-failure, S Stale**

**Origin codes: i - IGP, e - EGP, ? - incomplete**

**Network          Next Hop            Metric LocPrf Weight Path**

- **> 2022:2:2:22::/64 :: 0 32768 i**
- **>i3001:1:1:11::/64 2012:1:1:11::1 0 100 0 i**
- **>i3002:1:1:11::/64 2012:1:1:11::1 0 100 0 ?**
- **>i3003:1:1:11::/64 2012:1:1:11::1 0 100 0 ?**

**r2#**

**说明：可以看到，R1上的剩余网段成功被重分布进BGP。**

**6.过滤IPv6路由**

**说明：在R2上过滤掉IPv6路由，只留想要的网段，使用distribute-list对指定邻居进行过滤**

**（1）配置只留3002:1:1:11::/64网段**

**r2(config)#ipv6 prefix-list abc permit 3002:1:1:11::/64**

**r2(config)#router bgp 100**

**r2(config-router)#address-family ipv6**

**r2(config-router-af)#neighbor 2012:1:1:11::1 prefix-list abc in**

**（2）查看过滤后的路由表情况**

**r2#clear bgp ipv6 unicast ***

**r2#sh bgp all**

**For address family: IPv6 Unicast**

**BGP table version is 3, local router ID is 2.2.2.2**

**Status codes: s suppressed, d damped, h history, * valid, > best, i - internal,**

**r RIB-failure, S Stale**

**Origin codes: i - IGP, e - EGP, ? - incomplete**

**Network          Next Hop            Metric LocPrf Weight Path**

- **> 2022:2:2:22::/64 :: 0 32768 i**
- **>i3002:1:1:11::/64 2012:1:1:11::1 0 100 0 ?**

**r2#**

**说明：路由表中只剩想要的网段，说明过滤成功。**

**7.使用链路本地地址建立IPv6 BGP邻居**

**说明：正常情况下，IPv6 BGP使用全局地址建立邻居，也可以配置使用链路本地地址建立邻居。**

**（1）在R1上配置IPv6 BGP用链路本地地址建立邻居**

**r1(config)#router bgp 100**

**r1(config-router)#neighbor FE80::C200:DFF:FEC8:0 remote-as 100**

**r1(config-router)#neighbor FE80::C200:DFF:FEC8:0 update-source f0/0**

**r1(config-router)#address-family ipv6**

**r1(config-router-af)#neighbor FE80::C200:DFF:FEC8:0 activate**

**r1(config-router-af)#**

**（2）在R2上配置IPv6 BGP用链路本地地址建立邻居**

**r2(config)#router bgp 100**

**r2(config-router)#neighbor FE80::C200:8FF:FE10:0 remote-as 100**

**r2(config-router)#neighbor FE80::C200:8FF:FE10:0 update-source f0/0**

**r2(config-router)#address-family ipv6**

**r2(config-router-af)#neighbor FE80::C200:8FF:FE10:0 activate**

**r2(config-router-af)#**

**（3）查看邻居建立情况**

**r1#show bgp sum**

**BGP router identifier 1.1.1.1, local AS number 100**

**BGP table version is 1, main routing table version 1**

**Neighbor        V    AS MsgRcvd MsgSent   TblVer  InQ OutQ Up/Down  State/PfxRcd**

**FE80::C200:DFF:FEC8:0**

**4   100       6       7        1    0    0 00:01:30        0**

**r1#**

**r2#show bgp sum**

**BGP router identifier 2.2.2.2, local AS number 100**

**BGP table version is 1, main routing table version 1**

**Neighbor        V    AS MsgRcvd MsgSent   TblVer  InQ OutQ Up/Down  State/PfxRcd**

**FE80::C200:8FF:FE10:0**

**4   100       8       7        1    0    0 00:02:20        0**

**r2#**

**说明：从结果中看出，双方IPv6 BGP已成功使用链路本地地址建立邻居**

**（4）查看路由学习情况**

**r1#sh bgp all**

**For address family: IPv6 Unicast**

**BGP table version is 14, local router ID is 1.1.1.1**

**Status codes: s suppressed, d damped, h history, * valid, > best, i - internal,**

**r RIB-failure, S Stale**

**Origin codes: i - IGP, e - EGP, ? - incomplete**

**Network          Next Hop            Metric LocPrf Weight Path**

- **>i2022:2:2:22::/64 FE80::C200:DFF:FEC8:0**

**0    100      0 i**

- **> 3001:1:1:11::/64 :: 0 32768 i**
- **> 3002:1:1:11::/64 :: 0 32768 ?**
- **> 3003:1:1:11::/64 :: 0 32768 ?**

**r1#**

**r2#show bgp all**

**For address family: IPv6 Unicast**

**BGP table version is 6, local router ID is 2.2.2.2**

**Status codes: s suppressed, d damped, h history, * valid, > best, i - internal,**

**r RIB-failure, S Stale**

**Origin codes: i - IGP, e - EGP, ? - incomplete**

**Network          Next Hop            Metric LocPrf Weight Path**

- **> 2022:2:2:22::/64 :: 0 32768 i**
- **>i3001:1:1:11::/64 FE80::C200:8FF:FE10:0**

**0    100      0 i**

- **>i3002:1:1:11::/64 FE80::C200:8FF:FE10:0**

**0    100      0 ?**

- **>i3003:1:1:11::/64 FE80::C200:8FF:FE10:0**

**0    100      0 ?**

**r2#**

**说明：从结果中看出，双方IPv6 BGP已成功学习到相互的IPv6路由条目。**