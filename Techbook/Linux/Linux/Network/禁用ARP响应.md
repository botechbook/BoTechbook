# 禁用ARP响应

禁用ARP响应

2014年10月24日

16:05

echo 1 > /proc/sys/net/ipv4/conf/eth0/arp_ignore

echo 2 > /proc/sys/net/ipv4/conf/eth0/arp_announce

在/proc/sys/net/ipv4/conf/ 下可以发现类似 all,eth0,eth1,default,lo 等网络接口界面,每一个都是目录,他们下属的文件中,每个文件对应该界面下某些可以设置的选项设置.(all/是特定的，用来修改所有接口的设置, default/ 表示缺省设置,lo/表示本地接口设置,eth0/表示第一块网卡,eth1/表示第2块网卡.注意:下面有的参数,是需要all和该界面下同时为 ture才生效,而某些则是只需要该界面下为true即可,注意区别!!)

____________________________________________________________________________________________________

arp_announce=2

无论内部哪个IP使用arp请求外部地址，都将出站请求源IP替换为出站设备IP

（LVS-DR模型中，意思是vip向client转发数据包，需要知道交换机mac地址，但RS有多个，都使用相同vip解析交换机mac是有问题的，所以该值是将RS请求交换机的arp信息，源ip转换成出站，即RIP的地址。注意：这里的转换仅针对arp，RS向client发送数据包时依然使用VIP）

（默认为0，内部哪个IP做出的请求，数据包源IP即为哪个，不转换成与外部相连网卡IP）

arp_ignore=1

只响应外部设备对相连网卡IP的请求，对非相连IP的请求不予回应

（默认为0，回应任何网络接口上对任何本地IP地址的arp查询请求）

Linux 官方内核自2.6.4和2.4.26开始，interface上的arp_announce/arp_ignore系统调用就可用了。下面是内核文档中关于arp_announce/arp_ignore的描述:

arp_announce - INTEGER

Define different restriction levels for announcing the local source IP address from IP packets in ARP requests sent on interface:

0 - (default) Use any local address, configured on any interface

1 - Try to avoid local addresses that are not in the target's subnet for this interface. This mode is useful when target hosts reachable via this interface require the source IP address in ARP requests to be part of their logical network configured on the receiving interface. When we generate the request we will check all our subnets that include the target IP and will preserve the source address if it is from such subnet. If there is no such subnet we select source address according to the rules for level 2.

2 - Always use the best local address for this target.       In this mode we ignore the source address in the IP packet and try to select local address that we prefer for talks with the target host. Such local address is selected by looking for primary IP addresses on all our subnets on the outgoing interface that include the target IP address. If no suitable local address is found we select the first local address we have on the outgoing interface or on all other interfaces, with the hope we will receive reply for our request and even sometimes no matter the source IP address we announce. The max value from conf/{all,interface}/arp_announce is used. Increasing the restriction level gives more chance for receiving answer from the resolved target while decreasing the level announces more valid sender's information.

arp_ignore - INTEGER

Define different modes for sending replies in response to received ARP requests that resolve local target IP addresses:

0 - (default): reply for any local target IP address, configured on any interface

1 - reply only if the target IP address is local address configured on the incoming interface

2 - reply only if the target IP address is local address configured on the incoming interface and both with the sender's IP address are part from same subnet on this interface

3 - do not reply for local addresses configured with scope host, only resolutions for global and link addresses are replied

4-7 - reserved

8 - do not reply for all local addresses

The max value from conf/{all,interface}/arp_ignore is used when ARP request is received on the {interface}

Disable ARP for VIP

To disable ARP for VIP at real servers, we just need to set arp_announce/arp_ignore sysctls at the interface connected to the VIP network. For example, real servers have eth0 connected to the VIP network with the VIP at interface lo, we will have the following commands.

echo 1 > /proc/sys/net/ipv4/conf/eth0/arp_ignore

echo 2 > /proc/sys/net/ipv4/conf/eth0/arp_announce

Or, if /etc/sysctl.conf is used in the system, we have this config in /etc/sysctl.conf

net.ipv4.conf.eth0.arp_ignore = 1

net.ipv4.conf.eth0.arp_announce = 2

Note that the arp_announce/arp_ignore sysctls must be setup correctly, before the VIPaddress is brought up at a logical interface at real servers.

arp_announce :INTEGER 不同取值表示对网络接口上本地IP地址发出的ARP请求作出相应级别的限制：相关代码在 默认为0

确定不同程度的限制,宣布对来自本地源IP地址发出Arp请求的接口

0 - (默认) 在任意网络接口上的任何本地地址

1 -尽量避免不在该网络接口子网段的本地地址. 当发起ARP请求的源IP地址是被设置应该经由路由达到此网络接口的时候很有用.此时会检查来访IP是否为所有接口上的子网段内ip之一.如果该来访IP 不属于各个网络接口上的子网段内,那么将采用级别2的方式来进行处理.

2 - 对查询目标使用最适当的本地地址.在此模式下将忽略这个IP数据包的源地址并尝试选择与能与该地址通信的本地地址.首要是选择所有的网络接口的子网中外出 访问子网中包含该目标IP地址的本地地址. 如果没有合适的地址被发现,将选择当前的发送网络接口或其他的有可能接受到该ARP回应的网络接口来进行发送；

当内网的机器要发送一个到外部的ip包，那么它就会请求路由器的Mac地址，发送一个arp请求，这个arp请求里面包括了自己的ip地址和Mac地址， 而linux默认是使用ip的源ip地址作为arp里面的源ip地址，而不是使用发送设备上面的，如果设置 arp_announce 为2，则使用发送设备上的ip。

arp_ignore : INTEGER 定义对目标地址为本地IP的ARP询问不同的应答模式，相关代码在arp_announce函数中 默认为0

0 - (默认值): 回应任何网络接口上对任何本地IP地址的arp查询请求（比如eth0=192.168.0.1/24,eth1=10.1.1.1/24,那么即使 eth0收到来自10.1.1.2这样地址发起的对10.1.1.1 的arp查询也会回应--而原本这个请求该是出现在eth1上，也该由eth1回应的）

1 - 只回答目标IP地址是来访网络接口本地地址的ARP查询请求（比如eth0=192.168.0.1/24,eth1=10.1.1.1/24,那么即使 eth0收到来自10.1.1.2这样地址发起的对192.168.0.1的查询会回答，而对10.1.1.1 的arp查询不会回应）

2 -只回答目标IP地址是来访网络接口本地地址的ARP查询请求,且来访IP必须在该网络接口的子网段内（比如 eth0=192.168.0.1/24,eth1=10.1.1.1/24,eth1收到来自10.1.1.2这样地址发起的对192.168.0.1 的查询不会回答，而对192.168.0.2发起的对192.168.0.1的arp查询会回应）

3 - 不回应该网络界面的arp请求，而只对设置的唯一和连接地址做出回应(do not reply for local addresses configured with scope host,only resolutions for global and link addresses are replied )

4-7 - 保留未使用

8 -不回应所有（本地地址）的arp查询