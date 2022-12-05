# STP（Spanning-Tree Protocol）

STP（Spanning-Tree Protocol）

2011年7月7日

14:26

**STP（Spanning-Tree Protocol）**

![STP%EF%BC%88Spanning-Tree%20Protocol%EF%BC%89%2050f1f3e6d8c146789c2a802c1a33abf8/image1.png](STP（Spanning-Tree%20Protocol）/image1.png)

在上图所示的网络环境中，当交换机之间连有多条链路时，将存在一定的问题，如SW1的MAC地址表中会显示接口F0/1与主机A相对应，而当数据发往SW2后，SW2的MAC地址表则记录接口F0/23与主机A相对应，当SW2再次将流量从接口F0/24发回SW1时，SW1的MAC地址表又会记录接口F0/24与主机A相对应。

因此可以看出，当交换机之间存在多条活动链路时，交换机将从不正常的接口上学习到MAC地址，导致MAC地址表的不正确与不稳定，并且还会导致重复的数据包在网络中传递，引起广播风暴，使网络不稳定。

为了防止交换机之间由于多条活动链路而导致的网络故障，必须将多余的链路置于非活动状态，即不转发用户数据包，而只留下单条链路作为网络通信，当唯一的活动链路不能工作时，再启用非活动链路，从而达到网络的冗余性。要实现此功能，需要依靠生成树协议（STP）来完成，STP将交换网络中任何两个点之间的多余链路置于Blocking（关闭）状态，而只留一条活动链路，当使用中的活动链路失效时，立即启用被Block的链路，以此来提供网络的冗余效果。

STP并非思科私有协议，STP为IEEE标准协议，并且有多个协议版本，版本与协议号的对应关系如下：

**Common Spanning Tree (CST)**  =  IEEE 802.1D

**Rapid Spanning Tree Protocol (RSTP)**  =  IEEE 802.1w

**Per-VLAN Spanning-Tree plus (PVST+)**   =   Per-VLAN EEE 802.1D

**Rapid PVST+**  =  Per-VLAN IEEE 802.1w

**Multiple Spanning Tree Protocol (MSTP)**   =    IEEE 802.1s

下面来详细介绍STP协议：

请观察如下网络环境：

![STP%EF%BC%88Spanning-Tree%20Protocol%EF%BC%89%2050f1f3e6d8c146789c2a802c1a33abf8/image2.png](STP（Spanning-Tree%20Protocol）/image2.png)

在如上所示的网络环境中，不难看出，当所有主机都使用单条链路与一台核心相连时，只要不再增加其它额外设备与链路，就不可能存在环路。交换机就当相于Hub一样连接了多台主机，而这样的网络结构，被称为hub-spoke网络结构，只要主机与Hub是连通的，那么就表示主机之间是连通的。基于此原因，STP借助了hub-spoke网络结构无环的网络思想，将一个拥有多台交换机通过多条链路相连的网络，通过Block掉任意两点之间多余的链路而只留下单条链路，最终修整出一个hub-spoke的网络环境，创造一个无环的交换网络。

![STP%EF%BC%88Spanning-Tree%20Protocol%EF%BC%89%2050f1f3e6d8c146789c2a802c1a33abf8/image3.png](STP（Spanning-Tree%20Protocol）/image3.png)

在上图的交换网络中，由于存在多台交换机，并且交换机之间有多条冗余链路，因此，只要在网络中找一台交换机充当核心，也就是相当于hub-spoke网络中的Hub，而其它交换机则留出一条活动链路到核心交换机即可，其它链路全部被block，当留出的活动链路失效之后，再启用block链路作为备份。上图中SW1被选作交换网络中的核心，而其它交换机则只留一条活动链路到核心交换机，只要其它交换机与核心交换机是通的，就证明交换机之间一定是通的。图中红色的连路表示被留出的普通交换机到核心交换机的活动链路，蓝色链路表示被block掉的链路，只要红色链路是通的，就表示整个网络都是通的，当某条红色链路断掉以后，只要启用相应的蓝色链路代替即可，也就实现了网络的冗余功能。

通过上述的解释，STP要构建出无环的交换网络，就必须在网络中选出一台交换机做为核心交换机，STP称其为Root，也就是根，功能相当于hub-spoke网络中的Hub。其它不是Root的交换机则需要留出一条活动链路去往根交换机，因为只要普通交换机到根是通的，到其它交换机也就是通的。

需要说明的是，只有在一个三层网络中，广播能够到达的范围内，才需要进行相同的STP计算与选举，也就是一个广播域内独立选举STP：

![STP%EF%BC%88Spanning-Tree%20Protocol%EF%BC%89%2050f1f3e6d8c146789c2a802c1a33abf8/image4.png](STP（Spanning-Tree%20Protocol）/image4.png)

上图中，因为网络被路由器分割成两个广播域，所以在两个网段中，需要进行独立的STP计算与选举。

STP在计算与选举时，只会留下唯一一条活动链路，将其它所有多余链路全部block，所以STP要确定两点之间是否存在多条链路，因为只有两点之间有多条链路时，才有链路需要被block。要确认两点之间网络是否通畅，只要发送数据作个测试即可得到答案，而要确认两点之间是否有多条链路，方法还是发送数据作个测试就能得到答案。当然，要测试两点之间是否有多条链路，需要发送特殊的数据来做测试，比如给数据包都做上相同的标记，然后发出去，如果交换机同时从多个接口收到相同标记的数据包，很显示，交换机与发送者之间就是存在多条链路的，因此需要靠STP计算来断开多余链路。

STP在发送数据包测试网络是否有多条链路，是靠发送bridge protocol data units (BPDUs)来完成的，同台交换机发出去的BPDU都被做上了相同的标记，只要任何交换机从多个接口收到相同标记的BPDU，就表示网络中有冗余链路，因此需要STP断开多余链路。BPDU数据包里面有以下信息：

根交换机的bridge ID。

发送交换机的bridge ID 。

到根交换机的Path Cost。

发送接口以及优先级。

Hello、forward delay、max-age时间。

同台交换机发出的BPDU，bridge ID都是一样的，因为是用来标识自己的，其中bridge ID由两部分组成：Bridge优先级和MAC地址，默认优先级为32678。

