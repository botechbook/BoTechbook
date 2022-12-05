# 针对于生成树的攻击（Spanning Tree Attack）

针对于生成树的攻击（Spanning Tree Attack）

2011年7月7日

14:55

二层安全

**针对于二层的攻击一般分为6种类型：**

**1.针对于生成树的攻击（Spanning Tree Attack）：使用BPDU Guard，BPDU Filter，Root Guard，Loop Guard，UDLD解决**

**2.针对于VLAN的跳跃攻击（VLAN “Hopping”）：**

**3.针对于MAC地址的攻击（MAC Attacks）：使用Port-security解决**

**4.针对于DHCP的攻击（DHCP Attacks）：使用Port-security，DHCP snooping解决**

**5.针对于ARP的攻击（ARP Attack）：使用DAI解决**

**6.哄骗攻击（Spoofing Attacks）：使用IP Source Guard解决**

一、 针对于生成树的攻击（Spanning Tree Attack）

STP的作用是防止环路

> 1）选举一个根网桥
> 
> 
> **2）选择所有非根网桥的根端口**
> 

**3）选择各个网段的指定端口**

**模拟STP攻击**

![%E9%92%88%E5%AF%B9%E4%BA%8E%E7%94%9F%E6%88%90%E6%A0%91%E7%9A%84%E6%94%BB%E5%87%BB%EF%BC%88Spanning%20Tree%20Attack%EF%BC%89%20ef3ddb1b583047da8fd137f703084826/image1.png](针对于生成树的攻击（Spanning%20Tree%20Attack）/image1.png)

<<SPT攻击简单说明.txt>>

**攻击者的手段：1、让网络产生环路，造成广播风暴。2、让网络重新选举根网桥**

CISCO交换机默认在端口上是起动 Spanning Tree协议

防止局域网中出现安全问题.Spanning Tree一般需要50秒的时间启动完成

Spanning-tree Portfast

**1、关于BPDU Guard** （阻塞）

BPDU是一种用于在STP协议之间发送的数据包，这里的数据包是异于网络中传输数据信息的数据包，正如前期所说的，一旦交换机的接口被配置成portfast时必须要在接口打上spanning-tree bpduguard enable这句话，**之后这个端口再收到BPDU包后就会进入errdisable状态**，从而避免环路。而如果没有启用BPDU guard，那么端口在接收的BPDU时候，stp会让端口进入blocking状态，也就是所谓的监听状态，在监听状态时，就会造成网络重新选举根交换。**它的配置方法主要有两种方式**，一种是在全局模式下输入spanning-tree portfast bpduGuard default，一种是在接口模式下输入spanning-tree bpduguard enable。两者的共同目的是一致的，都是为了在接口上启用BPDU Guard这个功能，但是也有所差别。**在全局模式下，接口必须先启用portfast特性才可以，而在接口下则不管是否启用了portfast特性，都可以开启BPDU Guard这个功能。**

**配置**

配置方法有两种:可以在全局下配置，也可以在接口下配置

Switch(config)# spanning-tree portfast bpduguard default

/---在启用了Port Fast特性的端口上启用BPDU Guard---/

Switch(config-if)# spanning-tree bpduguard enable

/---在不启用Port Fast特性的情况下启用BPDU Guard---/

在全局下配置和在接口下配置，功能是一样的

**一般BPDU Guard和PortFast结合使用**

最佳经验：以后在接入PC机的接口上开启portfast和BPDU Guard

**在端口上启用了PortFast以后**，如果没有启用BPDU Guard，那么端口收的BPDU的时候，STP会让端口进入blocking状态，当配置了BPDU Guard之后，端口收到BPDU的时候就会进入err-disable状态**可使用**

当接口出现errdisable状态,默认300秒后将重新启用该端口.该时间可以通过

errdisable recovery interval {sec}进行修改.

命令开启端口状态的自动恢复

模拟器可以打入部分命令

**2、关于BPDU Filter** （丢弃）

防止Catalyst交换机在启用PortFast特性的接口上发送BPDU。

1.BPDU Filter有两种配置方式：全局下配置，接口下配置

（1）如果在全局下配置，PortFast端口将不发送任何BPDU，当端口在接收到任何BPDU的时候，将丢弃PortFast和BPDU Filter特性，改回正常的STP操作

（2）如果在接口下配置，PortFast端口将不发送任何BPDU，当端口在接收到任何BPDU的时候，丢弃BPDU

2.配置命令

Switch(config)# spanning-tree portfast bpdufilter default /---启用了Port Fast特性的端口才具备BPDU Filtering---/

Switch(config-if)# spanning-tree bpdufilter enable /---在不启用Port Fast特性的情况下也具备BPDU Filtering---/

3.BPDU Guard和BPDU Filter同时使用，BPDU Filter有效，而防护无效，因为过滤的优先级高于防护的优先级

4.BPDU Filter使用的并不多,而且不推荐使用

5.BPDU Guard和BPDU Filter是对PortFast端口的增强

6.show spanning-tree summary totals

根据前面所说的，我们防护的根本就是不让终端端口接上交换机这类的设备，那么现在我们只需要将这个接口设置为不能连接交换机就可以了。而STP是一种用来在交换机之间的协议，我们可以通过不让其发送BPDU，这样即使你接上了交换机也是没有用的。实现的方法是在接口下输入spanning-tree bpduFilter enable，此时当接口再收到BPDU包的时候，就会直接将BDUP包丢弃。

**3、关于Root Guard**

这项功能主要是为了防止网络中重新选举根交换的，我们所面临的威胁主要是在终端接口上，所以这里就把所有的终端接口全部强制的设备为指定接口，这样就保护了根交换机，不管你接进来的设备的优先权有多少，你都没有资格参与根交换的选举了。

