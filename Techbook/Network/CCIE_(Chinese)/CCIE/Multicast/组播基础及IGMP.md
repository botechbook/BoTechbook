# 组播基础及IGMP

组播基础及IGMP

2011年6月27日

17:28

**组播：Multicast**

**单播：一对一**

**组播：一对部分**

**广播：一对所有**

[通信CCIE复习：介绍IP组播.pdf](组播基础及IGMP/通信CCIE复习：介绍IP组播.pdf)

**关于组播的基础**

**1.组播使用D类IP地址表示，即224到239**

**2.组播没有子网掩码**

**3.组播基于UDP**

**注意：224.0.0.0-224.0.0.255这段范围的地址其TTL值为1，也就是说只能传播“一跳”路由器，但路由器收到该段范围的目的地址的包时会向所有接口都拷贝一份数据包发送出去。**

**使用组播地址更新的IGP（RIPv2、EIGRP、OSPF）意义在于：**

**凡是开启了相应IGP进程的接口就会侦听相应的组播IP地址和组播MAC地址，组播数据在数据链路层就可以判断出是否是自己要接收的数据，而广播数据则必须到达网络层才能判断出是否需要丢弃。（广播MAC地址是全F）所以IGP协议使用组播地址传输消息，不是为了节省链路上的流量，而是为了节省无关设备的CPU资源。**

交换机在转发组播数据时是根据组播地址表来进行的。由于组播数据不能跨越VLAN传输，因此组播地址表的第一部分是VLAN ID，当交换机收到组播数据包时，数据包只能在接收端口所在的VLAN内转发。组播地址表对应的出口端口不是一个，而是一组端口列表。转发数据时，交换机根据组播数据的目的组播地址查找组播地址表，如果在组播地址表中查不到相应的条目，则把该组播数据广播，即向接收端口所在VLAN内的所有端口上转发；如果能查找到对应的条目，则目的地址应该是一组端口列表，于是交换机把这个组播数据复制成多份，每份转发到一个端口，从而完成组播数据的交换。

**注意：交换机组播地址表不是靠“学习”完成的，是靠IGMP Snooping截取IGMP消息创建而成的。**

**Show mac-address-table multicast //查看组播地址表**

**关于组播地址**

**组播地址的范围是224.0.0.0到239.255.255.255**

**关于组播中的本地地址**

**其中224.0.0.0到224.0.0.255是本地地址**

**也就是说范围是本地链路，所以TTL被设置成1**

**几个特别的本地组播地址如下：**

**224.0.0.1：所有主机**

**224.0.0.2：所有组播路由器**

**224.0.0.4：所有DVMRP路由器**

**224.0.0.5：所有OSPF路由器**

**224.0.0.6：所有OSPF的DR与BDR**

**224.0.0.9：所有RIPv2路由器**

**224.0.0.10：所有EIGRP路由器**

**关于组播的全局地址**

**范围是224.0.1.0到238.255.255.255**

**在整个Internet中动态的进行分配**

**其中224.2.0.0/16用于Mbone（Multicast Backbone）**

**Mbone最初是由Internet工程任务组（IETF）开发的，旨在支持音频和视频会议**

**关于组播的管理地址**

**管理地址是指在有限范围内有效地地址，被保留给私有域使用**

**范围是239.0.0.0到239.255.255.255**

**关于第2层组播地址**

**在以太网中，对于单播地址如果想获取第2层地址，使用ARP协议**

**而对于组播，不需要进行ARP，有一种算法来实现从组播IP地址到组播MAC地址的映射**

**这种算法是：**

**0x0100.5e + 组播IP地址的后23位 = 组播MAC地址**

**也就是说组播的MAC地址前25位已经是定的了，就是0x0100.5e**

**因此，组播地址的范围是0100.5e00.0000到0100.5e7f.ffff**

**从上面的算法可以看出，一个组播IP地址可以推导出一个组播**

**MAC地址**

**思考：一个组播MAC地址可以推出一个组播IP地址吗？**

**答案是一个组播MAC地址可以对应32个组播IP地址**

**例子：**

**将下面的组播IP地址推导出组播MAC地址**

**1.224.1.1.1**

**2.239.5.5.5**

**将下面的组播MAC地址推导出组播IP地址**

**01-00-5e-0a-00-01**

**解法：**

**组播IP地址的后23位为：0001010.00000000.00000001**

**组播IP地址的前4为是：1110**

**组播IP地址为：1110+xxxxx+0001010.00000000.00000001**

**所以：32个组播IP地址对应一个组播MAC地址**

**关于客户端如何获取会话**

