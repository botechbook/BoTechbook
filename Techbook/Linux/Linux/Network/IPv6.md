# IPv6

IPv6

2014年10月24日

16:03

加载IPv6模块

# modprobe ipv6

（#insmod ipv6 //添加ipv6模块另一种方法）

查看ipv6模块是否被加载

1 直接ifconfig，看是否有ipv6地址

2 lsmod | grep ipv6 看看是否有ipv6的模块被加载

在网卡文件中加入如下行

IPV6INIT=yes

IPV6ADDR=2001:da8:8003:801:202:120:1:1

手工即使添加IPv6地址：

ifconfig eth2 add 2001::10.77.1.4/112

/etc/sysconfig/network 中必须：

NETWORKING=yes

HOSTNAME=chris

NETWORKING_IPV6=yes

~

记得关掉ipv6的防火墙：ip6tables

route -A inet6 add / gw [dev ]

例子：

route -A inet6 add 2001::10.78.0.0/112 dev eth1

route -A inet6 add 2001::10.78.0.0/112 gw 2001::10.78.3.60

查看ipv6路由：

route -A inet6 -n //-n是以数字形式显示

添加永久路由

/etc/sysconfig/static-routes-ipv6 #没有手动创建

#Device                Route                        Gateway

eth0 2002:470::/48 2002:480::1