1.**根防护特性能够强制让接口成为指定端口**，进而能够防止周围的交换机成为根交换机。防止新加入的交换机(有更低根网桥ID)影响一个已经稳定了（已经存在根网桥）的交换网络,阻止未经授权的交换机成为根网桥。

![%E9%92%88%E5%AF%B9%E4%BA%8E%E7%94%9F%E6%88%90%E6%A0%91%E7%9A%84%E6%94%BB%E5%87%BB%EF%BC%88Spanning%20Tree%20Attack%EF%BC%89%20ef3ddb1b583047da8fd137f703084826/image2.png](针对于生成树的攻击（Spanning%20Tree%20Attack）/image2.png)

2.工作原理：当一个端口启动了此特性，当它收到了一个比根网桥优先值更优的BPDU包，则它会立即阻塞该端口，使端口变成root inconsistent状态（等效于监听状态），并且不会从这个端口转发流量，使之不能形成环路等情况。这个端口特性是动态的，当没有收到更优的包时，则此端口又会自己变成转发状态了。

3.Root Guard强制该端口成为DP（指定端口），这样，就保证了与该端口相连的新交换机是离根远的交换机，也就保证了新交换机不能成为根。

4.在启用根防护特性的时候，交换机不允许端口成为根端口，而且当端口收到更好的BPDU，那么根防护将禁用（err-disable）端口，而不处理BPDU。

5.建议在接入端口上启用根防护

6.配置命令：

**Switch(config-if)#spanning-tree guard root**

**4、关于loop Guard和UDLD**

这两种功能主要是用在由单向链路产生的环路问题上，关于单向链路，如图三

> 
> 
> 
> 图三
> 

交换机A和B在全双工下传递数据，这时B通向A的链路损坏掉，就造成A可以传给B数据，B也能正常接收，但是B无法向A传递数据，这就是一个单向链路的故障。

![%E9%92%88%E5%AF%B9%E4%BA%8E%E7%94%9F%E6%88%90%E6%A0%91%E7%9A%84%E6%94%BB%E5%87%BB%EF%BC%88Spanning%20Tree%20Attack%EF%BC%89%20ef3ddb1b583047da8fd137f703084826/image4.png](针对于生成树的攻击（Spanning%20Tree%20Attack）/image4.png)

.解决方法：Loop Guard或者UDLD技术

**关于Loop Guard**

接收不到BPDU时，端口阻塞

![%E9%92%88%E5%AF%B9%E4%BA%8E%E7%94%9F%E6%88%90%E6%A0%91%E7%9A%84%E6%94%BB%E5%87%BB%EF%BC%88Spanning%20Tree%20Attack%EF%BC%89%20ef3ddb1b583047da8fd137f703084826/image5.png](针对于生成树的攻击（Spanning%20Tree%20Attack）/image5.png)

该命令使用在根端口和非指定端口上，**当交换机在启用loopguard特性的端口上停止接收BPDU时，交换机将使得端口进入STP“不一致环路”（inconsistentports）阻塞状态，该状态不能传递任何数据流量，当不一致端口再次收到BPDU时，端口将根据BPDU自动过渡到STP状态。**

在以太通道接口的情况下，如果没有收到特定VLAN的BPDU，那么通道组内的所有接口，通道状态都将进入“不一致环路”状态。

环路防护和根防护不能共存于相同的端口，如果启用环路防护特性，那么将以每端口为基础而禁用先前配置的根防护特性。

也可以使用全局命令：Switch(config)# **spanning-tree loopguard default** /---全局启用Loop Guard特性，但交换机只在被认为是点到点链路的端口上启用环路防护特性---/

接口下配置：**spanning-tree guard loop**

查看： show spanning-tree interface *interface* detail

**关于UDLD**

（1）UDLD是一个Cisco私有的二层协议

（2）UDLD监听利用光纤或双绞线连接的以太链路的物理配置

（3）UDLD需要链路两端设备都支持才能正常运行

（4）UDLD支持两种工作模式；普通（normal）模式（默认）和激进（aggressive）模式。

普通（normal）模式：这个模式下，UDLD可以检测到由于端口的误接引起的光纤的单向链路。

激进（aggressive）模式：这个模式下，UDLD可以检测到由于端口的误接引起的光纤的单向链路。并且可以检测到光纤及双绞线链路中的单向链路

补充：它有一个检测的作用：在启用UDLD的时候，交换机定期向邻居发送UDLD协议数据包，并且期望在预定计时器到期之前接收到回应的数据包。如果计时器到期，那么交换机将确定该链路是单向链路，并且将关闭该端口。

UDLD数据包包含：发送端口的设备ID和端口ID，邻居接收设备的设备ID和端口ID。如果邻居也启用UDLD，那么它将发送相同的hello消息，如果链路两侧的设备都接收到对方的UDLD数据包，那么链路就是双向链路。UDLD消息的默认间隔是15s。组播更新:0100.0ccc.cccc

当启用积极模式UDLD时，当端口停止接收UDLD数据包的时候，UDLD将尝试重新建立与邻居的连接。但如果尝试次数超过8次之后，那么端口状态将变为“err-disable”，并禁用端口。

（5）UDLD检测到单向链路后会将接口置为err-disable状态，我们可以用命令errdisable recovery cause udld恢复。也可以通过手动的shutdown和no shutdown来解决。

（6）UDLD的配置

(config)# udld {enable | aggressive}

(config-if)# udld port [aggressive]

Switch# udld reset //重启所有被 UDLD 功能所关闭的接口

> 注：UDLD不能检测软件故障，只能检测硬件故障
>