# BPDU Filtering

BPDU Filtering

2011年7月7日

14:34

> BPDU Filtering可以过滤掉在接口上发出或收到的BPDU，这就相当于关闭了接口的STP，将会有引起环路的可能。
> 
> 
> BPDU Filtering的配置同样也分两种，可以在接口下或在全局模式开启，但是不同的模式开启，会有不同效果。
> 
> 如果BPDU Filtering是全局开启的，则只能在开启了portfast的接口上过滤BPDU，并且只能过滤掉发出的BPDU，并不能过滤收到的BPDU，因为BPDU Filtering的设计目的是当交换机端口上连接的是主机或服务器时，就没有必要向对方发送BPDU，所以要过滤掉BPDU，但如果连接的是交换机，则会收到BPDU，而且会引起环路，所以这样的情况，配置BPDU Filtering就是错误的。而当一个开启了portfast功能的接口，在开启了BPDU Filtering后，如果还能收到BPDU，则BPDU Filtering特性会丢失，因此，还会造成接口portfast特性的丢失。
> 
> 如果是在接口模式下开启的，则可以过滤掉任何接口收到和发出的BPDU。(此理论为重点)
> 
> **配置**
> 

![BPDU%20Filtering%2042c69b6583a6429992bb63bce2429e2a/image1.png](BPDU%20Filtering/image1.png)

**1.在全局模式下配置BPDU Filtering（只能过滤portfast上的BPDU）**

**（1）将SW2的端口F0/23和F0/24改成三层接口**

sw2(config)#int ran f0/23 - 24

sw2(config-if-range)#no switchport

**说明：**禁止从端口上向SW1发送BPDU。

**（2）将SW1的端口F0/23配置为Port Fast，将F0/24配置为正常端口，但开启BPDU Guard**

sw1(config)#int f0/23

sw1(config-if)#switchport mode access

sw1(config-if)#spanning-tree portfast

sw1(config)#int f0/24

sw1(config-if)#switchport mode access

sw1(config-if)#spanning-tree bpduguard enable

**（3）查看SW1的端口F0/23和F0/24 的状态**

sw1#sh spanning-tree interface f0/23 portfast

VLAN0001         enabled

sw1#

sw1#sh int f0/24

FastEthernet0/24 is up, line protocol is up (connected)

（输出被省略）

sw1#

**说明：**SW1的端口F0/23为Port Fast状态，F0/24为正常状态，并且状态为UP。

**（4）在SW1上全局开启BPDU Filtering（只能过滤portfast上的BPDU）**

sw1(config)#spanning-tree portfast bpdufilter default

**（5）在SW2的端口F0/23和F0/24向SW1发送BPDU，测试BPDU Filtering**

sw2(config)#int range f0/23 - 24

sw2(config-if-range)#switchport

**说明：**只要将SW2的端口F0/23和F0/24变成二层端口，便可以从此端口向外发送BPDU。

**（6）查看SW1的端口状态：**

sw1#sh spanning-tree interface f0/23 portfast

VLAN0001         disabled

sw1#

sw1#sh int f0/24

FastEthernet0/24 is down, line protocol is down (err-disabled)

（输出被省略）

sw1#

**说明：**因为F0/24是普通端口，全局配置的BPDU Filtering不能过滤普通端口上的BPDU，所以收到了BPDU后，但由于BPDU Guard，最后端口被err-disabled。

而F0/23是开启了portfast功能的接口，在开启了BPDU Filtering后，如果还能收到BPDU，则BPDU Filtering特性会丢失，因此，造成了端口F0/23的portfast特性丢失。

**2.在接口模式下配置BPDU Filtering（将对任何端口生效）**

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

**（3）在SW1的端口F0/24开启BPDU Guard**

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

**（5）在SW1的端口F0/23和F0/24下开启BPDU Filtering**

sw1(config)#int range f0/23 - 24

sw1(config-if-range)#spanning-tree bpdufilter enable

**（6）在SW2的端口F0/23和F0/24向SW1发送BPDU，测试BPDU Filtering**

sw2(config)#int range f0/23 - 24

sw2(config-if-range)#switchport

**(7) 查看SW1的端口状态：**

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

**说明：**接口下开启的BPDU Filtering，过滤掉了正常端口下的BPDU，也过滤掉了portfast端口下的BPDPU。

> 
>