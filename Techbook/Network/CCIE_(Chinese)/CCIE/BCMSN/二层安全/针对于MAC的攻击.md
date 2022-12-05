# 针对于MAC的攻击

针对于MAC的攻击

2011年7月7日

15:06

**关于针对于MAC的攻击**

**可以对MAC进行攻击原因是：**

**1.交换机对未知单播要进行泛洪**

**2.CAM表的大小是有限的**

**攻击原理：伪造很多假MAC将交换机的CAM表挤破，这样任何的帧都是未知单播了**

**知识补充：**

**3xxx对应的CAM表的大小是16000**

**4xxx对应的CAM表的大小是32000**

**6xxx对应的CAM表的大小是128000**

**3.解决方案：使用端口安全（Port Security）**

**端口安全是一种第2层特性。端口安全能够基于主机MAC地址而允许流量。**

**单个端口能够允许1个以上到某个特定数目的MAC地址，有助于避免网络的非授权访问。**

**端口安全中的违背，表示未经授权地使用了端口安全配置中所定义的网络资源，违背端口安全存在两种可能的原因：**

- **安全端口接收到具有未授权源MAC地址的数据帧**
- **当端口已经学到所允许的最大数目的MAC地址之后，又接收到新的数据帧**

**当检测到违背端口安全之后，交换机将会执行下列某种行为：**

- **关闭——永久性或在特定周期内err-disable端口**
- **限制——交换机继续工作，但丢弃来自未授权主机的数据帧**
- **保护——当已经超过所允许学习的最大MAC地址数的时候，交换机继续工作，但丢弃来自新主机的数据帧**

> 实际工作中，我们所选择的行为取决于下列要素：特定的网络场景、交换机位置、期望的安全程度。
> 

**当接口处于err-disable模式的时候，可以通过配置计时器让接口自动恢复：**

**err-disable recovery cause secure-violation**

**err-disable recovery interval *time-interval***

> time-interval表示由于错误状态导致被禁用之后又重新启用接口之后的时间，单位s。
> 

**switchport port-security mac-address sticky**

> 启用 sticky特性的时候，在学习到地址后，交换机将把学习到的MAC地址动态地转化为sticky MAC地址，并且随后将其加入到运行配置中，就如同它们是端口安全所允许的单个MAC地址的静态表项。
> 

**SW1(config)#interface fastEthernet 1/1**

**SW1(config-if)#switchport mode access**

**SW1(config-if)#switchport access vlan 2**

**SW1(config-if)#spanning-tree portfast**

**SW1(config-if)#switchport port-security mac-address 0000.F092.9041 //手工绑定MAC地址**

**SW1(config-if)#switchport port-security maximum 2 //设置最大的MAC的数量**

**SW1(config-if)#switchport port-security violation restrict //当违背端口安全时作出的行为（分为三个：protect（丢包）、restrict（丢包+警告）、shutdown（err-disable状态））**

**SW1(config-if)#switchport port-security //生效命令**

**注意：**

**protect：丢包**

**restrict：丢包+警告**

**shutdown：err-disable状态**