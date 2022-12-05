# Introducing Classification and Marking

Introducing Classification and Marking

2011年7月7日

15:34

**分类的方式：**

**1.CoS**

**2.IP Precedence(IP 优先级)**

**3.DSCP（区分服务代码点）**

**4.input-interface（入接口）**

**5.源，目地址（使用ACL来匹配流量）**

**6.Application（特指NBAR）**

**CoS服务OSI模型中服务类型,高层协议用来指出低层协议应如何处理消息的标识.在系统网络架构(SNA)子区域路由选择中,CoS被子区域节点用来确定建立会话的最优路由.CoS由虚拟路由号和传输优先字段组成,也称为ToS.**

**DSCP差分服务代码点（Differentiated Services Code Point）,IETF于1998年12月发布了Diff-Serv（Differentiated Service）的QoS分类标准. 它在每个数据包IP头部的服务类别TOS标识字节中，利用已使用的6比特和未使用的2比特字节，通过编码值来区分优先级.**

**标记的方式**

**在链路层的标记方式有**

**CoS（ISL，802.1q）**

**MPLS EXP 位**

**Frame Relay中的DE位**

**网络层的标记方式有：**

**DSCP**

**IP precedence**

**关于CoS**

**以太网封装trunk的时候有ISL和802.1q两种方式，这两种方式的帧中都会有CoS的字段，如下图：**

![Introducing%20Classification%20and%20Marking%204a211e8e19d647019ccb5c1b1338e889/image1.png](Introducing%20Classification%20and%20Marking/image1.png)

**其中PRI=CoS=802.1p，PRI就是传说中的CoS，是在802.1p中定义的。TPID=0x8100**

**CoS占有3个比特，所以最多支持8种类型。**

![Introducing%20Classification%20and%20Marking%204a211e8e19d647019ccb5c1b1338e889/image2.png](Introducing%20Classification%20and%20Marking/image2.png)

**默认Cos是0**

**802.1p推荐对于不同的应用程序按上面的方式打，但是可以不这样使用。**

**关于MPLS中的EXP**

![Introducing%20Classification%20and%20Marking%204a211e8e19d647019ccb5c1b1338e889/image3.png](Introducing%20Classification%20and%20Marking/image3.png)

**MPLS中的EXP字段使用来做CoS的**

![Introducing%20Classification%20and%20Marking%204a211e8e19d647019ccb5c1b1338e889/image4.png](Introducing%20Classification%20and%20Marking/image4.png)

**MPLS中的EXP也是推荐按上图打标记。**

**补充一下：上图中的Frame Header字段不是指的只有以太网，而是除了ATM以外的所有的网络类型。MPLS分为两种模式，一个是帧模式，一个是信元模式。信元模式是指在ATM中的，而帧模式MPLS是指除ATM以外的所有网络。**

**关于帧中继**

![Introducing%20Classification%20and%20Marking%204a211e8e19d647019ccb5c1b1338e889/image5.png](Introducing%20Classification%20and%20Marking/image5.png)

**帧中继的头部中有个DE位，是用来做QoS的。**

**关于DLCI的范围：0-1023，其中0是ansi和q933a用的，1023是cisco用的，16-1007是可以使用的范围**

**关于IP Precedence和DSCP(Differentiated services codepoint,区分服务代码点)**

![Introducing%20Classification%20and%20Marking%204a211e8e19d647019ccb5c1b1338e889/image6.png](Introducing%20Classification%20and%20Marking/image6.png)

**IPv4包头中的ToS（Type of Service）字段有8个bit，上图就是前6个bit。**

**IP Precedence是在RFC 1812中定义的，占用前3个bit。**

**0 routine（常规）**

**1 priority（优先）**

**2 immediate（紧要）**

**3 flash（快速）**

**4 flash-override（最快速）**

**5 critical（关键）**

**6 internet（网络互联）**

**7 network（网络）**

