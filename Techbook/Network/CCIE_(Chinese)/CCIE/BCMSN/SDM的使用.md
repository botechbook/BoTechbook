# SDM的使用

SDM的使用

2011年9月23日

16:32

SDM(Security Device Manager)是Cisco公司提供的全新图形化路由器管理工具。该工具利用WEB界面、Java技术和交互配置向导使得用户无需了解命令行接口(CLI)即可轻松地完成IOS路由器的状态监控、安全审计和功能配置--甚至连QoS、Easy VPN Server、IPS、DHCP Server、动态路由协议等令中级技术人员都头疼的配置任务也可以利用SDM轻松而快捷地完成，配置逻辑严密、结构规范，真是令人震惊。使用SDM进行管理时，用户到路由器之间使用加密的HTTP连接及SSH v2协议，安全可靠。目前Cisco 的大部分中低端路由器包括8xx, 17xx, 18xx, 26xx(XM), 28xx, 36xx, 37xx, 38xx, 72xx, 73xx等型号都已经可以支持SDM。

要支持SDM管理，路由器必须进行以下配置：

ip http server //允许web接口

ip https server

ip http authentication local

ip http timeout-policy idle 600 life 86400 request 10000   //修改web接口超时参数

user chris privilege 15 secret 0 chris   //必须是secret，不能用password关键字

line vty 0 4

login local

transport input telnet ssh //允许telnet和ssh

SDM程序既可以安装在PC上，也可以安装在路由器上。安装在PC上能节约路由器的内存并且可以它来管理其他支持SDM管理的路由器，但是由于IE默认禁止网页访问本机资源，需要修改IE的安全设置。安装到路由器时基本安装需要大约4M Flash空间，组件Cisco SDM Express(需要1.5M Flash)只用于路由器的初始化配置，无须安装。

- *******************************************

记得将Internet选项中高级选项卡的“允许活动内容在我的计算机上的文件中运行*”

- *******************************************