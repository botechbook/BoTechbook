# Loop Guard

Loop Guard

2011年7月7日

14:37

> 在交换网络中，当两点之间存在多条冗余链路时，就会因为重复的数据包在网络中传递，引起广播风暴，并且还会造成交换机MAC地址表错误，使网络不稳定，因此造成环路。所以需要借助STP来阻塞网络中两点之间多余的链路，而只留一条活动链路，即为转发状态，其它多余链路变为Blocking状态，当转发状态的链路中断时，再启用Blocking状态的端口。
> 
> 
> 当STP运行时，只有两点之间存在多条冗余链路时，才会阻塞多余链路而只留一条活动链路。如果STP认为两点之间并没有多条链路，也就不会产生环路，那么就不会有端口被Blocking。因为STP在判断两点之间是否有多条链路，是靠发送BPDU，如果从多个端口收到同一台交换机的BPDU，则认为与那个点之间有多条链路，所以会阻塞多余链路而只留一条。如果只从一个端口收到同台交换机的BPDU，或者是没有收到重复BPDU，则认为网络是无环的，也就没有端口被Blocking，其它不需要被Blocking的端口，都会被变为指定端口。
> 

![Loop%20Guard%20f482164a34a048d3b99fc7c275c4b43d/image1.png](Loop%20Guard/image1.png)

在上图中的网络环境中，如果交换机所有端口收发数据的功能正常，则交换机就能够靠收发BPDU来检测出网络中的多余链路，就会将其Block，从而避免环路。但是当网络中出现单向链路故障时，也就是某个端口只能收数据而不能发数据，或者只能发数据而不能收数据，这时网络会出现意想不到的麻烦。如上图，由于SW2的端口F0/21出现单向链路故障，导致从F0/21发出去的数据包能被SW3收到，而SW3发的数据包却不能被SW2收到，此时造成的结果是，SW3认为网络是正常的，又由于SW3拥有更高优先级的Bridge-ID，所以SW3上F0/19为根端口，F0/21为指定端口，SW3上所有端口都是转发状态，而没有Blocking的端口。但是由于SW2不能收到SW3发来的数据包，也就不能从SW3收到BPDU，最终SW2只能从F0/23收到数据包，所以SW2认为网络是无环的，因此做出了一个错误的决定，就是在STP计算结束后，认为网络无环，而将原本应该被Block的端口F0/21变为指定端口，造成SW上F0/23和F0/21同时为转发状态。不难看出，此时，网络中所有的交换机端口都为转发状态，结果如下：

![Loop%20Guard%20f482164a34a048d3b99fc7c275c4b43d/image2.png](Loop%20Guard/image2.png)

最终造成网络中所有的交换机端口都为转发状态，流量在所有端口上被转发，引起广播风暴，出现环路。此结果是非常严重的。

单向链路故障不仅会使Blocking状态的端口错误地变成指定端口，还会造成根端口错误地变成指定端口。

对于上述问题，可以通过Loop Guard来解决，开启了Loop Guard的端口在收不到BPDU的情况下，并不会认为网络是无环的，并不会错误地将端口变成指定端口，而是将收不到BPDU的端口变成loop-inconsistent状态，此状态等同于blocking状态。

Loop Guard可以全局开启，也可以在接口下开启，但不建议在全局开启，请在相应接口下开启。什么端口最需要开，很明显，当然是被blocking的端口，但并不完全正确，准确答案是在所有非指定端口开启，其实就是根端口和blocking端口。

当在接口开启后Loop Guard，接口所在的所有VLAN都会生效，如果是接口是trunk，哪个VLAN没有收到BPDU，接口就会在哪个VLAN被blocking。在EtherChannel上是对整条生效。

只有交换机上的blocking端口和根端口才需要开启Loop Guard。如果一个网络中所有交换机没有blocking的端口，就表示此网络无环，所以就不需要开Loop Guard。并且根交换机上所有端口都是指定端口，所以在根上开Loop Guard是没有意义的。

**注：**

★PortFast的接口不能开启Loop Guard。

★Root guard和Loop Guard不能同时开。

★Root guard支持PVST+,，rapid PVST+， MSTP。

**配置**

![Loop%20Guard%20f482164a34a048d3b99fc7c275c4b43d/image1.png](Loop%20Guard/image1.png)

**1.开启Loop Guard**

**（1）在SW2的根端口与Blocking端口开启Loop Guard**

sw2(config)#int f0/21

sw2(config-if)#spanning-tree guard loop

sw2(config)#int f0/23

sw2(config-if)#spanning-tree guard loop

**说明：**在所有根端口与Blocking端口开启Loop Guard

**2.查看Loop Guard**

**(1)查看开启了Loop Guard的端口**

sw2#sh spanning-tree detail

（输出被省略）

Port 21 (FastEthernet0/21) of VLAN0001 is blocking

Port path cost 19, Port priority 128, Port Identifier 128.21.

Designated root has priority 16385, address 007d.618d.0300

Designated bridge has priority 24577, address 0013.8065.bd80

Designated port id is 128.21, designated path cost 19

Timers: message age 3, forward delay 0, hold 0

Number of transitions to forwarding state: 0

Link type is point-to-point by default

Loop guard is enabled on the port

BPDU: sent 3, received 3917

（输出被省略）

sw2#

**说明：**可以看到，F0/21已经开启Loop Guard

**3.测试Loop Guard**

**(1)过滤掉SW3从F0/21发往SW2的BPDU**

sw3(config)#int f0/21

sw3(config-if)#spanning-tree bpdufilter enable

**说明：**让SW2开启了Loop Guard的端口F0/21收不到BPDU。

**（2）查看SW2的Loop Guard状态**

当SW2开启了Loop Guard的端口收不到BPDU时，会有如下提示：

sw2#

02:16:28: %SPANTREE-2-LOOPGUARD_BLOCK: Loop guard blocking port FastEthernet0/21 on VLAN0001.

sw2#

**（3）查看被放入inconsistent (blocked) 状态的端口：**

sw2#sh spanning-tree inconsistentports

Name                 Interface              Inconsistency

- ------------------- ---------------------- ------------------

VLAN0001             FastEthernet0/21       Loop Inconsistent

Number of inconsistent ports (segments) in the system : 1

sw2#

**说明：**由于端口F0/21开启了Loop Guard，所有在收不到BPDU时，此端口被放入inconsistent (blocked) 状态的端口。