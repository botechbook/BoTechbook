# GLBP介绍及配置

GLBP介绍及配置

2011年6月29日

16:53

GLBP介绍及配置

1）GLBP介绍

全称Gateway Load Banancing Protocol，

和HRSP、VRRP不同的是，GLBP不仅提供冗余网关，还在各网关之间提供负载均衡，

而HRSP、VRRP都必须选定一个活动路由器，而备用路由器则处于闲置状态。

和HRSP不同的是，GLBP可以绑定多个MAC地址到虚拟IP，

从而允许客户端选择不同的路由器作为其默认网关，而网关地址仍使用相同的虚拟IP，

从而实现一定的冗余。

什么是GLBP？

GLBP全称Gateway Load Banancing Protocol，是思科的专有协议。GLBP可以绑定最多4个MAC地址到一个虚拟IP，允许客户端使用相同的虚拟IP作为网关地址。客户端发出ARP请求后，回应到不同的目标MAC地址，从而经由不同的路由器转发数据包，因此在一定程度上起到了负载均衡的作用。这与HRSP、VRRP是有区别的。HRSP、VRRP都必须选定一个活动路由器，由活动路由器代表虚拟路由器地址转发数据包，备用路由器则处于闲置状态。而GLBP在提供虚拟路由器的同时，GLBP组中的所有路由器都能够转发部分数据流，参与负载均衡，可见GLBP可充分利用网络资源，同时无需过多配置与管理。

活动虚拟网关选举

活动虚拟网关的选举采用类似于HRSP的选举机制选举活动网关，优先级最高的路由器成为活动路由器，如果优先级相同，则IP地址最高的路由器成为活动路由器。活动路由器被称做AVG（Acitve Virtual Gateway），其他非AVG则提供冗余，如果AVG失效，新的选举就会发生。非AVG也被称做活动虚拟转发器AVF（Active Virtual Forwarder）。AVG与AVF共同组成GLBP的组成员，每个GLBP组最多可以有4个成员。

虚拟MAC地址分配

GLBP自动管理虚拟MAC地址的分配。如果某路由器被推举为AVG后， AVG开始按序分配虚拟MAC地址给AVF。AVF分为两类: PVF（Primary Virtual Forwarder）和SVF（Secondary Virtual Forwarder）。直接由AVG分配虚拟MAC地址的路由器被称做PVF；后续不知道AVG真实IP地址的组成员，只能使用hellos包来识别其身份，然后被分配虚拟MAC地址，此类被称做SVF。PVF的虚拟MAC是由一段固定的MAC前缀+组号组成的。GLBP最多有4台路由器作为IP默认网关，每个网关的虚拟MAC地址依次为PVF的地址号加1。譬如PVF的虚拟MAC地址为0007.b400.0a01，则第一个SVF就是0007.b400.0a02，依此类推。分配了虚拟MAC地址后，所有的GLBP组成员都参与转发数据包，但是各成员只负责转发分给自己的虚拟MAC地址相关的数据包。

2）活动网关选举

使用类似于HRSP的机制选举活动网关，

优先级最高的路由器成为活动落由器，称作Acitve Virtual Gateway，其他非AVG提供冗余。

某路由器被推举为AVG后，和HRSP不同的工作开始了，AVG分配虚拟的MAC地址给其他GLBP组成员。

所有的GLBP组中的路由器都转发包，

但是各路由器只负责转发与自己的虚拟MAC地址的相关的数据包。

GLBP组成员交互HEELO信息，时间间隔为3S，组播地址为224.0.0.102，使用UDP3222端口。

GLBP

1.思科私有的

2.一个虚拟IP地址，多个虚拟MAC地址

3.GLBP和HSRP，VRRP的最大不同在于：可以提供负载均衡

4.两个术语：

（1）AVF：active virtual forwarder

（2）AVG：active virtual gateway

5.GLBP的工作原理：

（1）GLBP组选举一个AVG

（2）AVG给整个组分配虚拟MAC地址，即一个AVF分配到一个

（3）AVG负责回复用户的ARP请求，每次给的虚拟MAC地址不同，以这种方式实现负载均衡

（4）每个AVF负责转发自己负责的那个虚拟MAC的数据

6.GLBP支持3种负载均衡的模式

1 round-robin:在所有AVF间轮询，同一用户在不同的时间里可能由不同AVF服务。

2 weighted：根据weight大小决定负载的多少，大的，就会多些机会负载，同一用户同一应用程序处理过程。

