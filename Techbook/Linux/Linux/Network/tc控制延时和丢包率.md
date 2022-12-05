# tc控制延时和丢包率

tc控制延时和丢包率

2014年10月24日

16:11

Linux下用tc控制网络延时和丢包率 流量控制

linux下的tc可以操纵网络，比如分配带宽给不同的应用、模拟网络时延、模拟糟糕网络环境下的丢包等。

tc中间需要用一个路由器。使用 tc 当中间的路由器，来接二个网卡,然后打开路由功能来测试。

于是我们拿一台linux机当router，单网卡，两个虚拟ip，让它连接两台服务器再试。更滑稽了，tc不起作用，两台服务器间的流量刷刷的走，tc却显示没有多少packet经过。tc不能用于router吗？

后来看了tc的详细手册（注意4.1节），终于知道了：tc标准用法是两台服务器中间一个双网卡的router，在router上用tc。

最后测试成功。丢包率越高，tcp传输的速度越慢；如果丢包率很高，tcp可能会顿住，但是只要改回去（去掉tc的netem配置），传输就会恢复。

tc修改网络延时：

sudo tc qdisc add dev eth0 root netem delay 1000ms

删除策略：

sudo tc qdisc del dev eth0 root netem delay 1000ms

tc -d qdisc //查看实施的策略

验证效果：

PING myhost (192.168.0.2) 56(84) bytes of data.

64 bytes from myhost (192.168.0.2): icmp_seq=1 ttl=64 time=1000 ms

64 bytes from myhost (192.168.0.2): icmp_seq=1 ttl=64 time=1000 ms

64 bytes from myhost (192.168.0.2): icmp_seq=1 ttl=64 time=1000 ms

修改丢包率：

sudo tc qdisc add dev eth0 root netem loss 10%

删除策略：

sudo tc qdisc del dev eth0 root netem loss 10%