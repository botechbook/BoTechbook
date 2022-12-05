# IP Source Tracker

IP Source Tracker

2011年8月2日

22:15

此功能是让路由器能够收集网络中可能正在遭受DOS攻击的主机，并且记录攻击源，创建必要的描述DOS攻击易用的信息，可以跟踪多个IP。

记录日志的时间间隔是可以随意定义的，定义的最大主机数量也是可以定义的，并且这些信息全部可以输出到远程服务器，如GRP和 RSP，也只有高端系列75，12000才支持。

**配置**

**1.配置跟踪的主机，可以配置多个主机。**

r1(config)#ip source-track 100.10.0.1

**2.配置产生日志的间隔，单位为分**

r1(config)#ip source-track syslog-interval 2

**3.阶段配置输出的时间间隔**

r1(config)#ip source-track export-interval 60

**4.配置最多记录的地址数量**

r1(config)#ip source-track address-limit 3