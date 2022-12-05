# 配置PPPOE

配置PPPOE

2013年1月4日

9:09

ADSL配置（和家里的猫的功能相同）：

1）开启虚拟拨号功能

vpdn enable

2）开启接口的PPPOE功能

int fa1/0 这个是物理上对外的接口，即连接了ISP的DLAM设备，实际上应该是电话线。

pppoe enable

pppoe-client dial-pool-number 1 (关联和客户的 dialer pool 1 进程号)

no shut

3）创建拨号接口 （这个是对外的虚拟接口）

int dialer 0 客户端的ADSL使用的是dialer虚拟拨号，和电信的模板是相对的。

en ppp 封装PPP

ip address negotiated 地址协商

dialer pool 1 与前边物理接口下的号码对应，关联fa1/0接口

ppp chap hostname cisco 配置用于拨号的名称，这个要与上面DSLAM的配置对应

ppp chap password cisco 配置拨号的密码，这个要与上面DSLAM的配置对应

ppp ipcp dns request accept 向ISP请求不是全0的dns地址

ip nat outside

no shut

4）设置DHCP，这个DHCP是用户内部用户的。

server dhcp

no ipdhcp conflict logging

ip dhcp excluded-address 192.168.1.1

ip dhcp pool DHCP

network 192.168.1.0/24

import all 如果DNS有变化，那么就自搜索DNS服务器

5）设置内部物理接口：

int fa0/0 （这是内网的物理接口）

ip add 192.168.1.1 255.255.255.0

ip nat inside

no shut

6）设置NAT功能：

ac 10 per 192.168.1.0 0.0.0.255

ip nat inside source list 10 interface dialer 0 overload

7）指一条默认路由

ip route 0.0.0.0 0.0.0.0 dialer 0 指一条路由，为内网的用户服务。