# VLAN(VLAN,TRUNK,VTP)

VLAN(VLAN,TRUNK,VTP)

2011年6月27日

17:37

![VLAN(VLAN,TRUNK,VTP)%206db1088d3b6149a89644fc90a4ffa884/image1.png](VLAN(VLAN,TRUNK,VTP)/image1.png)

**3层结构：接入层，汇聚层，核心层**

**核心层一般用来快速交换**

**关于VLAN（Virtual Local Area Network,虚拟局域网）**

**1.VLAN是一种将局域网设备从逻辑上划分成一个个网段，从而实现虚拟工作组的数据交换技术**

**2.VLAN的实现方式：**

**（1）基于端口的VLAN：这是最常见的，现在都是使用的这种**

**（2）基于MAC地址的VLAN**

**（3）基于网络层协议的VLAN：VLAN按网络层协议来划分，可分为IP、IPX、DECnet、AppleTalk、Banyan等**

**（4）按IP组播划分的VLAN：即认为一个IP组播组就是一个VLAN**

**（5）按策略划分的VLAN**

**（6）按用户定义、非用户授权划分的VLAN**

**3.添加VLAN有两种方法：**

**（1）在Vlan Database下进行配置**

**（2）在全局模式下进行配置**

**4.将某个接口添加到VLAN的配置：**

**接口下：**

**switchport mode access**

**switchport access vlan 10**

**最佳简写：**

**sw m a**

**sw a v 10**

**关于native vlan**

**1.native vlan是dot1q中特有的，ISL中没有native vlan的概念(ISL对所有帧都进行封装，包括Native vlan)**

**2.native vlan默认是vlan 1**

**3.native vlan中的数据在trunk上传输的时候不打标签**

**4.如果要修改native vlan，要在两边同时修改**

**5.如果想使native vlan的数据在trunk上传输的时候也打标签，使用命令：vlan dot1q tag native**

**6.一般使用一个没有用户使用的vlan作为native vlan**

**对于一些二层协议，如STP，交换机之间需要互相协商，如果对STP数据包打tag的话，会导致一些不支持VLAN的交换机不能协商，为了解决这个问题，提出native vlan的概念。交换的管理流量以及未指定VLAN的流量,默认使用Native VLAN(默认为VLAN 1)来传送,这些流量不需要做802.1Q封装.**

**关于VLAN的范围**

**VLAN的范围是：0-4095**

**0，4095是保留VLAN**

**1：系统默认VLAN**

**2-1001（Normal Range）：用户可以配置的VLAN**

**1002-1005：留给令牌环和FDDI**

**1006-4095（Extended range）：用户可以配置的VLAN，只能在vtp透明模式的时候配置**

**补充：**

**1.1-1005的VLAN总是以vlan.dat的形式保存在交换机闪存或者是NVRAM部分的VLAN数据库中**

**2.在VTP透明模式中，交换机也支持VLAN号在1006-4094范围中的VLAN，也就是扩展VLAN。扩展VLAN不是在VLAN数据库中保存的。扩展VLAN必须在全局模式下配置，不能在Vlan Database中配置。**

**3.NVRAM:保存配置(startup-config)**

**flash:存放ios。可与PC中的硬盘类比。**

**ram:存放ios 的一个副本/路由表/路由信息等.可与PC中的内存类比。**

**bootrom:存放 mini-ios .可与PC中的cmos芯片类比。**

**4.所谓的vlan database实际上就是一个vlan.dat的文件，默认存在flash中，使用全局命令vtp file nvram:vlan.dat可以将vlan.dat放到nvram中**

**注意点：现在很多设备都逐渐取消了NVRAM，改用Flash来保存配置文件**

**关于Trunk（干道/干线）**

**1.Trunk一般使用在交换机与交换机之间，或者交换机与路由器之间（配置单臂路由的时候）**

**2.Trunk有两种封装形式：dot1q和ISL**

**关于dot1q和ISL的区别：**

**1.ISL是思科私有的，dot1q是公有的**

