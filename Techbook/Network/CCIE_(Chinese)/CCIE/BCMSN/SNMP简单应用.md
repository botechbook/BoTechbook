# SNMP简单应用

SNMP简单应用

2011年9月23日

16:33

目前SNMP仍然是监视网络设备（包括Cisco路由器和交换机）性能的流行方法。通过SNMP

管理站点，管理员可以查看网络设备性能的图表。另外，Cisco网络设备还会将报警信息 (称

作 traps)发送到管理站点。

什么是SNMP?

SNMP分为三个版本：v1, v2, 和 v3。其功能是依次递增的。很多网络管理员喜欢用V2

版，但是V3版本可以提供更多的安全特性。

那么SNMP是怎么工作的呢？ SNMP设备包含了一个配制好的SNMP代理。网络管理系统

(NMS)会与每个网络设备上的SNMP代理进行对话。

NMS可以是一个很大的系统，比如HP OpenView，也可以是一个小巧的工具软件，比如

PRTG。

SNMP如何帮助我？

SNMP可做的工作很多，比如以下几类：

1 以图表的方式显示 Cisco路由器/交换机的带宽使用情况，可以按端口，数据流向等分类。

2 以图形方式显示网络错误(比如CRC错误).

3 某个端口出现问题时可以发送警告信息给管理员。

是否需要NMS?

作为管理员，一定要有一个NMS来帮助实现SNMP的功能。配置SNMP 本身并不会让你

获得任何信息，你需要配置一个NMS系统来接收，并显示出SNMP的信息。

如何配置SNMP监视？

Cdp run 启用CDP //需要先启用设备的CDP功能

首先，我们需要建立一个识别字符串。识别字符串其实就是访问网络设备的密码。设立一个

良好的识别字符串可以让我们更好的读写网络设备，比如：

snmp-server community chris ro 配置本路由器的只读字串为chris

snmp-server community chris rw 配置本路由器的读写字串为chris

//现在我们的NMS，不论在网络的什么节点，都可以读取（view）以及写入（change）设备

的配置和状态。

snmp-server enable traps 允许路由器将所有类型SNMP Trap发送出去

snmp-server host IP-address-server traps trapcomm 指定路由器SNMP Trap的接收者为10.238.18.17，发送Trap时采用trapcomm作为字串

我们设置路由器或交换机发送SNMP报文到192.168.1.23主机（NMS），并带有设备的识别字符串，以便我们知道是那个设备出现问题了。我们希望设备端口开启或关闭时，或者有人重新启动设备时发送信息给NMS。以下是设置命令：

Router(config)# snmp-server host 192.168.1.23 version 2c MyCommunity972

Router(config)# snmp-server enable traps snmp linkdown linkup coldstart

warmstart

//在Cisco IOS 12.0到12.3版本中，存在SNMP漏洞，因此大家要注意不要使用这些版本

的Cisco IOS。尽可能在安全的前提下进行配置。

snmp-server trap-source loopback0 //将loopback接口的IP地址作为SNMP Trap的发送源地址

配置Cisco设备的SNMP代理

配置Cisco设备上的SNMP代理的步骤如下：

启用SNMP:

configure terminal

snmp-server community rw/ro (example: snmp-server community public ro)

启用陷阱（警告）:

configure terminal

snmp-server enable traps snmp authentication

配置snmp

#conf t

#snmp-server community cisco ro（只读） ；配置只读通信字符串

#snmp-server community secret rw（读写） ；配置读写通信字符串

#snmp-server enable traps ；配置网关SNMP TRAP

#snmp-server host 10.254.190.1 rw ；配置网关工作站地址

查看SNMP状态

Show snmp