**而DSCP占用前6个bit。余下的两bit用于流控制，成为ECN（Explicit Congestion Notification,显式拥塞指示）**

**DSCP提出了一个PHB（每一跳行为）的概念。其实说白了用AF，EF等关键字表示DSCP就叫做PHB。**

**交换机或路由器根据报文所携带的类别信息，可以为各种交通流提供不同的传输优先级，或者为某种交通流预留带宽，或者适当的丢弃一些重要性较低的报文、或者采取其他一些操作等等。这些独立设备的这种行为在DiffServ 体系中被称作每跳行为（per-hop behavior）。如果网络上的所有设备提供了一致的每跳行为，那么对于DiffServ 体系来说，这个网络就可以构成end-to-end QoS solution。**

![Introducing%20Classification%20and%20Marking%204a211e8e19d647019ccb5c1b1338e889/image7.png](Introducing%20Classification%20and%20Marking/image7.png)

**PHB分为4种：**

**Default PHB（FIFO，tail drop）：前3位是十进制0，后3位也是0**

**AF PHB：前3位是十进制从1到4**

**EF PHB：前3位是十进制5，二进制是101 110，十进制46**

**Class-selector PHB(IP precedence)：后3位是零，用来保持与IP precedence的前向兼容性。**

**关于EF**

![Introducing%20Classification%20and%20Marking%204a211e8e19d647019ccb5c1b1338e889/image8.png](Introducing%20Classification%20and%20Marking/image8.png)

**EF = 二进制101 110 = 十进制 46**

**关于AF**

![Introducing%20Classification%20and%20Marking%204a211e8e19d647019ccb5c1b1338e889/image9.png](Introducing%20Classification%20and%20Marking/image9.png)

**AF分为4个类别（AFxy）：AF1y，AF2y，AF3y，AF4y。其中在每个类别中，y表示丢弃可能性。口诀是：越高越丢弃。**

**其实说白了就是AF分为4个队列，每个队列都会有一个预定义的带宽，当某个特定队列上的流量超出了为该队列预留的带宽时，队列就会出现拥塞并发生丢包。为了避免出现尾丢弃现象，需要在每个队列上都部署WRED（Weighted Random Early Detection，加权随机早期检测）等拥塞避免技术，从而可以根据数据包上不同的标记丢弃数据包。如：在队列AF1中，AF13会比AF11在重度拥塞的情况下丢弃的可能性要高。**

**AF11 = 二进制 001010（1=001 1=01 最后一位0） = 十进制10**

**AF12 = 二进制 001100（1=001 2=10 最后一位0） = 十进制12**

**公式：AFxy = 十进制x*8+y*2**

**AF41=二进制4=100 1=01 最后一位0 （二进制100010=十进制34）**

**推荐的DSCP值**

**DSCP　 PHB　 说明**

**101110 EF　　急速转发**

**001XXX AF1 QoS介于EF和BE之间。每一种AF可以划分为三种优先级，共12种**

**010XXX AF2**

**011XXX AF3**

**100XXX AF4**

**000000 BE 尽力而为业务**

**关于二层与三层之间的映射：二层的CoS可以映射到三层的ToS中，三层的ToS也可以映射到二层的CoS中。**

**当帧/分组从第2层环境传到第3层环境时，isl和802.1q头部被丢弃。为了保持端对端的qos，就有第2层cos值映射到第3层tos值能力的需要。当帧/分组从路由的网络返回到交换网络时，isl或802.1q的头部将再次使用携带第2层qos标记。当网络中包含不具备第3层能力的第2层设备时，这点尤为重要，因为他们可能理解cos标记，但不理解tos标记。而且，为保持端对端qos，必须利用第3层标记在这些下行分组中标记第2层的cos值。**

**称DSCP与CoS、IP优先级之间的对应关系为DSCP映射（DSCP map）。在交换机中，这些值之间存在着一种默认的对应关系，并且使用命令可以更改它们的对应关系。**

**默认的CoS-to-DSCP映射／对应关系如下。**

