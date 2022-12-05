# Port Fast

Port Fast

2011年7月7日

14:28

> 因为一个默认情况下的交换机端口，在交换机启动后，由于STP的原因，端口状态需要从initialization（初始化）到blocking，从blocking到listening，从listening 到learning，从learning到forwarding，其中经历了两个forward delay，也就是说一个端口在交换机启动后，至少需要30秒后才能够为用户提供数据转发。对于一个连接了主机或服务器的端口，进行STP计算是毫无必要的，因为此类端口即使直接转发数据，也不会造成环路，并且30秒的时间对于需要立即传递数据的主机或服务器来说，是漫长的，因此，此类端口可以配置为跳过STP的计算，从而直接过渡到forwarding状态。
> 
> 
> 此类端口通常称为边缘端口，在思科交换机上，通过配置Port Fast功能，便可以使接口跳过STP的计算，从而直接过渡到forwarding状态。
> 
> access接口和Trunk接口都可以配置Port Fast功能。如果将交换机连交换机的接口变成Port Fast，则是制造环路。
> 
> 当开启了Port Fast功能的接口，如果在接口上收到BPDU后，就认为对端连接的是交换机，而并非主机或服务器，因此默认在接口收到BPDU后会立即关闭该接口的Port Fast功能。
> 
> **配置**
> 

![Port%20Fast%208ccb007436fa46599ac3b80722e54427/image1.png](Port%20Fast/image1.png)

**1.在接口下配置Port Fast**

**（1）将SW2的端口F0/23和F0/24改成三层接口**

**说明：**因为如果SW2的端口是二层接口，那么就会向SW1发送BPDU，最终会造成SW1由于收到BPDU而关闭Port Fast功能，所以就无法验证Port Fast。

sw2(config)#int ran f0/23 - 24

sw2(config-if-range)#no switchport

**说明：**禁止从端口上向SW1发送BPDU。

**（2）在SW1的F0/23和F0/24上开启Port Fast**

**说明：**access和trunk接口模式都可以配置

sw1(config)#int ran f0/23 - 24

sw1(config-if-range)#switchport mode access

sw1(config-if-range)#spanning-tree portfast

**说明：**将端口变为静态access，再开portfast。（无论什么模式的接口都可以开启Port Fast）

**（3）验证Port Fast**

sw1#sh spanning-tree interface f0/23 portfast

VLAN0001         enabled

sw1#

sw1#sh spanning-tree interface f0/24 portfast

VLAN0001         enabled

sw1#

**说明：**端口F0/23和F0/24已经开启portfast功能。

**（4）在SW2的端口F0/23向SW1发送BPDU**

sw2(config)#int f0/23

sw2(config-if)#switchport

**说明：**只要将SW2的端口F0/23变成二层端口，便可以从此端口向外发送BPDU。

**（5）查看SW1的端口的portfast状态：**

sw1#sh spanning-tree interface f0/23 portfast

VLAN0001         disabled

sw1#

sw1#sh spanning-tree interface f0/24 portfast

VLAN0001         enabled

sw1#

**说明：**可以看见，SW1的端口F0/23，在收到BPDU后，portfast功能自动丢失。

**2.在全局模式下配置Port Fast（只能对access接口生效）**

**（1）将SW2的端口F0/23和F0/24改成三层接口**

sw2(config)#int ran f0/23 - 24

sw2(config-if-range)#no switchport

**(2)将SW1的端口配置为access**

sw1(config)#int ran f0/23 - 24

sw1(config-if-range)#switchport mode dynamic desirable

**说明：**因为对方是三层端口，在本地配置DTP后，会自动形成access模式。

**（3）查看SW1的端口状态**

sw1#show interfaces f0/23 switchport

Name: Fa0/23

Switchport: Enabled

Administrative Mode: dynamic desirable

Operational Mode: static access

Administrative Trunking Encapsulation: negotiate

Operational Trunking Encapsulation: native

Negotiation of Trunking: On

（输出被省略）

sw1#

sw1#show interfaces f0/24 switchport

Name: Fa0/24

Switchport: Enabled

Administrative Mode: dynamic desirable

Operational Mode: static access

Administrative Trunking Encapsulation: negotiate

Operational Trunking Encapsulation: native

Negotiation of Trunking: On

（输出被省略）

sw1#

**说明：**DTP已经将本地端口变为access模式。

**(4)在SW1全局开启Port Fast**

sw1(config)#spanning-tree portfast default

**（5）查看SW1上端口的Port Fast状态**

sw1#sh spanning-tree interface f0/23 portfast

VLAN0001         enabled

sw1#sh spanning-tree interface f0/24 portfast

VLAN0001         enabled

sw1#

**说明：**SW1上的access端口受全局配置影响，已经变成Port Fast端口。

**（6）验证同上，省略**

> 
>