**组播的客户端获悉会话的方法有：**

**1.客户端的应用程序预先已经加入到了某个著名的预定义组，组播的服务器端向该组播组发送组播应用**

**2.应用可能是从网页中启动的，说白了就是先上哪个网站，然后点击一下某个链接触发组播的会话**

**3.用户通过点击E-mail来获悉会话**

**4.客户端上安装了客户应用程序，此应用程序让用户知道哪些内容可以用，客户应用程序使用SDP（Session Description Protocol，会话描述协议）和SAP（Session Announcement Protocol，会话通告协议）来获悉内容。在Cisco文档中，SDP/SAP指的就是SDR，可以把他们理解成同义词**

**关于组播中用到的协议**

**组播中用到的协议有三种类型**

**一种是主机与路由器之间的：IGMP**

**一种是交换机与路由器之间的：CGMP，IGMP snooping**

**一种是路由器与路由器之间的：PIM，DVMRP，MOSPF，CBT**

**关于IGMP**

**IGMP：Internet Group Management Protocol，英特网组管理协议**

**IGMP是路由器和主机之间的协议**

**IGMP分为三个版本：IGMPv1，IGMPv2，IGMPv3**

**关于IGMPv1**

**IGMPv1在RFC1112中定义的**

**IGMPv1中使用到2种消息：**

**1.Membership Query（主机成员查询）：路由器发送的，每60-120秒发送一次，目标地址224.0.0.1**

**2.Membership Report（主机成员报告）：主机发送的，两种情况下发送，第一种是主机第一次加入某个组，第二种是相应路由器的Membership Query查询的时候，目标地址是要加入的组**

**关于IGMPv2**

**IGMPv2在RFC2236中定义的**

**IGMPv2中使用5种消息：**

**1.General Query：路由器发送，默认情况下60秒发送一次，目标地址224.0.0.1，这个消息中包含一个字段叫做Max Response Time，默认此字段的值是10.**

**2.Group-Specific Query(特定组查询消息)：路由器发送，当收到Leave Group message的时候发送，它的目标地址是Leave Group消息中的地址，group-specific query时间间隔：1s，RFC2236建议发送多条查询消息，但Cisco的IGMPv2仅发送一条**

**3.Membership Report messages：主机发送，两种情况发送，第一种是主机第一次加入某个组，第二种是相应路由器的Membership Query查询的时候**

**4.Version 1 Membership Report messages：主机发送，为了保持与IGMPv1的前向兼容性**

**5.Leave Group messages：主机发送，当主机想离开的时候发送，目标地址224.0.0.2**

**注意点：**

**1.什么是Max Response Time（最大响应时间）？主要是用来防止不必要的包的传输，当Query消息发送出来以后，每个机子都启用一个0到Max Response Time之间的计时器，然后有一个机子回复，其他机子就不用回复了。//意思是某个主机的计时器先超时了就回复给路由器，同时其他主机也能收到该主机的回复，所以其他主机不用回复。**

**2.general query时间间隔：每60s发送一次general query消息，称为查询间隔。**

**Cisco设备在3倍查询时间内（默认为3分钟）无法收到report消息，认为该子网内已经没有组成员了，但是RFC2236规定：这个时间为2倍查询间隔加上1个最大响应时间。**

**RFC2236文档节选**

**When a router receives a Report, it adds the group being reported to the list of multicast group memberships on the network on which it received the Report and sets the timer for the membership to the[Group Membership Interval]. Repeated Reports refresh the timer. If no Reports are received for a particular group before this timer has expired, the router assumes that the group has no local members and that it need not forward remotely-originated multicasts for that group onto the attached network.**

- **------------------------------------------------------------- The Group Membership Interval is the amount of time that must pass before a multicast router decides there are no more members of a group on a network. This value MUST be ((the Robustness Variable) times (the Query Interval)) plus (one Query Response Interval).**

**3.思科的路由器启动的时候会发送一个General Query消息**

**关于IGMPv1和IGMPv2之间的不同点：**

**1.IGMPv1没有Leave Group Message，IGMPv2有**

**2.IGMPv1没有Group-Specific Query，IGMPv2有**

**3.IGMPv1的Max Response Time是不可以调的，一定是10秒，而在IGMPv2中，Max Response Time字段封装进了Query包中，所以可以改变**

**4.IGMPv1的Query消息是60-120秒之间，而IGMPv2的Query消息是60秒一次**

**5.IGMPv1没有查询者选举（Querier election）机制，需要路由协议的帮忙，而IGMPv2有查询者选举机制**

**IGMPv1的机制**：

**IGMPv1 join group－report**

