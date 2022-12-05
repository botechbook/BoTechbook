# 交换机MAC地址表

交换机MAC地址表

2011年7月7日

14:09

> 交换机在转发数据时，需要根据MAC地址表来做出相应转发，如果目标主机的MAC地址不在表中，交换机将收到的数据包在所有活动接口上广播发送。当交换机上的接口状态变成UP之后，将动态从该接口上学习MAC地址，并且将学习到的MAC地址与接口相对应后放入MAC地址表。
> 
> 
> 交换机的MAC地址表除了动态学习之外，还可以静态手工指定，并且在指定MAC地址时，还可以指定在某个VLAN的某个接口收到相应的MAC后，将数据包作丢弃处理。
> 
> **注：交换机上，一个接口可以对应多个MAC地址，地址的数量无上限，但不超过交换机所支持的MAC地址最大数量。**
> 
> 一个MAC地址可以同时出现在交换机的多个接口上，但此特性并不被所有型号的交换机支持，在某些型号的交换机上，一个MAC地址只能出现在一个接口上，如果出现在另外一个接口上，将会报错，并且数据转发也会出错。
> 
> **（1）查看接口F0/1的MAC地址表**
> 
> Switch#sh mac-address-table interface f0/1
> 
> Mac Address Table
> 
> - ------------------------------------------
> 
> Vlan    Mac Address       Type        Ports
> 
> - --- ----------- -------- -----
> 
> 2    0013.1a2f.0680    DYNAMIC     Fa0/1
> 
> Total Mac Addresses for this criterion: 1
> 
> Switch#
> 
> **说明：**交换机从F0/1上学习到了MAC地址0013.1a2f.0680，并且说明是动态学习到的。
> 

> 手工静态指定MAC地址
> 
> 
> **（1）手工静态指定MAC地址**
> 
> Switch(config)#mac-address-table static 0013.1a2f.0680 vlan 1 interface f0/2
> 
> **说明：**指定VLAN 1的接口F0/2的MAC地址为0013.1a2f.0680。
> 
> **（2）查看接口F0/2的MAC地址表**
> 
> Switch#sh mac-address-table interface f0/2
> 
> Mac Address Table
> 
> - ------------------------------------------
> 
> Vlan    Mac Address       Type        Ports
> 
> - --- ----------- -------- -----
> 
> 1    0013.1a2f.0680    STATIC      Fa0/2
> 
> 1    0013.1a7f.a4a0    DYNAMIC     Fa0/2
> 
> Total Mac Addresses for this criterion: 2
> 
> Switch#
> 
> **说明：**接口F0/2上除了动态学习到的MAC地址之外，还有静态手工指定的地址。
> 
> **（3）指定丢弃某个MAC地址**
> 
> Switch(config)#mac-address-table static 0013.1a2f.0680 vlan 2 drop
> 
> **说明：**此配置将使源MAC为0013.1a2f.0680的数据包在VLAN 2被丢弃，但在别的VLAN通信正常。
> 

**MAC地址老化时间（aging-time）**

交换机在一个接口上学习到MAC地址之后，该MAC与接口的映射并不会永远被保存在MAC地址表中，除非是手工静态指定的。当一台主机从某个接口转移后，交换机再将目标MAC为该主机的数据从该接口发出去是毫无意义的，所以MAC地址在MAC地址表中是有最大停留时间的，称为老化时间（aging-time），当相应MAC地址在超出老化时间后还没有数据传输时，该MAC地址将从表中被清除。**默认的MAC地址老化时间为300秒（5分钟）。**

**（1）修改MAC地址的老化时间**

**说明：**只能针对VLAN作修改

**Switch(config)#mac-address-table aging-time 60 vlan 1**

**说明：**将VLAN 1的MAC地址老化时间改为60秒。

**（2）查看MAC地址的老化时间**

Switch#sh mac-address-table aging-time

Global Aging Time:  300

Vlan    Aging Time

- --- ----------

1      60

2     300

3     300

4     300

Switch#

**说明：**可以看到，VLAN 1的MAC地址老化时间为60秒，其它VLAN保存默认300秒。

> 
>