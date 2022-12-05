# 介绍Native Vlan

介绍Native Vlan

2012年12月21日

16:38

Native Vlan（本征VLAN）和其他Vlan的另外一个区别在于：非Native Vlan在trunk中传输数据时要被添加Vlan标记的（如dot1q或者isl），但是native vlan在trunk中传输数据时是不进行标记的。

在trunk链路上，如果switchport trunk allowed vlan all，那么所有带有vlan信息的帧都允许通过，如果配置了只允许特定vlan通过，那么只有native vlan 、和特定vlan的帧才能通过，默认native vlan 是vlan 1，有些情况下trunk出问题了，只能vlan 1的信息才能通过，vlan 1是管理vlan， 当然你也可以通过命令修改native vlan为vlan 2或者vlan 3，

命令：

Switch(config-if)#switchport trunk native vlan vlanID

Switch#show interfaces f0/24 switchport

所有的帧在trunk中都是打上标记的，也就是tag，不同点在于，如果帧在进入trunk以前已经打上标记了，比如vlan 2的标记，并且trunk又允许vlan 2通过的话，该vlan 2的帧就通过，反之丢弃。 另外如果帧在进入trunk时是没有标记的，那么trunk就会给他打上native vlan的标记，该帧在trunk中就以native vlan的身份传输，native vlan 是用于trunk 口的， 在access口没有native vlan的概念。

**在一些协议中, 如STP, 交换机之间是要互相协商通讯的， 如果对STP的数据包打了tag的话， 会导致一些不支持VLAN的在交换机不能相互协商。为了解决这个问题, 提出native vlan的概念. 在trunK中, 对于没有带tag的流入数据, 在交换机中打下native vlan id, 流出时, 当发现tag是该端口的native vlan ID,去掉tag转发.**

对于支持pvlan的交换机。每个端口都有一个pvid(PVID是不分trunk 口或access口), 缺省跟该端口的VLAN ID一样，对设置成trunk口的端口, pvid 等于 native vlan ID