使用的report包的IP目的地址为特定的组播地址，比如要加入组224.1.1.1，目的地址就是224.1.1.1。这是因为report包的一个功能是**需要抑制其他接收者的report包**，需要其他的接收者收到。这时叶路由器和特定组的接收者都能收到这个report包。

**IGMPv1 通用组查询**

在v1里面的query包叫做通用组查询，其IP的目的地址为224.0.0.1,让链路上的所有接收者都收到这个查询包。默认每60秒周期性发送查询，询问链路上有没有需要加入组的接收者。

(if)#ip igmp query-interval 30 修改接口发送查询的时间间隔

如果是一个LAN网络，需要选择出一个**DR作为查询者发送query** ，**IGMPv1没有一个查询者选择机制，只能依靠上层协议PIM选出一个DR**，选择规则：**首先选举优先级，默认优先级为1，若优先级一样选择IP接口地址大的。这里和OSPF不同，当优先级为0时并不代表不能参与选举。**

(if)#ip pim dr-priority 100 修改接口下pim dr优先级

**IGMPv1 report抑制机制**

如果一个LAN的链路，一个组中有多个接收者，只会有1个接收者来发送report，而其他的会被抑制。**当所有的接收者收到query包后，接收者会随机产生一个(0－10)秒的倒计时数**，由于是随机的倒计时数，每个接收者倒计时到0的时候可能会不同。只要哪台接收者首先倒计时到0就开始发送report，之后其他的接收者接收到这个report包后将计时器设置为-1停止倒计时，自己的report包被抑制。

**IGMPv1的离组**

Ipmpv1没有一种离组消息，而是一种静静的离开方式。当一台接收者要离开一个组时不会发送离组消息给叶路由器，这时叶路由器依然会发送该组的组播流量给接收者，默认每60秒发送一次查询，hold时间为180秒，这样就需要最多等待3分钟才能将这个接收者从组成员中删除。

**IGMPv2的机制**：

IGMPv2有自己的**查询者选择机制**，这里的选择机制是**比较发送query包的接口IP地址的大小，选择小的**。这里和DR的选择机制相反。非查询者也能收到查询者的query包，当2倍的时间内（即120秒）没有收到查询者发出的query包，就会马上发出自己的query信息。查看查询者命令：show ip igmp interface fa 1/0

> (if)#ip igmp querier-timeout 120 修改查询者定时器，默认查询时间2倍的查询间隔即120s
> 

IGMPv2中发送report的抑制机制产生的倒计时时间可以修改，可以设置最大的响应时间，单位不是秒了。**以0.1秒做为单位**。这样粒度增大了，冲突的可能性缩小。**因为如果象v1那样随机产生0－10秒的倒计时器，**很有可能两个叶路由器的时间碰到一样。

> V2是在0－100之间选择一个数字来倒计时，这样粒度更大，选择的范围更广，冲突的可能性减小，其实时间还是0－10秒。
> 

**兼容IGMPv1**。

**关于IGMPv3**

**IGMPv3还在发展之中，所以不必太关注，现在的主流还是IGMPv2**

**IGMPv3对IGMPv2的最大改进之处就是针对特定源的选择机制，主机可以决定那些源发送的组播流可以接收，哪些源发送的组播流不可以接收**

**组播在交换机中产生的问题？**

**交换机的工作原理：**

**1.组播、广播、未知单播，泛洪**

**2.依据MAC地址转发 //三层交换机的转发原理**

**3.记录源MAC，填充CAM表 //MAC表的形成**

**根据第一条，所以产生问题。。。。 //优点，缺点**

**解决方法**

**1、手工配置 // 视频会议**

**2、GMRP(多播注册协议)**

**GMRP是IEEE 802.1p标准中定义的开放式协议，可以在交换机中动态注册/撤销MAC层多播地址。利用命令set gmrp enable即可在交换机上启用GRMP，而无需在路由器上做其他配置。如IEEE 802.1p标准所建议的那样，GMRP是一种严格的二层协议。**

**3.IGMP Snooping**

**现在解决二层组播泛洪问题的一个标准就是IGMP snooping，使用的最多。**

**运行在交换机上。**

**交换机查看IGMP的report和leave消息，监控协议包。**

**使用什么监控：1、NMP（CPU）**

**2、专用集成电路（ASICs）**

**这时有个问题，如果每次CPU都读取组播数据包，如果组播数据包过多，CPU将会负载过重，IGMP snooping采用ASICs硬件执行IGMP snooping。**

**命令：(config)#ip igmp snooping 开启所有vlan的snooping功能**

**(config)#ip igmp snooping vlan 10 单独开启某个vlan的snooping功能**