**2.ISL会在原始帧前加26字节，帧尾加4字节，所以有时也被称做封装**

**dot1q会在原始帧的内部添加4个字节，所以有时也被称作标记**

**3.ISL最多支持1000个VLAN，dot1q最多支持4096个VLAN**

**4.ISL对语音的支持不好，dot1q对语音（QoS）的支持比较好**

**5.dot1q中有native vlan的概念，ISL中没有**

**补充：现在是dot1q的天下**

**关于dot1q的帧格式：**

![VLAN(VLAN,TRUNK,VTP)%206db1088d3b6149a89644fc90a4ffa884/image2.png](VLAN(VLAN,TRUNK,VTP)/image2.png)

**以太网类型：2字节，默认是0x8100**

**PRI：3bits，在802.1p中定义的，有时也被称作CoS，用来做QoS的**

**令牌环封装标识：1bits，表示对令牌环的支持**

**VLAN号:12bits，用来携带VLAN号**

**关于DTP（Dynamic trunk protocol，动态trunk协议）**

**1.DTP是思科私有的**

**2.DTP是一种用来协商trunk的协议，如果在发送DTP的端口也收到了DTP包，那么这个端口就被协商成为trunk**

**关于协商trunk的4种模式：**

**1.desirable模式：主动发送DTP包**

**2.auto模式：不主动发送DTP包，但在接收到DTP包的时候会回复DTP包**

**3.trunk模式：静态配置成trunk模式，主动发送DTP包**

**4.access模式：静态配置成access模式**

接口模式（包括portchannel）：access、trunk（on）、auto（dynamic auto）、desirable（dynamic desirable）、nonegotiate

Trunk链路的几种mode:

OFF:当接口设置为access时(switch mode access)

ON:当强制指定端口为trunk时候(switch mode trunk)

DD(dynamic desirable):指定端口为动态协商(switch mode dynamic desirable)交换机端口默认

DA(dynamic auto):指定端口为自动(switch mode dynamic auto)

auto 和desirable是属于协商状态，思科建议为保证联通性设置时不用启用状态协商，即：switchport nonegotiate

switchport nonegotiate：阻止接口产生DTP（自动协商）帧，关闭中继的协商。该命令只有在接口上已经配置access或trunk之后才能使用。必须手工去配置相邻接口的模式。

**将端口静态配置成trunk模式的命令：**

**switchport mode trunk**

**switchport trunk encapsulation dot1q/ISL**

**最佳简写：**

**sw m t**

**sw t e d**

**注意点：在将一个端口配置成trunk的时候推荐使用这种方法，避免使用下面的方法去协商**

**将端口配置成desirable模式的命令：**

**switchport mode dynamic desirable**

**switchport trunk encapsulation dot1q/ISL**

**将端口配置成auto模式的命令：**

**switchport mode dynamic auto**

**switchport trunk encapsulation dot1q/ISL**

**配置trunk端口native vlan的命令：**

**switchport trunk native vlan 99**

**限制trunk端口允许通过的vlan的命令：**

**switchport trunk allowed vlan 1,5,11,1002-1005**

**配置trunk端口不发送DTP包的命令：**

**switchport nonegotiate**

**注意点：这条命令一般使用在：静态配置了trunk，所以不需要DTP包了，使用此命令禁用。**

**关于VTP**

**1.VTP是思科私有的**

**2.VTP的口诀：2层，组播，5分钟一次**

**3.用来传输vlan的配置信息,在整个交换网络中分发和同步VLAN的相关信息**

**4.VTP有个domain的概念，只有在相同的domain中才可以传输vlan的配置信息**

**5.VTP消息只能在trunk链路上传输**

**6.VTP的3种模式是：server，client，transparent**

**7.Catalyst交换机只能在每台交换机上维护单个VTP域**

**关于VTP的配置版本号：高版本号会向低版本号传输**

**关于Server模式**

**1.添加、删除、修改VLAN信息**

**2.发送、转发VLAN信息**

**3.存在NVRAM中**

**4、学习**

**口诀：添、删、改，发、转、存**

