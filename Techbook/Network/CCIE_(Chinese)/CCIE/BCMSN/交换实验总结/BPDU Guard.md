# BPDU Guard

BPDU Guard

2011年7月7日

14:32

> 因为开启了Port Fast功能的端口，会跳过STP的计算，从而直接过渡到forwarding状态。当端口连接的是主机或服务器，这样的操作不会有任何问题，但如果连接的是交换机，就会收到BPDU，就证明在此接口开启Port Fast功能是错误的配置。为了杜绝此类错误配置，BPDU Guard功能可以使端口在收到BPDU时，立即被shutdown或进入err-disabled状态。
> 
> 
> BPDU Guard可以在接口下或全局开启，但操作会有所不同。
> 
> 如果BPDU Guard是全局开启，则只对portfast端口有影响，当portfast端口收到BPDU后，会shutdown此端口，需要注意，某些型号的交换机会将接口error-disabled。
> 
> 如果BPDU Guard是接口下开启，将对任何端口有影响，无论是正常端口还是portfast端口；当端口收到BPDU后，会变成error-disabled状态。
> 
> **配置**
> 

![BPDU%20Guard%2071448f8e037b4a739f321747d410d4f4/image1.png](BPDU%20Guard/image1.png)

**1.在全局模式下配置BPDU Guard（只对Port Fast端口有影响）**

**（1）将SW2的端口F0/23和F0/24改成三层接口**

sw2(config)#int ran f0/23 - 24

sw2(config-if-range)#no switchport

**说明：**禁止从端口上向SW1发送BPDU。

**（2）将SW1的端口F0/23 配置为Port Fast，F0/24为正常端口**

sw1(config)#int f0/23

sw1(config-if)#switchport mode access

sw1(config-if)#spanning-tree portfast

sw1(config)#int f0/24

sw1(config-if)#switchport mode access

**（3）查看SW1的端口F0/23和F0/24 的状态**

sw1#sh spanning-tree interface f0/23 portfast

VLAN0001         enabled

sw1#

sw1#sh spanning-tree interface f0/24 portfast

VLAN0001         disabled

sw1#

sw1#sh protocols f0/23

FastEthernet0/23 is up, line protocol is up

sw1#sh protocols f0/24

FastEthernet0/24 is up, line protocol is up

sw1#

**说明：**SW1的端口F0/23已经变成Port Fast状态，而F0/24为正常端口，并且两个端口都为正常UP状态。

**（4）在SW1全局开启BPDU Guard（只对Port Fast端口有影响）**

sw1(config)#spanning-tree portfast bpduguard default

**（5）在SW2的端口F0/23和F0/24向SW1发送BPDU，测试BPDU Guard**

sw2(config)#int ran f0/23 - 24

sw2(config-if-range)#switchport

**说明：**只要将SW2的端口F0/23和F0/24变成二层端口，便可以从此端口向外发送BPDU。

**（6）查看SW1的端口状态：**

sw1#sh spanning-tree interface f0/23 portfast

no spanning tree info available for FastEthernet0/23

sw1#

sw1#sh spanning-tree interface f0/24 portfast

VLAN0001         disabled

sw1#

sw1#sh protocols f0/23

FastEthernet0/23 is down, line protocol is down

sw1#

sw1#sh protocols f0/24

FastEthernet0/24 is up, line protocol is up

sw1#sh int f0/23

FastEthernet0/23 is down, line protocol is down (err-disabled)

（输出被省略）

sw1#

**说明：**可以看见，SW1的portfast端口F0/23收到BPDU后，受到BPDU Guard的影响，端口被shutdown，并且变成error-disabled，（某些型号不会），而全局BPDU Guard不能影响非portfast端口，所以F0/24还是正常状态。

**2.在接口模式下配置BPDU Guard（将对任何端口生效）**

**（1）将SW2的端口F0/23和F0/24改成三层接口**

sw2(config)#int ran f0/23 - 24

sw2(config-if-range)#no switchport

**说明：**禁止从端口上向SW1发送BPDU。

**（2）将SW1的端口F0/23配置为portfast，将F0/24配置为正常端口**

sw1(config)#int f0/23

sw1(config-if)#switchport mode access

sw1(config-if)#spanning-tree portfast

sw1(config)#int f0/24

sw1(config-if)#switchport mode access

**（3）在SW1的端口F0/23和F0/24开启BPDU Guard**

sw1(config)#int ran f0/23 - 24

sw1(config-if-range)#spanning-tree bpduguard enable

**（4）查看SW1的端口F0/23和F0/24 的状态**

sw1#sh spanning-tree interface f0/23 portfast

VLAN0001         enabled

sw1#

sw1#sh spanning-tree interface f0/24 portfast

VLAN0001         disabled

sw1#

sw1#sh protocols f0/23

FastEthernet0/23 is up, line protocol is up

sw1#

sw1#sh protocols f0/24

FastEthernet0/24 is up, line protocol is up

sw1#

**说明：**SW1上的端口F0/23为portfast状态，F0/24为正常状态，并且状态都为UP。

**（5）在SW2的端口F0/23和F0/24向SW1发送BPDU，测试BPDU Guard**

sw2(config)#int range f0/23 - 24

sw2(config-if-range)#switchport

**（6）查看SW1的端口状态：**

sw1#sh spanning-tree interface f0/23 portfast

no spanning tree info available for FastEthernet0/23

sw1#

sw1#sh spanning-tree interface f0/24 portfast

no spanning tree info available for FastEthernet0/24

sw1#

sw1#sh int f0/23

FastEthernet0/23 is down, line protocol is down (err-disabled)

（输出被省略）

sw1#sh int f0/24

FastEthernet0/24 is down, line protocol is down (err-disabled)

（输出被省略）

sw1#

**说明：**SW1的端口在收到BPDU后，受到BPDU Guard的影响，无论是正常端口还是portfast端口，都被err-disabled。

> 
>