3 host-dependent：基于源MAC选择的负载(用户请求到某一个AVF后，一直由这个AVF为其服务)。

（1）host-dependent：确保主机始终使用同一个虚拟MAC地址

（2）round-robin：每次轮流地分配AVF的虚拟MAC地址

（3）weighted：前往AVF的流量取决于AVF的权重

默认的负载均衡是round-robin：主机在AVF（活跃虚拟转发器）间轮循，有点类似基于主机的负载均衡。但是如果PC的arp表超时或删除后，会重新获取新的虚拟mac，和之前获取的不一定一样。

GLBP: 让局域网更均衡

使用GLBP协议，在不改变网络结构的前提下，无需更多的配置，即可实现关键应用的负载均衡以及路由的冗余备份，最大限度保护了用户的投资，能够用最少的管理费用大大提升网络性能。

GLBP配置验证

在GLBP组成员的指定端口上分别配置相关GLBP命令，并为不同成员配置不同的优先级。优先级高的路由器则成为活动路由器，其状态值为active，其余路由器成为备份路由器，状态值为standby。活动路由器自动分配虚拟MAC地址给所有组成员，这样，每个组成员会得到所有成员的虚拟MAC地址，但每个路由器下虚拟MAC地址的状态各不相同。状态值为active表示此MAC地址为该路由器的活动MAC地址，负责转发相关数据包; 状态值为listen表示此MAC地址处于监听状态，一旦监听到其他路由器出现故障不能转发，则自动将listen状态变为active，同时接管该MAC地址的数据转发功能，实现冗余。正常情况下，每个组成员只负责转发MAC地址状态值为Active的相关数据包。

**用GLBP实现负载均衡**

GLBP将多台交换机或者路由器分配到同一个GLBP组中。GLBP自动管理并由选举出来的AVG来分配不同的虚拟的MAC地址给组成员，每个GLBP组中最多能够拥有4个虚拟MAC地址。当客户端发送查询虚拟网关地址的ARP请求时，AVG应答所有有关虚拟网关地址的ARP请求，依据负载均衡算法决定返回哪一个MAC地址给客户端，因此客户端得到的MAC地址是不尽相同的。GLBP正是通过使用ARP应答中不同的虚拟MAC地址，来实现网络的负载均衡。

这种做法有两个优点: 第一，客户端无需分别指向冗余路由的物理MAC地址，所有客户端的默认网关均指向惟一的虚拟路由器IP地址，即可通过不同的冗余路由，真正实现负载均衡; 第二，即使某一台路由器出现故障，GLBP组中其他路由器可以马上接管故障路由器的虚拟MAC地址，从而不会影响客户端数据的传输。

GLBP命令解释：

Router(config)#track 100 interface f1/0 //配置跟踪目标100，检查跟踪接口状态，up或是down，当状态为down时weighting值减去相应设置值，weighting值默认为100

interface f0/0

glbp 1 ip 211.1.100.254 //配置glbp虚拟路由IP地址

glbp 1 priority 110 //配置优先级，默认100

glbp 1 preempt //配置抢占功能

glbp 1 load-balancing [host-dependent|round-robin| weighted] //更改

glbp 1 weighting 100 //配置权重值，默认为100

glbp 1 weighting 100 lower 100 //当glbp组成员权重值小于最小门槛值（默认最小门槛值为1），放弃AVF角色

glbp 1 weighting track 100 decrement 100 //配置被跟踪接口出故障时的惩罚值,惩罚的权重值，所以如果本台设备某接口出问题了并且被track了，要想让其放弃转发数据的责任，必须改为权重模式，然后设置权重门槛，让其放弃。所以这里面的priority值仅仅是为了选择AVG的，如果连接主机这边的接口不出故障就不会重新选举AVG。

glbp 1 timers //调整发送hello包的时间间隔和有效时间，默认为3和10s

glbp 1 forwarder preempt delay minimum 2 //调整转发者抢占延时为2s，默认为30s

glbp 1 authenticaiton md5 key-string cisco //配置glbp验证key为cisco

Show glbp

<<GLBP.jpg>>

<<GLBP实验.net>>

写在实验后面：

GLBP的作用有别于HSRP VRRP，是网关的负载均衡，既做到了网关的冗余备份，也完成了对传统冗余设备中备份设备的利用，利用轮询负载的特性使组内每一台网关都能得到充分的利用，并且在发生故障时能够得到更快的备份。