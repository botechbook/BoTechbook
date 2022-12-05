# Root Guard

Root Guard

2011年7月7日

14:35

> 以下图为例来解释Root Guard的功能与作用：
> 

![Root%20Guard%209c0ce9467635453db4fbe5993534816d/image1.png](Root%20Guard/image1.png)

在上图中，交换机SW1，SW2与SW3为网络中运行正常的交换机，其中SW1被选为根交换机，当其它交换机之间要通信，都必须选出一个去往根交换机的端口，也就是根端口，所以当SW2与SW3承认SW1为网络中的根交换机时，SW2便将连接SW1的端口F0/23选为根端口，SW3将连SW1的端口F0/19选为根端口，此后网络通信正常。

考虑到网络的合理性与稳定性，将SW1选为根交换机是最佳选择，如果要将其它交换机选为根交换机或网络需要变动，都会引起不必要的麻烦。由于可以任意将一台交换机接入网络，而新接入的交换机，有很大的可能会因为自己拥有更高的Bridge-ID而抢夺当前根交换机的角色，这样就会引起网络的麻烦。上图中新加入的交换机SW4，如果拥有比当前根交换机SW1更高的Bridge-ID，就会抢夺根交换机的角色。如果SW2要承认SW4为根交换机，就必须将连接SW4的端口F0/19变成根端口，.如果SW2将端口F0/19中断或者阻塞，都将禁止SW4对网络的影响。所以只要控制好连接新加入交换机的端口角色，就能够阻止对方成为根交换机。

特性Root Guard正是利用上述原因，控制SW2用来连接新加入交换机的那个端口的角色，可以决定是否让其影响当前网络。开启了Root Guard功能的端口，如果在此端口上连接的新交换机试图成为根交换机，那么此端口并不会成为根端口，相反，此端口将进入inconsistent (blocked) 状态，从而防止新加入交换机抢占根角色来影响网络。

**注：**

★运行MSTP时，开启了Root guard的端口强制成为指定端口。

★开启Root guard的端口在哪个vlan，Root guard就对哪些vlan生效。

★不能在需要被UplinkFast,使用的端口上开启Root Guard。

★Root Guard在可能连接新交换机的端口上开启。

**配置**

![Root%20Guard%209c0ce9467635453db4fbe5993534816d/image1.png](Root%20Guard/image1.png)

**1.开启Root guard**

**（1）在SW2上连接新交换机的端口F0/19上开启Root guard**

sw2(config-if)#spanning-tree guard root

**2.查看Root guard**

**（1）查看SW2上的Root guard**

sw2#sh spanning-tree detail

（输出被省略）

Port 19 (FastEthernet0/19) of VLAN0001 is forwarding

Port path cost 19, Port priority 128, Port Identifier 128.19.

Designated root has priority 16385, address 007d.618d.0300

Designated bridge has priority 32769, address 0013.805c.4b00

Designated port id is 128.19, designated path cost 19

Timers: message age 0, forward delay 0, hold 0

Number of transitions to forwarding state: 1

Link type is point-to-point by default

Root guard is enabled on the port

BPDU: sent 204, received 0

（输出被省略）

sw2#

**说明：**可以看到，F0/19已经开启Root guard

**3.测试Root guard**

**(1)配置SW4为根**

sw4(config)#spanning-tree vlan 1 priority 4096

**说明：**给SW4配置一个更高优先级的Bridge-ID，以此来抢夺根交换机的角色。

**（2）查看SW2的状态**

当开启了Root guard的端口对方如果要成为根交换机，则会有如下提示，并且接口被放入inconsistent (blocked) 状态：

sw2#

01:18:56: %SPANTREE-2-ROOTGUARD_BLOCK: Root guard blocking port FastEthernet0/19 on VLAN0001.

sw2#

**（3）查看被放入inconsistent (blocked) 状态的端口：**

sw2#sh spanning-tree inconsistentports

Name                 Interface              Inconsistency

- ------------------- ---------------------- ------------------

VLAN0001             FastEthernet0/19       Root Inconsistent

Number of inconsistent ports (segments) in the system : 1

sw2#

**说明：**由于端口F0/19开启了Root guard，而对端要成为根交换机，所以此端口被放入inconsistent (blocked) 状态的端口。