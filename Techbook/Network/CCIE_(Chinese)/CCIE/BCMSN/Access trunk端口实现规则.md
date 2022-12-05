# Access trunk端口实现规则

Access/trunk端口实现规则

2012年4月28日

9:19

Access端口的报文收发规则如下：

Access端口在收到一个报文（**Access端口通常是从终端PC中接收报文**）后，先判断该报文中是否有VLAN标记信息：如果没有VLAN标记，则打上该Access端口的PVID后继续转发（**毕竟Access端口收到报文后是向其他端口发送的，可以识别带有VLAN标记的报文**）；如果有VLAN标记（**这个报文肯定是来自其他非Access端口和终端PC，因为Access端口和终端PC网卡不会发送带VLAN标记的报文**），则默认直接丢弃（国产厂商默认行为，在Cisco设备上需要开启BPDU guard和port-fast等）。

Access端口上发送报文时，会先将报文中的VLAN信息去掉（**因为Access端口发送报文一般是到终端PC，PC中的网卡是不能识别VLAN标记的。还有一种情况是发送到另一个同VLAN中的Access端口，因为Access端口也不接受带有VLAN标记的报文**），然后再直接发送，所以Access端口发出去的报文都是不带VLAN标记的。表4-1是根据上面介绍的Access端口接收或发送报文规则而例举的示例（表中的VLAN 2、VLAN 3只是其中的两个VLAN例，实际上可为其他任意已激活的VLAN）。

![Access%20trunk%E7%AB%AF%E5%8F%A3%E5%AE%9E%E7%8E%B0%E8%A7%84%E5%88%99%206f51fbed33fb4b02b53214f0f14a5e19/image1.jpg](Access%20trunk端口实现规则/image1.jpg)

Trunk端口的报文收发规则如下：

在Trunk端口上发送报文时，先会将要发送报文的VLAN标记与Trunk端口的PVID进行比较，**如果与PVID相等，则从报文中去掉VLAN标记再发送；如果与PVID不相等，则直接发送**。这样一来，如果将交换机级连端口都设置为Trunk，并允许所有VLAN通过后，默认情况下除VLAN 1外的所有来自其他VLAN中的报文将直接发送（因为这些VLAN不是Trunk端口的默认VLAN），而作为Trunk端口默认VLAN的VLAN 1，则需要通过去掉报文中的VLAN信息后再发送。

在Trunk端口收到一个报文时，会首先判断是否有VLAN信息：**如果没有VLAN标记，则打上该Trunk端口的PVID，视同该帧是来自PVID所对应的VLAN转发到PVID所对应的VLAN接口上；如果有VLAN标记，判断该Trunk端口是否允许该VLAN的报文进入，如果允许则直接转发，否则丢弃**。

表4-2是根据上面介绍的Trunk端口接收或发送报文规则而例举的示例（表中的VLAN 2、VLAN 3只是其中的两个VLAN例，实际上可为其他任意已激活的VLAN）。

![Access%20trunk%E7%AB%AF%E5%8F%A3%E5%AE%9E%E7%8E%B0%E8%A7%84%E5%88%99%206f51fbed33fb4b02b53214f0f14a5e19/image2.jpg](Access%20trunk端口实现规则/image2.jpg)

下面通过一个因PVID设置不当造成的网络故障的排除方法来加深对Access和Trunk端口数据收发规则的理解。图4-1中，SW1与R1之间，SW1和SW2之间的连接链路都是Trunk链路，允许网络中所有VLAN的数据通过。并设置SW1的f0/2 Trunk接口的PVID=1，SW2的f0/1 Trunk接口的PVID=2，PC2~5各自属于自己的VLAN，为Access端口。现只有PC2无法上网。

![Access%20trunk%E7%AB%AF%E5%8F%A3%E5%AE%9E%E7%8E%B0%E8%A7%84%E5%88%99%206f51fbed33fb4b02b53214f0f14a5e19/image3.jpg](Access%20trunk端口实现规则/image3.jpg)

图4-1 Access和Trunk端口收发规则解析示例

这时我们首先分析一下PC2在上网时发送的数据帧流程：首先PC2是向所连接的Access端口发送不带VLAN标记的帧，所连的Access端口接收到这个帧后打开它所属的VLAN 2的标记转发到达SW2的f0/1 Trunk端口，经过比较发现所收到的数据帧的VLAN标记（2）与SW2的f0/1 Trunk端口的PVID（2）一样，所以此时SW2的f0/1 Trunk端口会为把这个数据帧去掉VLAN标记转发到SW1的f0/2 Trunk端口。此时因为SW1的f0/2 Trunk端口收到的数据包没有VLAN标记，则直接把它打上与SW1的f0/2 Trunk端口PVID（1）对应的VLAN 1标记，然后错误地把它转发到VLAN 1所对应的VLAN接口上，所以造成PC2不能上网。

现在再来看一下其他几台机为什么能正常上网，以PC3为例。

PC3连接的也是SW2上的一个Access端口，发送的帧也是不带标记的，所连的Access端口接收到这个帧后打开它所属的VLAN 3的标记转发到达SW2的f0/1 Trunk端口，经过比较发现所收到的数据帧的VLAN标记（3）与SW2的f0/1 Trunk端口的PVID不一样，所以此时SW2的f0/1 Trunk端口会为直接转发这个数据帧到SW1的f0/2 Trunk端口。SW1的f0/2 Trunk端口再比较自己的PVID（1）与所收到的数据帧VLAN 标记（3），发现不一样，直接转发，所以PC3是能上网。其他的PC4、PC5与PC3的数据发送流程是一样。

从以上分析可以看出，造成PC2不能上网的根本原因就在于从访问端口发送的数据帧的VLAN标记与SW2的f0/1 Trunk端口的PVID（2）一样，所以造成转发后的数据帧是不带VLAN标记的，最后被SW1的f0/2 Trunk端口错误地把这些数据帧直接转发到了它所属的VLAN中，而不是正确地发到对应的VLAN中。这时如果把SW2的f0/1 Trunk端口的PVID设置成其他PC机在VLAN的VLAN ID，则对应的VLAN中的PC机就不能上网了。所以在这种情况下，只有把SW2的f0/1 Trunk端口的PVID设置不包括网络中PC机所在VLAN的VLAN ID（本示例中如设置为1）就可以确保各VLAN中的PC都可以上网。这样就可以得出这样一条经验：要确保网络中所有VLAN用户都能上网，则需要把Trunk端口的PVID设置成非上网用户所在VLAN的VLAN ID。