**Show ip igmp snooping mroute**

**Show mac-address-table multicast**

**使用igmp snooping后当路由器收到离组消息代表这个链路上肯定没有其他组成员了，所以路由器没有必要在发送特定组查询（因为启用了IGMP snooping功能的交换机已经替路由器接收leave消息，并且确认了确实没有组成员才会给路由器发送leave消息，所以说当路由器收到leave消息时能够确认确实下面没有组成员了，也就可以禁用特定组查询消息了），可使用这个命令来禁止发送特定组查询：**

**interface FastEthernet1/0**

**ip igmp immediate-leave group-list 1 一旦收到group-list 1匹配的组的离组消息，就不会发送特定组查询，马上prune流量。**

**access-list 1 permit 224.1.1.1 使用访问列表匹配组地址**

IGMP Snooping和IGMP协议一样，两者都用于组播组的管理和控制，它们都使用IGMP报文。IGMP协议运行在网络层，而IGMP Snooping则运行在链路层，通过report消息，主机能够加入组。交换机监听到IGMP消息，并将发送IGMP report消息的主机接口加入到相关的2层转发表中。IGMP仅将每个组播组的第一个主机的report消息转发给组播路由器，并将抑制组播组的其他后续report消息。交换机从report消息所指定组的组播路由器中接收组播流量，并且将把这些组播流量转发给接收到加入消息的接口。

交换机收到主机发送的IGMPv2指定组leave消息后，用基于MAC的指定组查询进行响应，以确定该VLAN中是否还有其他设备想接收发送给该组播组的通信流。如果交换机没有收到响应query消息的IGMP report消息，将删除该主机的组播条目。如果leave消息来自组播组中惟一的一台主机，直接删除该条目，并将该leave消息转发给组播路由器。

当二层以太网交换机收到主机和路由器之间传递的IGMP报文时，IGMP Snooping分析IGMP报文所带的信息，在二层建立和维护CAM表，以后从路由器下发的组播报文就根据CAM表进行转发。IGMP Snooping只有在收到某一端口的IGMP离开报文或者某一端口的老化时间定时器超时的时候才会主动向端口发IGMP特定组查询报文，除此之外，它不会向端口发任何IGMP报文

**4.CGMP**

**CGMP是路由器和交换机之间的协议**

**关于CGMP**

**CGMP：Cisco Group Membership Protocol，思科组管理协议，不用三层也行，让上面的路由器去做吧**

**CGMP使用2中包：**

**1.Join包：路由器发送给交换机，目标MAC地址0100.0cdd.dddd**

**2.Leave包：路由器发送给交换机，目标MAC地址0100.0cdd.dddd**

**CGMP报文中有两个重要的字段：GDA（Group Destination Address，组目的地址）**

**USA（Unicast Source Address，单播源地址，对此组播流感兴趣的主机MAC）**

**使交换机能从路由器和三层交换机哪里获得组播组的存在。**

**CGMP基于C/S模型，路由器为S，交换机为C。基本原理是：组播路由器能看到所有IGMP数据包，所以当主机加入或脱离组播组时，它能够将此信息告诉交换机，交换机再据此建立MAC地址表。**

**主机通过发送report消息加入组播组，组播路由器收到该消息后，记录其源MAC地址，并发送一个CGMP join消息给交换机，交换机根据该CGMP消息在交换表中动态创建一个条目，将组播流映射到客户连接的交换机端口。**

**CGMP只有一些老的IOS支持，新的IOS已经不支持CGMP了。**

**CGMP的包永远是路由器发给交换机的，交换机识别CGMP包，监控0100.0cdd.dddd，这个地址是cisco私有的组播地址。CGMP包可变长，最小16个字节。GDA：组的目的MAC地址，6字节。USA：单播源MAC地址，6字节。**

**相对于CGMP，IGMP Snooping拥有更多优点：即使没有路由器也能运行，还能采用硬件执行，所费CPU更少。**

**命令：(config)#cgmp 在交换机上配置**

**(if)#ip cgmp 在路由器上配置**

**口诀：路由器命令交换机**

**关于路由协议**

**路由协议分为单播路由协议和组播路由协议**

**1.单播路由协议分为内部网关路由协议和外部网关路由协议**

**内部网关路由协议分为：RIP，OSPF，IS-IS等**

**外部网关路由协议分为：EGP，BGP**

**2.组播路由协议分为域内组播路由协议和域间组播路由协议**

**域内组播路由协议分为：DVMRP，MOSPF，CBT，PIM**

**域间组播路由协议分为：MBGP，MSDP，SSM**