交换机上的每个端口也是有优先级的，默认为128，范围为0-255。

**注：**在STP协议中，所有优先级数字越小，表示优先级越高，数字越大，优先级越低。

STP在计算网络时，需要在网络中选举出根交换机（Root），根端口（Root Port），以及指定端口(Designated Port)，才能保证网络的无环，选举规则分别如下：

**根交换机（Root）**

在同一个三层网络中需要选举，即一个广播域内要选举，并且一个网络中只能选举一台根交换机。Birdge-ID中优先级最高（即数字最小）的为根交换机，优先级范围为0-65535，如果优先级相同，则MAC地址越小的为根交换机。

**根端口（Root Port）**

所有非根交换机都要选举，非根交换机上选举的根端口就是普通交换机去往根交换机的唯一链路，选举规则为 到根交换机的Path Cost值最小的链路，如果多条链路到达根交换机的Path Cost值相同，则选举上一跳交换机Bridge-ID最小的链路，如果是经过的同一台交换机，则上一跳交换机Bridge-ID也是相同的，再选举对端端口优先级最小的链路，如果到达对端的多个端口优先级相同，最后选举交换机本地端口号码最小的链路。

**指定端口(Designated Port)**

在每个二层网段都要选举，也就是在每个冲突域需要选举，简单地理解为每条连接交换机的物理线路的两个端口中，有一个要被选举为指定端口，每个网段选举指定端口后，就能保证每个网段都有链路能够到达根交换机，选举规则和选举根端口一样，即：到根交换机的Path Cost值最小的链路，如果多条链路到达根交换机的Path Cost值相同，则选举上一跳交换机Bridge-ID最小的链路，如果是经过的同一台交换机，则上一跳交换机Bridge-ID也是相同的，再选举对端端口优先级最小的链路，如果到达对端的多个端口优先级相同，最后选举交换机本地端口号码最小的链路。

在STP选出根交换机，根端口以及指定端口后，其它所有端口全部被Block，为了防止环路，所以Block端口只有在根端口或指定端口失效的时候才有可能被启用。

交换机上的端口，根据端口的带宽不同，Path Cost值也不同，以下参数为标准：

> 10 Mb/s：100
> 
> 
> 100 Mb/s：19
> 
> 1000 Mb/s：4
> 
> 10000 Mb/s：2
> 
> 可以看出，带宽越高，被选为根端口和指定端口的几率就越大，所以经过STP选举后，活动的链路总是性能最好的，其它被Block掉的端口，将在活动端口失效时被启用。
> 
> 以下图为例来看STP计算：
> 

![STP%EF%BC%88Spanning-Tree%20Protocol%EF%BC%89%2050f1f3e6d8c146789c2a802c1a33abf8/image5.png](STP（Spanning-Tree%20Protocol）/image5.png)

> 上图的网络环境中，运行STP后，则选举如下角色：（所有链路为100 Mb/s，即Path Cost值为19）
> 
> 
> **根交换机（Root）**
> 
> 因为4台交换机的优先级分别为 SW1（4096） ，SW2（24576），SW3（32768），SW4（32768），选举优先级最高的（数字最低的）为根交换机，所以SW1被选为根交换机，如果优先级相同，则比较MAC地址。
> 
> **根端口（Root Port）**
> 
> 根端口需要在除SW1外的非根交换机上选举。
> 
> SW2上从端口F0/23到达根的Path Cost值为19，从F0/19和F0/20到达根的Path Cost值都为19×3=57。因此，F0/23被选为根端口。
> 
> SW3上从端口F0/19到达根的Path Cost值为19，从F0/23和F0/24到达根的Path Cost值都为19×3=57。因此，F0/19被选为根端口。
> 
> SW4上从所有端口到达根的Path Cost值都为19×2=38，所以从比较Path Cost值，无法选出根端口，接下来比较上一跳交换机Bridge-ID，也就是比较SW2与SW3的Bridge-ID，所以选择往SW2的方向，然而通过端口F0/19和F0/20都可以从SW2到达根交换机，所以接下来比较端口F0/19和F0/20对端交换机端口的优先级，因为SW2的F0/19端口优先级为128，而F0/20的端口优先级为112，所以SW4选择连接SW2的F0/20的端口为根端口，即SW4的F0/20为根端口，如果此步还选不出，SW4将根据本地端口号做出决定，也就是F0/19和F0/20，数字小的为根端口，也就是F0/19。
> 
> **指定端口(Designated Port)**
> 
> 每个网段（每个冲突域），或理解为每条线路都要选举指定端口。
> 
> 在根交换机SW1连接SW2的网段与连接SW3的网段中，当然是根自己的端口离自己最近，所以这两个网段中，选举根交换机上的端口为指定端口，因此，根交换机上所有的端口都应该是指定端口。
> 
> 在SW3连接SW4的两个网段中，同样也是SW3上的两个端口离根交换机最近，所以在这两个网段中，选举SW3上的端口为指定端口。
> 
> 在SW2连接SW4的两个网段中，同样也是SW2上的两个端口离根交换机最近，所以在这两个网段中，选举SW2上的端口为指定端口。
> 
> **注：**根交换机上所有的端口最终都为指定端口。
> 
> 其它既不是根端口，也不是指定端口的落选的端口，就是SW4上的F0/19，F0/23，F0/24，都将被STP放入Blocking状态，不为用户提供数据转发，以此来防止环路。最终的网络，构建出了任何两点之间，都是单链路的环境，不会有环路，当使用中的链路失效时，Blocking的端口可以代替原端口。上图的STP选举结果如下：
> 
> **根交换机（Root）**
> 
> SW1
> 
> **根端口（Root Port）**
> 
> SW2：F0/23    SW3：F0/19    SW4：F0/20
> 
> **指定端口(Designated Port)**
> 
> SW1：F0/19，F0/23    SW2：F0/19，F0/20    SW3：F0/23，F0/24
> 
> **Blocking端口**
> 
> SW4：F0/19，F0/23，F0/24
> 
> 结果图如下：
> 

![STP%EF%BC%88Spanning-Tree%20Protocol%EF%BC%89%2050f1f3e6d8c146789c2a802c1a33abf8/image6.png](STP（Spanning-Tree%20Protocol）/image6.png)