**关于Client模式**

**1.不能添加、删除、修改VLAN信息**

**2.发送、转发VLAN信息**

**3.不存在NVRAM中**

**4、学习**

**关于transparent模式**

**1.添加、删除、修改VLAN信息**

**2.不发送，但转发VLAN信息**

**3.存在NVRAM中**

**4、不学习**

**关于OFF模式----只在7.1或更高版本的Cisco CatOS软件才能支持VTP关闭模式**

**与透明模式相类似，区别：关闭模式在干道接口处丢弃VTP通告**

**show vtp status //查看配置版本号**

**实验：**

**Server（高）--------Server（低）：传**

**Server（高）--------Client（低）：传**

**Server（高）--------Transparent(低)：不传**

**Client（高）--------Server（低）：传**

**Client（高）--------Client（低）：传**

**Client（高）--------Transparent（低）：不传**

**Transparent-----Server：不传**

**Transparent---Client：不传**

**Transparent---Transparent：不传**

**Server（高）------Client（低）-------Client（低）：传**

**Client（高）------Server（低）-------Client（低）：传**

**Server（高）------Transparent（低）--Client（低）：传**

**关于VTP的配置**

**vtp domain**

**vtp mode**

**vtp password**

**在实际工程中要使用如下方法配置，为的是避免动态学习域名：**

**vtp password**

**vtp domain**

**vtp mode**

**关于VTP的裁剪**

**VTP的裁剪：通过阻止不必要的数据的泛洪来增加可用的带宽，提升数据传输率**

**使用裁剪前：**

![VLAN(VLAN,TRUNK,VTP)%206db1088d3b6149a89644fc90a4ffa884/image3.png](VLAN(VLAN,TRUNK,VTP)/image3.png)

**使用裁剪后：**

![VLAN(VLAN,TRUNK,VTP)%206db1088d3b6149a89644fc90a4ffa884/image4.png](VLAN(VLAN,TRUNK,VTP)/image4.png)

**注意点：**

**1.VTP裁剪，裁剪的是广播**

**2.VTP裁剪要在Server模式中配置，它会传给Client**

**配置命令：Sw1(config)#vtp pruning**

**补充：**

**PC机的工作原理：**

**1.如果目标地址与自己的地址在同一个网段，那么以目标地址为目标做ARP解析，取得对方的MAC地址，然后和对方通信**

**2.如果目标地址与自己的地址不在同一个网段，那么以网关作为目标地址做ARP解析，取得网关的MAC地址，然后把包交给网关，让网关去处理 //代理ARP的作用见附件**

**一般情况下，一个VLAN使用一个IP子网**

**将一台交换机加入到现存网络中**

**会出现倒灌现象**

**倒灌现象：新加入的交换机由于配置版本号比较高，可能会造成新加入的交换机内部的vlan会覆盖原有网络中的vlan，导致不能估计的错误。**

**为了防止倒灌现象，当将一台计算机加入到现有网络的时候，可以使用现有方法：**

**1.改域名：改成其他的域名，然后再改回来**

**2.改模式：特指改成透明模式，然后再改回来**

**3.清空配置：使用命令delete flash：/vlan.dat，这种方法要求重启机子**

**其实，说白了，这3种方法都是将新加入的交换机的配置版本号改成0。**

**口诀：改域名，改模式，清空配置**

**4.直接使用透明模式接入**

**设计VTP的时候需要考虑的事情：**

**1.控制好VTP域的边界**

**2.最好只有1个到2个Server**

**3.配置VTP的密码**

**4.在所有的设备上手工配置VTP的域名----尽量避免VTP域名的传输**

**5.当设计一个新域的时候，首先配置VTP客户端交换机，这样有好处**

**6.当清楚一个现存的VTP域的时候，首先在Server上更换密码，其他客户端可以维持现有的VLAN信息，直到Server完成了更新**

**关于vlan 1**

**1.默认情况下，交换机的端口都属于vlan 1**

**2.dot1q默认的native vlan是vlan 1**

**3.避免将vlan 1作为管理vlan**