**Cos-dscp map:**

**cos: 0 1 2 3 4 5 6 7**

- **---------------------------------------------------**

**dscp: 0 8 16 24 32 40 48 56**

**在交换机上修改这种映射关系的命令如下。**

**Switch(config)# mls qos map cos-dscp dscp1 dscp2dscp3 dscp4 dscp5 dscp6 dscp7 dscp8**

**例：把CoS0～CoS7分别对应于DSCP 10,15,20,25,30,35,40,45。**

**Switch(config)# mls qos map cos-dscp 10 15 20 25 30 35 40 45**

**Switch# show mls qos maps cos-dscp**

**Cos-dscp map: cos: 0 1 2 3 4 5 6 7 -----------------------------------------------------**

**dscp: 10 15 20 25 30 35 40 45**

**默认的DSCP-to-CoS 映射关系**

**DSCP CoS**

**0～7 0**

**8～15 1**

**16～23 2**

**24～31 3**

**32～ 39 4**

**40～47 5**

**48～55 6**

**56～63 7**

**使用命令查看其映射关系，显示如下：**

**Switch# show mls qos maps dscp-cos**

**Dscp-cos map:**

**d1 : d2 0 1 2 3 4 5 6 7 8 9 ------------------------------------------------------------------**

**0 : 00 00 00 00 00 00 00 00 01 01**

**1 : 01 01 01 01 01 01 02 02 02 02**

**2 : 02 02 02 02 03 03 03 03 03 03**

**3 : 03 03 04 04 04 04 04 04 04 04**

**4 : 05 05 05 05 05 05 05 05 06 06**

**5 : 06 06 06 06 06 06 07 07 07 07**

**6 : 07 07 07 07**

**这是个二维阵列表，d1 列代表DSCP值的十位数，d2 行代表DSCP值的个位数。在列与行交叉的位置上显示的是映射到该DSCP值上的CoS值。**

**例如，在d1列等于2，d2行等于4的交叉点上的数值为03，这表示DSCP值24映射的CoS值为03。**

**更改DSCP-to-CoS映射关系的命令如下所示。**

**switch(config)# mls qos map dscp-cos dscp1 dscp2 dscp3 dscp4 dscp5 dscp6 dscp7 dscp8 to cos dscp1 ~ dscp8--1～8个被修改的DSCP值。**

**cos : DSCP值映射的CoS值。**

**例：把DSCP值0,8,16,24,32,40,48,50映射到CoS=0。**

**Switch(config)# mls qos map dscp-cos 0 8 16 24 32 40 48 50 to 0**

**Switch# show mls qos maps dscp-cos**

**Dscp-cos map:**

**d1 : d2 0 1 2 3 4 5 6 7 8 9 ------------------------------------------------------------------**

**0 : 00 00 00 00 00 00 00 00 00 01**

**1 : 01 01 01 01 01 01 00 02 02 02**

**2 : 02 02 02 02 00 03 03 03 03 03**

**3 : 03 03 00 04 04 04 04 04 04 04**

**4 : 00 05 05 05 05 05 05 05 00 06**

**5 : 00 06 06 06 06 06 07 07 07 07**

**6 : 07 07 07 07**

**恢复到默认的命令是：**

**switch(config)# no mls qos dscp-cos**

**对网络流量进行分类的时候注意不要超过4到5个类别。**

**常见的流量类别有：**

**1. 语音应用（Voice application）：如VoIP**

**2. 关键型应用（Mission-critical application）：如SAP和Oracle**

**3. 交互型应用（interactive application）：如Telnet和SSH**

**4. 批量应用（Bulk application）：如FTP和TFTP**

**5. 尽力而为型应用（Best-effort application）：如WWW和电子邮件**

**6. 清道夫型应用（Scavenger application）：如Napster和Kazaa**

**关于信任边界：信任边界的设备用来分配流量标记。信任边界构成了QoS的前端。而信任边界之外的设备打上的标记都会被网络重置。**