**注：**一个端口，在STP中只能处于一种角色，不可能是两种角色。

在交换机启动后，端口要过渡到转发状态，需要经历以下的状态：

1 从initialization（初始化）到blocking

2 从blocking到listening或disabled

3 从listening 到learning或disabled

4 从learning到forwarding或disabled

被Disabled的接口相当于关闭了，每个状态有如下功能：

**Blocking**

丢弃所有收到的数据帧，不学习MAC地址，能收BPDU但不发BPDU。

**Listening**

丢弃所有收到的数据帧，不学习MAC地址，能收BPDP的处理BPDU，并进行STP计算。

**Learning**

丢弃所有收到的数据帧，会学习MAC地址，能收BPDU和处理BPDU。

**Forwarding**

也就是正常转发状态，能转发收到的数据帧，能学习MAC地址，接收并处理BPDU。

**Disabled**

丢弃所有收到的数据帧，不学习MAC地址，能收BPDU，除此之外不会再做其它的。

当交换机启动后，都认为自己是根交换机，然后从所有接口向网络中发送BPDU，称为configuration BPDU，所以configuration BPDU是根交换机发出的。当交换机收到更优Bridge-ID的configuration BPDU，会将它从自己所有接口转发出去，并保存在接口，如果收到差的configuration BPDU，则全部丢掉，所以在交换网络中，只有根交换机的BPDU在转发，其它普通交换机的BPDU不会出现在网络中。

根交换机的BPDU会在每个hello时间往网络中发送一次，hello时间默认为2秒钟，也就是交换机的BPDU会在每2秒钟往网络中发送一次，如果普通交换机在max-age时间内没有收到根交换机的BPDU，则认为根交换机已经失效，便开始重新选举BPDU，默认max-age时间为20秒，即10倍hello时间。

除了hello时间和max-age时间外，还有一个forward delay时间，默认为15秒，接口在经过Listening 和Learning状态时，都会分别停留一个 forward delay时间，也就是说接口从Listening状态到Learning状态，最后变成转发状态，需要经过两个forward delay时间共计30秒。

因为STP有多个版本，不同版本的STP，在操作和运行上，会有所不同，但是需要说明，无论什么版本的STP，对根交换机，根端口以及指定端口的选举规则完全是一样的，下面分别详细介绍各版本的运行过程：

**Common Spanning Tree (CST)**

> CST的协议号为IEEE 802.1D，如果交换机运行在CST，交换机只进行一次STP计算，无论交换机上有多少个VLAN，所有流量都会走相同的路径。
> 

**Rapid Spanning Tree Protocol (RSTP)**

> RSTP是快速STP，协议号为IEEE 802.1w，在运行CST时，端口状态blocking、listening、disabled都不发送数据，RSTP将这三个状态归为一个状态，discarding状态。其次之外就是learning和forwarding状态，所以RSTP端口状态为discarding、learning和forwarding。
> 
> 
> 当运行CST时，如果根交换机失效了，那么需要等待10个hello时间，也就是20秒收不到根交换机BPDU才能发现，再将block的端口过滤到forwarding状态，还需要经过两个forward delay时间共计30秒，所以CST在网络出现故障时，要经过50秒才能启用block端口，而RSTP则只需要在3个hello时间，即6秒收不到根交换机BPDU，便认为根交换机已经失去连接，就立刻启用discarding状态的接口，RSTP在根交换机失效后，并不会进行完整的STP计算，会在该启用备用端口时立即启用，因此网络收敛速度快，RSTP会在低于1秒的时间内恢复网络。
> 

**Per-VLAN Spanning-Tree plus (PVST+)**

> PVST+是思科自己的协议，在之前有一个PVST，但由于PVST只能支持ISL Trunk，所以思科为了扩展PVST支持IEEE 802.1Q，诞生了PVST+，在多数三层交换机，如3550、3560及以上型号，默认运行的STP版本为PVST+。PVST+是基于CST（IEEE 802.1D）运行的，但运行了PVST+的交换机并不像CST那样只进行一次STP计算，PVST+会在每个VLAN进行一次STP计算，也就是会根据VLAN数的不同，计算STP的次数也不同，并且每个VLAN的STP信息是单独保存的。请看下图：
> 

![STP%EF%BC%88Spanning-Tree%20Protocol%EF%BC%89%2050f1f3e6d8c146789c2a802c1a33abf8/image7.png](STP（Spanning-Tree%20Protocol）/image7.png)

在上图的网络中，各台交换机上都有VLAN 10，VLAN 20，VLAN 30，VLAN 40，在运行CST的情况下，因为只进行一次STP计算，所以SW1到SW4的流量要么从SW2走，要么从SW3走，在这种情况下，流量只能走同一条路径，而另一条路径完全被空闲而得不到利用。

当在上图的网络中运行PVST+后，因为PVST+会在每个VLAN进行不同的STP计算，称为STP实例（instance），所以可以控制每个VLAN流量的路径走向。上图中，就可以通过PVST+控制SW1的VLAN10和VLAN20从连接SW2的接口到达SW4，控制SW1的VLAN 30和VLAN 40从连接SW3的接口到达SW4，这样之后，将不同的VLAN流量分担到不同的路径，即实现了负载均衡，也通过STP避免了环路。

**重点说明：**

PVST+ 只支持128个实例（instance），如果交换机上配置的VLAN数超过128个，那么128个以外的VLAN将没有STP在运行，所以此时剩余的VLAN将出现环路。可以单独在特定的VLAN上打开或关闭STP功能，即使一台没有运行STP的交换机或没有运行STP的VLAN，在收到BPDU时，也会转发的，所以在对单个VLAN进行开启或关闭STP时，请确保交换机能够计算出无环的网络，否则网络将出现预想不到的故障。

在PVST+可以配置全局关闭某VLAN的STP，如关闭VLAN 10 的STP

no spanning-tree vlan 10，恢复使用命令spanning-tree vlan 10

**Extended System ID**

默认交换机的Bridge-ID的优先级为32768，当开启Extended System ID功能后，每个VLAN的默认的Bridge-ID优先级就不再是32768了，需要再加上VLAN号码，如VLAN 1的Bridge-ID优先级就是32768+1=32769，VLAN 8的Bridge-ID优先级就是32768+8=32776。

