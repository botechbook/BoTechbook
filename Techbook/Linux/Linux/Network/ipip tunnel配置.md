# ipip tunnel配置

ipip tunnel配置

Wednesday, October 25, 2017

11:49 AM

简记

ip add add 2.2.2.2/32 brd 2.2.2.2 dev tunl0

ip link set tunl0 up

Ipv6 mode

ip -6 add add 2001::2:2:2:2/96 dev ip6tnl0

ip link set ip6tnl0 up

以下两种方式，选一种

(1) 这种方式，其他的接口rp_filter值都为1

echo 2 > /proc/sys/net/ipv4/conf/tunl0/rp_filter

(2)

sysctl net.ipv4.conf.all.rp_filter=0

sysctl net.ipv4.conf.eth1.rp_filter=0

sysctl net.ipv4.conf.tunl0.rp_filter=0

- --------------------------------

默认情况下，系统应该是有个隐藏的tunl0 接口

如果用命令

ip tunnel add abc10 mode ipip remote any

会报错

说已经存在tunl0 了

ip -6 tunnel add ip6abc10 mode ip6ip6 remote any

会报错

说已经存在ip6tnl0

但执行过之后，再查看

ip tunnel show

能看到

root@NxLinux:~# ip tunnel show

tunl0: ip/ip remote any local any ttl inherit nopmtudisc

这时再通过ip add 和 ip link 命令都是能看到这个接口的了

如果remote不是any的tunnel可以继续创建：

ip tunnel add mytunnel100 mode ipip remote 1.1.1.1

其他的tunnel都可以删除，唯独tunl0删不掉

删除tunnel命令

ip tunnel delete mytunnel100

或者更简单的办法，在一开始看不见tunl0的时候，直接：

ip add add 2.2.2.2/32 brd 2.2.2.2 dev tunl0

ip link set tunl0 up # 千万别忘了开启这个接口

或者老命令

ifconfig tunl0 192.168.1.110 netmask 255.255.255.255 broadcast 192.168.1.110