**可信任边界是所有支持qos分类的交换机支持的一种分类配置的选项。交换端口和接口的可信任状态定义了如何对入口分组进行分类、标记和随后的调度。对于仅仅依靠cos值保证qos的交换机而言，被设置为不可信任的端口将任何cos值重新分类为0或一个静态配置的cos值。**

**影响信任边界的因素：**

**1、被信任设备必须在网络管理员的管理和控制之下，至少要能确信其流量标记与网络的Qos策略一致。**

**2、不同设备在检查和设置/重置不同Qos标记方面的能力和特征集是不一样。**

**一般将信任边界设置在以下网络层次：**

**1.端系统（end system）**

**2.接入层交换机**

**3.分布层交换机**

**配置信任cos：**

**接口下命令：**

**（1）mls qos trust cos**

**指定cos值（可选）**

**（2）mls qos cos 值**

**cos值：表示分配给无标记帧的cos值**

**（3） 配置无标记帧或标记帧的替换，相当于取消信任COS**

**mls qos cos override**

**override表示在mls qos cos 值命令中覆盖标记帧的cos值。**

**案例：**

switch(config)#interface f0/10

switch(config-if)#mls qos trust cos

switch#show mls qos interface f0/10

- ---------------------------------------------

fastethernet0/10

trust state: trust cos

trust mode: trust cos

cos override: dis

default cos: 0

dscp mutation map: default dscp mutation map

trust device: none

switch(config)#interface f0/10

switch(config-if)#mls qos cos 5

switch(config-if)#mls qos cos override //将取消信任cos

switch#show mls qos interface f0/10

- -------------------------------------------------

fastethernet0/10

trust state: not trusted

trust mode: not trusted

cos override: ena

default cos: 5

dscp mutation map: default dscp mutation map

trust device: none

**问题：**

**1.下面哪一项不是用来分类的？**

**A.入接口**

**B.流量路径.**

**C.IP Precedence或DSCP值**

**D.源或目地址**

**2.下面哪一项不属于数据链路层的标记？**

**A.CoS**

**B.帧中继DE**

**C.DSCP.**

**D.EXP**

**4.下面哪一项属于帧中继QoS标记域？**

**A.DE.**

**B.CLP**

**C.Cos**

**D.EXP**

**5.下面哪一项关于MPLS头和EXP字段长度的描述是正确的？**

**A.MPLS头为2字节，EXP字段为3比特**

**B.MPLS头为2字节，EXP字段为6比特**

**C.MPLS头为4字节，EXP字段为6比特**

**D.MPLS头为4字节，EXP字段为3比特.**

**6.下面哪一项的丢弃概率更大？**

**A.AF31**

**B.AF32**

**C.AF33.**

**D.上述三项具有相同的丢弃概率**

**7.下面哪一项位置未实施信任边界?**

**A.核心层交换机.**

**B.分布层交换机**

**C.接入层交换机**

**D.端系统**

**问答题：**

**1.CoS值0-7的名字和定义分别是什么？**

**IP Precedence的0-7的名字和定义分别是什么？**

**2.哪种DSCP PHB提供了与基于ToS的IP优先级的兼容性？**

**3.4个DiffServ（DSCP）PHB分别是什么？**

**案例一：**

**把来自192.168.10.0/24的出站的telnet流量的IP优先级设置为5,**

**目标为192.168.20.0/24的出站的http流量的IP优先级设置为4，**

**其他的出站流量的IP优先级设置为1**

**关键配置：**

**access-list 110 permit tcp 192.168.10.0 0.0.0.255 any eq telnet**

**access-list 120 permit tcp any 192.168.20.0 0.0.0.255 eq www**

**class-map TEL**

**match access-group 110**

**class-map HTTP**

**match access-group 120**

**policy-map PM**

**class TEL**

**set ip precedence 5**

**class HTTP**

**set ip precedence 4**

**class class-default**

**set ip precedence 1**

**int s1/1**

**service-policy output PM**