如果网络中即有开启了Extended System ID功能的交换机，也有关闭的，那么关闭Extended System ID功能的交换机有更大的机会成为根交换机，因为自己默认的优先级就比其它开启了Extended System ID功能的优先级更高（数字更小）。

[返回目录](http://www.china-ccie.com/ccie/lilun/switching/switching.html)

**Rapid PVST+**

> Rapid PVST+就是具有RSTP特性的PVST+，是像RSTP一样基于IEEE 802.1w运行的，其它所有运行与规则与PVST+完全相同，不再做详细介绍。
> 

**Multiple Spanning Tree Protocol (MSTP)**

> MSTP的协议号为IEEE 802.1s，因为在交换机存在多个VLAN时，CST会将所有流量放在单条路径中传输，而PVST+则可以通过为每个VLAN运行一个STP实例，从而将不同VLAN的流量放在不同的路径上传输。但正是由于PVST+为每个VLAN都运行了一个STP实例，可能会多达128个STP实例，所以PVST+会极其消耗系统资源。比如交换机上有20个VLAN，而PVST+会维护20个STP实例，但是这20个VLAN的流量也许只需要被分担到几条不同路径上，那就只需要维护几个STP实例即可，而并不需要维护20个STP实例。MSTP正因为这个原因，将需要进行相同STP计算的VLAN映射到同一个STP实例中，即无论有多少个VLAN，只要实际需要多少条不同的路径，就根据需要的路径维护相同的STP实例数，从而大大节省系统资源，如下图：
> 

![STP%EF%BC%88Spanning-Tree%20Protocol%EF%BC%89%2050f1f3e6d8c146789c2a802c1a33abf8/image7.png](STP（Spanning-Tree%20Protocol）/image7.png)

还是以此图为例，因为各台交换机上都有VLAN 10，VLAN 20，VLAN 30，VLAN 40，为了能够在SW1上让不同VLAN的流量从不同的路径到达SW4，所以可以运行PVST+，将流量分担到不同的路径上，即SW1通过PVST+将VLAN10和VLAN20的流量从连接SW2的接口到达SW4，将VLAN 30和VLAN 40的流量从连接SW3的接口到达SW4，但PVST+维护了4个STP 实例，才达到此效果，不难看出，其实网络中只有两个不同的路径，VLAN 10和VLAN 20的路径完全是相同的，VLAN 30和VLAN 40的路径也是完全相同的，此时，MSTP就可以通过将相同的VLAN映射到同一个STP实例，如将VLAN 10和VLAN 20映射到一个实例，再将VLAN 30和VLAN 40映射到另外一个实例，总共只有两个STP实例，既像PVST+那样实现了负载均衡的效果，也节省了系统资源。

MSTP是在RSTP的基础之上运行的，所以具有快速收敛的功能，但不能不运行RSTP时运行MSTP，RSTP是随着开启MSTP时自动开启的。MSTP最多支持65个STP实例，但是映射到实例的VLAN数量是没有限制的。默认所有VLAN都在实例0。

MSTP还需要通过分区域管理，即region，交换机要在同一region进行相同的STP计算，必须region name和revision number一致，最重要的是VLAN和实例的映射也要一致，否则STP计算出来的网络，将不是你想要的网络，一个VLAN只能被映射到一个实例，一个网络可以有多个MSTP revision，便于各自独立。

**拓朴变更**

当网络中的链路出现变化时，也就需要进行新的STP计算，并且由于交换机的MAC地址在表中的老化时间默认为300秒（5分钟），所以当原有的链路发生变化后，MAC地址与接口的对应关系也会发生变化，因此不能再等5分钟才更新，所以基于拓朴变化的因素，还需要将MAC地址的老化时间设置的更短，此动作在STP拓朴变更时，会自动更改为forward_delay的时间。

当网络链路发生变化后，必须进行新的STP计算，但是在正常的STP状态下，只有根交换机才能往网络里发送BPDU，称为configuration BPDU，而普通交换机只有接收configuration BPDU的权限，并不能向网络中发送BPDU。但是当交换机检测到链路变化时，可以通知网络中的根交换机，此时可以发送一种特殊的BPDU，叫做topology change notification (TCN)，也就是TCN BPDU。TCN BPDU是用来告诉根交换机网络链路有变化，因此TCN BPDU只能从根端口发出去，如果接收者不是根交换机，则必须回复一个确认消息，这个消息是一个设置了TCA位的configuration BPDU，然后自己再从根端口向根发送TCN BPDU，直到根收到为止，当根收到TCN BPDU后，需要回复该BPDU，方式为发送一个设置了TC位的configuration BPDU。

其中，TCN是一种特殊的BPDU，而TCA只是设置了TCA位的configuration BPDU，TC也只是设置了TC位的configuration BPDU。最终STP网络中，出现了两种BPDU，即TCN BPDU和configuration BPDU。

**注：**

★在配置STP时，Bridge-ID的优先级，端口优先级，hello时间，max-age时间，forward delay时间都可以手工修改，而Bridge-ID的优先级必须为4096的整数倍，端口优先级必须为16的整数倍。

★在修改时，PVST+可以基于每个VLAN修改，而MSTP则只能基于实例，而不能基于VLAN，因为一个实例会有多个VLAN。

可以通过命令来强制指定某台交换机为根交换机，当使用命令强制指定某交换机为根后，此交换机将通过修改一个比当前根交换机更高优先级的Bridge-ID，以此来抢夺根交换机的角色，如果命令再到别的交换机上输入，那么那台交换机将再次抢夺根交换机的角色，因为它可以修改自己的Bridge-ID比当前根更高的优先级，所以此命令最后在网络中的哪台交换机上输入后，哪台交换机就能成为根交换机，但是也有个限度，因为交换机的Bridge-ID不能自动改的比1小，又不能改MAC地址，所以如果需要修改优先级到1以下才能抢夺根交换机的角色，那么此命令将提示错误。

**注：**链路的全双工与半双工，在STP中，被分为不同的链路类型，如果是全双工（full-duplex），叫做point-to-point(P2p)，如果是半双工，叫做（half-duplex）。接口下可以手工更改：spanning-tree link-type point-to-point。

**配置**

**配置PVST+**

![STP%EF%BC%88Spanning-Tree%20Protocol%EF%BC%89%2050f1f3e6d8c146789c2a802c1a33abf8/image8.png](STP（Spanning-Tree%20Protocol）/image8.png)

**说明：**以上图为例，配置PVST+，默认交换机上都配置有VLAN 10，VLAN 20，VLAN 30，VLAN 40，要求控制SW1与SW4之间的流量路径为VLAN 10和VLAN 20从 SW1—SW2—SW4，VLAN 30和VLAN 40从 SW1—SW3—SW4。

**注：**默认为PVST+，所以STP版本不用改。

**1.配置各交换机优先级（只能为4096的整数倍）**

**（1）配置SW1在所有VLAN的优先级为4096**

sw1(config)#spanning-tree vlan 10-40 priority 4096

**（2）配置SW2在所有VLAN的优先级 24576**

sw2(config)#spanning-tree vlan 10-40 priority 24576

**（3）配置SW3在所有VLAN的优先级 32768**

sw3(config)#spanning-tree vlan 10-40 priority 32768

**（4）配置SW4在所有VLAN的优先级32768**

sw4(config)#spanning-tree vlan 10-40 priority 32768

**2.配置SW2的F0/20的端口优先级（必须为16的整数倍）**

**（1）在所有VLAN将SW2的F0/20的端口优先级配置为112**

sw2(config)#int f0/20

sw2(config-if)#spanning-tree vlan 10-40 port-priority 112

**3.查看根交换机**

**（1）查看根交换机SW1**

**说明：**因为现在4个VLAN的配置是一样的，结果也是一样的，所以只提供一个VLAN的结果：

sw1#sh spanning-tree

（输出被省略）

VLAN0010

Spanning tree enabled protocol ieee

Root ID    Priority    4106

Address     001a.6c6f.fb00

This bridge is the root

Hello Time   2 sec  Max Age 20 sec  Forward Delay 15 sec

Bridge ID  Priority    4106   (priority 4096 sys-id-ext 10)

Address     001a.6c6f.fb00

Hello Time   2 sec  Max Age 20 sec  Forward Delay 15 sec

Aging Time 300

Interface        Role Sts Cost      Prio.Nbr Type

- --------------- ---- --- --------- -------- --------------------------------

Fa0/23           Desg FWD 19        128.25   P2p

（输出被省略）

sw1#

**说明：**从结果中看出，SW1手工配置的优先级为4096，但由于Extended System ID功能，所以优先级加上了VLAN号码10，结果优先级变为4106，因为优先级在网络中数字最小，所以自己就是当前网络的根交换机。

**4.查看根端口**

**（1）查看SW2的根端口**

sw2#sh spanning-tree

（输出被省略）

VLAN0010

Spanning tree enabled protocol ieee

Root ID    Priority    4106

Address     001a.6c6f.fb00

Cost        19

Port        23 (FastEthernet0/23)

Hello Time   2 sec  Max Age 20 sec  Forward Delay 15 sec

Bridge ID  Priority    24586  (priority 24576 sys-id-ext 10)

Address     0013.805c.9d00

Hello Time   2 sec  Max Age 20 sec  Forward Delay 15 sec

Aging Time 300

Interface        Role Sts Cost      Prio.Nbr Type

- --------------- ---- --- --------- -------- --------------------------------

Fa0/19           Desg FWD 19        128.19   P2p

Fa0/20           Desg FWD 19        112.20   P2p

Fa0/23           Root FWD 19        128.23   P2p

（输出被省略）

sw2#

**说明：**因为SW2上从端口F0/23到达根的Path Cost值为19，从F0/19和F0/20到达根的Path Cost值都为19×3=57。因此，F0/23被选为根端口。

**（2）查看SW3的根端口**

sw3#sh spanning-tree

（输出被省略）

VLAN0010

Spanning tree enabled protocol ieee

Root ID    Priority    4106

Address     001a.6c6f.fb00

Cost        19

Port        21 (FastEthernet0/19)

Hello Time   2 sec  Max Age 20 sec  Forward Delay 15 sec

Bridge ID  Priority    32778  (priority 32768 sys-id-ext 10)

Address     001a.a256.f300

Hello Time   2 sec  Max Age 20 sec  Forward Delay 15 sec

Aging Time 15

Interface        Role Sts Cost      Prio.Nbr Type

- --------------- ---- --- --------- -------- --------------------------------

Fa0/19           Root FWD 19        128.21   P2p

Fa0/23           Desg FWD 19        128.25   P2p

Fa0/24           Desg FWD 19        128.26   P2p

（输出被省略）

sw3#

**说明：**因为SW3上从端口F0/19到达根的Path Cost值为19，从F0/23和F0/24到达根的Path Cost值都为19×3=57。因此，F0/19被选为根端口。

**（3）查看SW4的根端口**

sw4#sh spanning-tree

（输出被省略）

VLAN0010

Spanning tree enabled protocol ieee

Root ID    Priority    4106

Address     001a.6c6f.fb00

Cost        38

Port        22 (FastEthernet0/20)

Hello Time   2 sec  Max Age 20 sec  Forward Delay 15 sec

Bridge ID  Priority    32778  (priority 32768 sys-id-ext 10)

Address     001e.14cf.0980

Hello Time   2 sec  Max Age 20 sec  Forward Delay 15 sec

Aging Time 300

Interface        Role Sts Cost      Prio.Nbr Type

- --------------- ---- --- --------- -------- --------------------------------

Fa0/19           Altn BLK 19        128.21   P2p

Fa0/20           Root FWD 19        128.22   P2p

Fa0/23           Altn BLK 19        128.25   P2p

Fa0/24           Altn BLK 19        128.26   P2p

（输出被省略）

sw4#

**说明：**因为SW4上从所有端口到达根的Path Cost值都为19×2=38，所以从比较Path Cost值，无法选出根端口，接下来比较上一跳交换机Bridge-ID，也就是比较SW2与SW3的Bridge-ID，所以选择往SW2的方向，然而通过端口F0/19和F0/20都可以从SW2到达根交换机，所以接下来比较端口F0/19和F0/20对端交换机端口的优先级，因为SW2的F0/19端口优先级为128，而F0/20的端口优先级为112，所以SW4选择连接SW2的F0/20的端口为根端口，即SW4的F0/20为根端口

**5.查看指定端口**

**（1）查看SW1的指定端口**

sw1#sh spanning-tree

（输出被省略）

VLAN0010

Spanning tree enabled protocol ieee

Root ID    Priority    4106

Address     001a.6c6f.fb00

This bridge is the root

Hello Time   2 sec  Max Age 20 sec  Forward Delay 15 sec

Bridge ID  Priority    4106   (priority 4096 sys-id-ext 10)

Address     001a.6c6f.fb00

Hello Time   2 sec  Max Age 20 sec  Forward Delay 15 sec

Aging Time 300

Interface        Role Sts Cost      Prio.Nbr Type

- --------------- ---- --- --------- -------- --------------------------------

Fa0/19           Desg FWD 19        128.21   P2p

Fa0/23           Desg FWD 19        128.25   P2p

（输出被省略）

SW1#

**说明：**在根交换机SW1连接SW2的网段与连接SW3的网段中，当然是根自己的端口离自己最近，所以这两个网段中，选举根交换机上的端口为指定端口，因此，根交换机上所有的端口都应该是指定端口。

**（2）查看SW2的指定端口**

sw2#sh spanning-tree

（输出被省略）

VLAN0010

Spanning tree enabled protocol ieee

Root ID    Priority    4106

Address     001a.6c6f.fb00

Cost        19

Port        23 (FastEthernet0/23)

Hello Time   2 sec  Max Age 20 sec  Forward Delay 15 sec

Bridge ID  Priority    24586  (priority 24576 sys-id-ext 10)

Address     0013.805c.9d00

Hello Time   2 sec  Max Age 20 sec  Forward Delay 15 sec

Aging Time 300

Interface        Role Sts Cost      Prio.Nbr Type

- --------------- ---- --- --------- -------- --------------------------------

Fa0/19           Desg FWD 19        128.19   P2p

Fa0/20           Desg FWD 19        112.20   P2p

Fa0/23           Root FWD 19        128.23   P2p

（输出被省略）

Sw2#

**说明：**在SW2连接SW4的两个网段中，同样也是SW2上的两个端口离根交换机最近，所以在这两个网段中，选举SW2上的端口为指定端口。

**（3）查看SW2的指定端口**

sw3#sh spanning-tree

（输出被省略）

VLAN0010

Spanning tree enabled protocol ieee

Root ID    Priority    4106

Address     001a.6c6f.fb00

Cost        19

Port        21 (FastEthernet0/19)

Hello Time   2 sec  Max Age 20 sec  Forward Delay 15 sec

Bridge ID  Priority    32778  (priority 32768 sys-id-ext 10)

Address     001a.a256.f300

Hello Time   2 sec  Max Age 20 sec  Forward Delay 15 sec

Aging Time 300

Interface        Role Sts Cost      Prio.Nbr Type

- --------------- ---- --- --------- -------- --------------------------------

Fa0/19           Root FWD 19        128.21   P2p

Fa0/23           Desg FWD 19        128.25   P2p

Fa0/24           Desg FWD 19        128.26   P2p

（输出被省略）

Sw3#

**说明：**在SW3连接SW4的两个网段中，同样也是SW3上的两个端口离根交换机最近，所以在这两个网段中，选举SW3上的端口为指定端口。

**（4）查看SW2的指定端口**

sw4#sh spanning-tree

（输出被省略）

VLAN0010

Spanning tree enabled protocol ieee

Root ID    Priority    4106

Address     001a.6c6f.fb00

Cost        38

Port        22 (FastEthernet0/20)

Hello Time   2 sec  Max Age 20 sec  Forward Delay 15 sec

Bridge ID  Priority    32778  (priority 32768 sys-id-ext 10)

Address     001e.14cf.0980

Hello Time   2 sec  Max Age 20 sec  Forward Delay 15 sec

Aging Time 300

Interface        Role Sts Cost      Prio.Nbr Type

- --------------- ---- --- --------- -------- --------------------------------

Fa0/19           Altn BLK 19        128.21   P2p

Fa0/20           Root FWD 19        128.22   P2p

Fa0/23           Altn BLK 19        128.25   P2p

Fa0/24           Altn BLK 19        128.26   P2p

（输出被省略）

sw4#

**说明：**除了根端口和指定端口，其它的都为落选端口，也就是SW4上的F0/19，F0/23，F0/24，都将被STP放入Blocking状态，不为用户提供数据转发，以此来防止环路

**6.调整VLAN 30和VLAN 40的路径为 SW1—SW3—SW4。**

**说明：**因为默认4个VLAN相同配置，所以全部和VLAN 10一样，路径为SW1—SW2—SW4，现只对VLAN 30和VLAN 40做修改，以调整路径为SW1—SW3—SW4。

**（1）修改SW3在VLAN 30和VLAN 40的Bridge-ID优先级**

**说明：**因为选举根端口和指定端口的第一步为比较到根的Path Cost值，第二步为比较上一跳Bridge-ID，而SW4从SW2到SW1和从SW3到SW1的Path Cost值全部是一样的，所以可以选择修改SW3在VLAN 30和VLAN 40的Bridge-ID优先级来做调整：

sw3(config)#spanning-tree vlan 30,40 priority 20480

**说明：**SW3在VLAN 30和VLAN 40的Bridge-ID优先级必须比SW2的Bridge-ID优先级小，才能将VLAN 30与VLAN 40的流量引过来。

**7.查看修改后的VLAN 30与VLAN 40的路径**

**说明：**因为VLAN 30与VLAN 40相同配置，所以只查看一个VLAN 即可。

**（1）查看SW4上VLAN 10与VLAN 30的路径对比**

sw4#sh spanning-tree

（输出被省略）

VLAN0010

Spanning tree enabled protocol ieee

Root ID    Priority    4106

Address     001a.6c6f.fb00

Cost        38

Port        22 (FastEthernet0/20)

Hello Time   2 sec  Max Age 20 sec  Forward Delay 15 sec

Bridge ID  Priority    32778  (priority 32768 sys-id-ext 10)

Address     001e.14cf.0980

Hello Time   2 sec  Max Age 20 sec  Forward Delay 15 sec

Aging Time 300

Interface        Role Sts Cost      Prio.Nbr Type

- --------------- ---- --- --------- -------- --------------------------------

Fa0/19           Altn BLK 19        128.21   P2p

Fa0/20           Root FWD 19        128.22   P2p

Fa0/23           Altn BLK 19        128.25   P2p

Fa0/24           Altn BLK 19        128.26   P2p

VLAN0030

Spanning tree enabled protocol ieee

Root ID    Priority    4126

Address     001a.6c6f.fb00

Cost        38

Port        25 (FastEthernet0/23)

Hello Time   2 sec  Max Age 20 sec  Forward Delay 15 sec

Bridge ID  Priority    32798  (priority 32768 sys-id-ext 30)

Address     001e.14cf.0980

Hello Time   2 sec  Max Age 20 sec  Forward Delay 15 sec

Aging Time 300

Interface        Role Sts Cost      Prio.Nbr Type

- --------------- ---- --- --------- -------- --------------------------------

Fa0/19           Altn BLK 19        128.21   P2p

Fa0/20           Altn BLK 19        128.22   P2p

Fa0/23           Root FWD 19        128.25   P2p

Fa0/24           Altn BLK 19        128.26   P2p

（输出被省略）

sw4#

**说明：**可以看到，SW4的VLAN 10还是保持原来的路径SW4—SW2—SW1，而VLAN 30的路径已经变成SW4—SW3—SW1并且VLAN 30的根端口为F0/23。

**8.调整STP参数**

**（1）调整SW4在VLAN 30的根端口为F0/24**

**说明：**因为SW4在VLAN 30从F0/23和F0/24到达根的Path Cost值都为19×2=38，所以从比较Path Cost值，无法选出根端口，接下来比较上一跳交换机Bridge-ID，由于都是SW3，所以Bridge-ID相同，接下来比较F0/23和F0/24对端交换机端口的优先级，但对方优先级都为128，所以最后选择了本地端口号码小的，即F0/23比F0/24小，F0/23被选为根端口，我们现在通过修改本地F0/24对端设备的端口优先级来调整路径，也就是修改SW3的F0/24的优先级：

sw3(config)#int f0/24

sw3(config-if)#spanning-tree vlan 30 port-priority 112

**说明：**端口优先级为16的整数倍。

**（2）查看SW4在VLAN 30的根端口**

sw4#sh spanning-tree vlan 30

VLAN0030

Spanning tree enabled protocol ieee

Root ID    Priority    4126

Address     001a.6c6f.fb00

Cost        38

Port        26 (FastEthernet0/24)

Hello Time   2 sec  Max Age 20 sec  Forward Delay 15 sec

Bridge ID  Priority    32798  (priority 32768 sys-id-ext 30)

Address     001e.14cf.0980

Hello Time   2 sec  Max Age 20 sec  Forward Delay 15 sec

Aging Time 300

Interface        Role Sts Cost      Prio.Nbr Type

- --------------- ---- --- --------- -------- --------------------------------

Fa0/19           Altn BLK 19        128.21   P2p

Fa0/20           Altn BLK 19        128.22   P2p

Fa0/23           Altn BLK 19        128.25   P2p

Fa0/24           Root FWD 19        128.26   P2p

sw4#

**说明：**因为选举时，比较对方的端口优先级，成功调整了路径，此时的根端口已变为F0/24。

**（3）修改SW4在VLAN 10的hello时间为3秒，max-age为25秒，forward delay为10秒**

sw4(config)#spanning-tree vlan 10 hello-time 3

sw4(config)#spanning-tree vlan 10 max-age 30

sw4(config)#spanning-tree vlan 10 forward-time 10

**（4）查看SW4在VLAN 10的hello时间，max-age，forward delay**

sw4#sh spanning-tree

（输出被省略）

VLAN0010

Spanning tree enabled protocol ieee

Root ID    Priority    4106

Address     001a.6c6f.fb00

Cost        38

Port        22 (FastEthernet0/20)

Hello Time   2 sec  Max Age 20 sec  Forward Delay 15 sec

Bridge ID  Priority    32778  (priority 32768 sys-id-ext 10)

Address     001e.14cf.0980

Hello Time   3 sec  Max Age 30 sec  Forward Delay 10 sec

Aging Time 300

Interface        Role Sts Cost      Prio.Nbr Type

- --------------- ---- --- --------- -------- --------------------------------

Fa0/19           Altn BLK 19        128.21   P2p

Fa0/20           Root FWD 19        128.22   P2p

Fa0/23           Altn BLK 19        128.25   P2p

Fa0/24           Altn BLK 19        128.26   P2p

VLAN0020

Spanning tree enabled protocol ieee

Root ID    Priority    4116

Address     001a.6c6f.fb00

Cost        38

Port        22 (FastEthernet0/20)

Hello Time   2 sec  Max Age 20 sec  Forward Delay 15 sec

Bridge ID  Priority    32788  (priority 32768 sys-id-ext 20)

Address     001e.14cf.0980

Hello Time   2 sec  Max Age 20 sec  Forward Delay 15 sec

Aging Time 300

Interface        Role Sts Cost      Prio.Nbr Type

- --------------- ---- --- --------- -------- --------------------------------

Fa0/19           Altn BLK 19        128.21   P2p

Fa0/20           Root FWD 19        128.22   P2p

Fa0/23           Altn BLK 19        128.25   P2p

Fa0/24           Altn BLK 19        128.26   P2p

（输出被省略）

sw4#

**说明：**可以看到，修改的时间只对VLAN 10生效，VLAN 20还是保持原状，PVST+可以单独修改每个VLAN 的参数。

**9.强制指定根与备份根**

**（1）指定SW2为VLAN 10的根**

sw2(config)#spanning-tree vlan 10 root primary

**（2）在SW2查看VLAN 10的根**

sw2#sh spanning-tree vlan 10

VLAN0010

Spanning tree enabled protocol ieee

Root ID    Priority    4106

Address     0013.805c.9d00

This bridge is the root

Hello Time   2 sec  Max Age 20 sec  Forward Delay 15 sec

Bridge ID  Priority    4106   (priority 4096 sys-id-ext 10)

Address     0013.805c.9d00

Hello Time   2 sec  Max Age 20 sec  Forward Delay 15 sec

Aging Time 15

Interface        Role Sts Cost      Prio.Nbr Type

- --------------- ---- --- --------- -------- --------------------------------

Fa0/19           Desg FWD 19        128.19   P2p

Fa0/20           Desg FWD 19        112.20   P2p

Fa0/23           Desg FWD 19        128.23   P2p

sw2#

**重点说明：**当使用命令强制指定某交换机为根后，此交换机将通过修改一个比当前根交换机更高优先级的Bridge-ID，以此来抢夺根交换机的角色，如果命令再到别的交换机上输入，那么那台交换机将再次抢夺根交换机的角色，因为它可以修改自己的Bridge-ID比当前根更高的优先级，所以此命令最后在网络中的哪台交换机上输入后，哪台交换机就能成为根交换机，但是也有个限度，因为交换机的Bridge-ID不能自动改的比1小，又不能改MAC地址，所以如果需要修改优先级到1以下才能抢夺根交换机的角色，那么此命令将提示错误。

**配置MSTP**

![STP%EF%BC%88Spanning-Tree%20Protocol%EF%BC%89%2050f1f3e6d8c146789c2a802c1a33abf8/image8.png](STP（Spanning-Tree%20Protocol）/image8.png)

**1.配置MSTP**

**（1）改变所有交换机的STP模式为MSTP**

Sw1(config)#spanning-tree mode mst

Sw2(config)#spanning-tree mode mst

Sw3(config)#spanning-tree mode mst

Sw4(config)#spanning-tree mode mst

**（2）映射VLAN到实例**

sw1(config)#spanning-tree mst configuration

sw1(config-mst)#name ccie

sw1(config-mst)#revision 1

sw1(config-mst)#instance 1 vlan 10,20

sw1(config-mst)#instance 2 vlan 30,40

**说明：**其它交换机配置和SW1配置完全相同，必须region name和revision number完全相同，否则属于不同的region。

**2.控制VLAN 10和VLAN 20（实例1）的路径为 SW1—SW2—SW4，VLAN 30和VLAN 40（实例2）的路径为SW1—SW3—SW4。**

**(1)配置SW1为实例1和实例2的根交换机**

sw1(config)#spanning-tree mst 1 root primary

sw1(config)#spanning-tree mst 2 root primary

**（2）控制SW4在实例1连SW2的端口Path Cost值为10**

sw4(config)#int range f0/19-20

sw4(config-if-range)#spanning-tree mst 1 cost 10

**（3）控制SW4在实例2连SW3的端口Path Cost值为10**

sw4(config)#int ran f0/23-24

sw4(config-if-range)#spanning-tree mst 2 cost 10

**3.查看STP状态**

**（1）查看根交换机**

sw1#sh spanning-tree

（输出被省略）

MST1

Spanning tree enabled protocol mstp

Root ID    Priority    24577

Address     001a.6c6f.fb00

This bridge is the root

Hello Time   2 sec  Max Age 20 sec  Forward Delay 15 sec

Bridge ID  Priority    24577  (priority 24576 sys-id-ext 1)

Address     001a.6c6f.fb00

Hello Time   2 sec  Max Age 20 sec  Forward Delay 15 sec

Interface        Role Sts Cost      Prio.Nbr Type

- --------------- ---- --- --------- -------- --------------------------------

Fa0/19           Desg FWD 200000    128.21   P2p

Fa0/23           Desg FWD 200000    128.25   P2p

MST2

Spanning tree enabled protocol mstp

Root ID    Priority    24578

Address     001a.6c6f.fb00

This bridge is the root

Hello Time   2 sec  Max Age 20 sec  Forward Delay 15 sec

Bridge ID  Priority    24578  (priority 24576 sys-id-ext 2)

Address     001a.6c6f.fb00

Hello Time   2 sec  Max Age 20 sec  Forward Delay 15 sec

Interface        Role Sts Cost      Prio.Nbr Type

- --------------- ---- --- --------- -------- --------------------------------

Fa0/19           Desg FWD 200000    128.21   P2p

Fa0/23           Desg FWD 200000    128.25   P2p

sw1#

**说明：**可以看到SW1已经成为实例1和实例2的根交换机。

**（2）查看SW4的路径**

sw4#sh spanning-tree

（输出被省略）

MST1

Spanning tree enabled protocol mstp

Root ID    Priority    24577

Address     001a.6c6f.fb00

Cost        200010

Port        21 (FastEthernet0/19)

Hello Time   2 sec  Max Age 20 sec  Forward Delay 15 sec

Bridge ID  Priority    32769  (priority 32768 sys-id-ext 1)

Address     001e.14cf.0980

Hello Time   2 sec  Max Age 20 sec  Forward Delay 15 sec

Interface        Role Sts Cost      Prio.Nbr Type

- --------------- ---- --- --------- -------- --------------------------------

Fa0/19           Root FWD 10        128.21   P2p

Fa0/20           Altn BLK 10        128.22   P2p

Fa0/23           Altn BLK 200000    128.25   P2p

Fa0/24           Altn BLK 200000    128.26   P2p

MST2

Spanning tree enabled protocol mstp

Root ID    Priority    24578

Address     001a.6c6f.fb00

Cost        200010

Port        25 (FastEthernet0/23)

Hello Time   2 sec  Max Age 20 sec  Forward Delay 15 sec

Bridge ID  Priority    32770  (priority 32768 sys-id-ext 2)

Address     001e.14cf.0980

Hello Time   2 sec  Max Age 20 sec  Forward Delay 15 sec

Interface        Role Sts Cost      Prio.Nbr Type

- --------------- ---- --- --------- -------- --------------------------------

Fa0/19           Altn BLK 200000    128.21   P2p

Fa0/20           Altn BLK 200000    128.22   P2p

Fa0/23           Root FWD 10        128.25   P2p

Fa0/24           Altn BLK 10        128.26   P2p

sw4#

**说明：**可以看到，实例1与实例2的流量已经分担到两条不同的路径上，既实现了与PVST+相同的负载效果，也节省了系统资源，因为只有两个STP实例，而PVST+要4个STP实例。