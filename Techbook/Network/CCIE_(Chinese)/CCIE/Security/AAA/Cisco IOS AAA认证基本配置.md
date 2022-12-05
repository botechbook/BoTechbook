# Cisco IOS AAA认证基本配置

Cisco IOS AAA认证基本配置

2011年8月2日

21:45

Cisco IOS AAA认证基本配置

在Cisco IOS中配置AAA认证的过程不算复杂，主要步骤如下：

步骤1、全局开启AAA服务。

要使用AAA，就必须使用aaa new-model全局配置命令启用AAA服务。

Router(config)# aaa new-model

步骤2、配置ACS服务器的地址和AAA client密码，其命令格式如下：

AAA Client和AAA Server之间使用TACACS+协议时：

tacacs-server host IP_address key *key*

AAA Client和AAA Server之间使用RADIUS协议时：

radius-server host IP_address key *key*

步骤3、配置Cisco Secure ACS服务器。

在ACS导航条中选择“Network Configuration”，点击右边栏的“Add Entry”进入以下界面

![Cisco%20IOS%20AAA%E8%AE%A4%E8%AF%81%E5%9F%BA%E6%9C%AC%E9%85%8D%E7%BD%AE%204cf1e3e45fb54913a706d1bdedf5c64a/image1.png](Cisco%20IOS%20AAA认证基本配置/image1.png)

如上图所示，在“AAA Client Hostname”处填入AAA客户端的名称，在“AAA client IP Address”处填入AAA客户端的地址，在“key”处填入AAA客户端的密码，在“authentication Using”处选择该客户端所使用认证协议，最后点击“Submit + Restart”完成服务器设置。

![Cisco%20IOS%20AAA%E8%AE%A4%E8%AF%81%E5%9F%BA%E6%9C%AC%E9%85%8D%E7%BD%AE%204cf1e3e45fb54913a706d1bdedf5c64a/image2.jpg](Cisco%20IOS%20AAA认证基本配置/image2.jpg)

Router(config)#aaa authentication login default local

Router(config)#aaa authentication login ex1 group tacacs+

Router(config)#aaa authentication login ex2 enable

Router(config)#aaa authentication login ex3 group tacacs+ none

Router(config)#aaa authentication login ex4 group tacacs+ local

Router(config)#line vty 0

Router(config-line)#login authentication ex1

Router(config-line)#exit

使用AAA在Cisco IOS中对用户可使用的命令进行授权

Cisco Secure ACS支持IOS命令的授权，它可以限制管理用户所能够使用的命令以及命令参数。下面，我们使用一个示例来说明如何配置IOS命令的授权。

![Cisco%20IOS%20AAA%E8%AE%A4%E8%AF%81%E5%9F%BA%E6%9C%AC%E9%85%8D%E7%BD%AE%204cf1e3e45fb54913a706d1bdedf5c64a/image3.png](Cisco%20IOS%20AAA认证基本配置/image3.png)

如上图所示，管理员希望使用ACS实现以下功能：

普通管理员（等级15）只能使用“show ip route”、“show interface”命令查看设备的基本信息，并且无法进入配置模式对设备的配置进行修改；超级管理员（等级15）可以使用所有命令。

第一步：在IOS设备上启动AAA，并且配置AAA认证（授权之前必须先通过认证）。

Router(config)# aaa new-model

Router(config)# username cisco password cisco

Router(config)# tacacs-server host 10.1.1.2 key cisco

Router(config)# aaa authentication login **default** group tacacs+ local

第二步：在ACS管理页面上点击“Network Configuration”，添加一个AAA client，地址为10.1.1.1，key为cisco，协议使用TACACS +，最后点击“Submit + Restart”完成设置

![Cisco%20IOS%20AAA%E8%AE%A4%E8%AF%81%E5%9F%BA%E6%9C%AC%E9%85%8D%E7%BD%AE%204cf1e3e45fb54913a706d1bdedf5c64a/image4.png](Cisco%20IOS%20AAA认证基本配置/image4.png)

第三步：点击“group setup”，将“group 1”重命名为“normal”，将“group 2”重命名为“super”。

第四步：点击“user setup”添加用户test1和test2，其中test1属于“normal”组，test2属于“super”组。

![Cisco%20IOS%20AAA%E8%AE%A4%E8%AF%81%E5%9F%BA%E6%9C%AC%E9%85%8D%E7%BD%AE%204cf1e3e45fb54913a706d1bdedf5c64a/image5.png](Cisco%20IOS%20AAA认证基本配置/image5.png)

第五步：在IOS设备上配置命令授权。

Router(config)# aaa authorization exec default group tacacs+ local

Router(config)# aaa authorization commands 1 default group tacacs+ none ！对等级1的命令进行授权

Router(config)# aaa authorization commands 15 default group tacacs+ none ！对等级15的命令进行授权

第六步：在Cisco Secure ACS的“group setup”中按照要求设置组的权限。 点击“group setup”，选择“normal”组，点击“Edit Settings”。

![Cisco%20IOS%20AAA%E8%AE%A4%E8%AF%81%E5%9F%BA%E6%9C%AC%E9%85%8D%E7%BD%AE%204cf1e3e45fb54913a706d1bdedf5c64a/image6.png](Cisco%20IOS%20AAA认证基本配置/image6.png)

如上图所示，在TACACS +选项组中选择“shell（exec）”，并且将“privilege Level”设置为

![Cisco%20IOS%20AAA%E8%AE%A4%E8%AF%81%E5%9F%BA%E6%9C%AC%E9%85%8D%E7%BD%AE%204cf1e3e45fb54913a706d1bdedf5c64a/image7.png](Cisco%20IOS%20AAA认证基本配置/image7.png)

如上图所示，在“Shell Command Authorization Set”中设置该组所能执行的命令以及参数，最后点击“Submit + Restart”。

“super”组的权限设置和“normal”组基本类似，唯独不同的就是“Shell Command Authorization Set”部分，下图显示了normal组的“Shell Command Authorization Set”设置

![Cisco%20IOS%20AAA%E8%AE%A4%E8%AF%81%E5%9F%BA%E6%9C%AC%E9%85%8D%E7%BD%AE%204cf1e3e45fb54913a706d1bdedf5c64a/image8.png](Cisco%20IOS%20AAA认证基本配置/image8.png)