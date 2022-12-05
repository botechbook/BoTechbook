# H3C交换机端口三种模式区别

H3C交换机端口三种模式区别

2012年5月24日

14:06

实际上数据帧在交换机内部处理时，均带有vlan tag。

a）access端口

发送（从交换机内部往外发送）：

带有vlan tag：删除tag后，发送

不带vlan tag：不可能出现

接收：

带有vlan tag：若该tag等于该access端口的pvid，则可以接收，进入交换机内部

不带vlan tag：添加该access端口的pvid，进入交换机内部

b）trunk端口（允许发送native VLAN数据的时候，可以不加tag）

发送（从交换机内部往外发送）：

带有vlan tag：若tag等于该trunk端口的pvid，则删除tag后发送；否则保留tag直接发送

不带vlan tag：不可能出现

接收：

带有vlan tag：保留该tag，进入交换机内部

不带vlan tag：添加该trunk端口的pvid，进入交换机内部

c）hybrid端口（允许发送多个VLAN数据的时候，可以不加tag）

发送（从交换机内部往外发送）：

带有vlan tag：

是否带tag进行发送，取决于用户配置（用户可以配置tagged list，untagged list）

不带vlan tag：不可能出现

接收：

带有vlan tag：保留该tag，进入交换机内部

不带vlan tag：添加该hybrid端口的pvid，进入交换机内部

在设备上允许trunk和hybrid端口同时存在，但是不能将hybrid端口直接改为trunk端口（hybrid--》access---》trunk），反之亦然。

hybrid端口可以允许多个vlan的数据发送时不带tag，而802.1q的trunk只能是native vlan（即pvid）对应的vlan的数据发送时不带tag，应该说hybrid可以实现trunk端口的特性。实际使用时都可以用hybrid端口，而不用trunk。