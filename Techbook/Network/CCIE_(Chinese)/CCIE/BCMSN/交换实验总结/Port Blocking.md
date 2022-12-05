# Port Blocking

Port Blocking

2011年7月7日

14:39

> 默认情况下，交换机收到未知目标MAC的流量，也就是目标MAC地址不在MAC地址表中的流量，会将此流量在所有接口上泛洪。用户可以选择在交换机接口上拒绝泛洪未知目标MAC的流量，配置可以对unicast和 multicast生效，但不能限制广播流量。
> 
> 
> 接口上默认是没有Port Blocking配置的。
> 
> 配置Port Blocking时，可以在物理接口和EtherChannel上配置，如果是配在EtherChannel上，那么配置将对EtherChannel中的所有物理接口生效。
> 
> **配置**
> 
> **1.在接口上配置Port Blocking**
> 
> **（1）配置Port Blocking限制unicast**
> 
> sw1(config)#int f0/1
> 
> sw1(config-if)#switchport block unicast
> 
> **（2）配置Port Blocking限制multicast**
> 
> sw1(config)#int f0/1
> 
> sw1(config-if)#switchport block multicast
> 
> **(3)查看Port Blocking**
> 
> sw1#sh interfaces f0/1 switchport
> 
> （输出被省略）
> 
> Unknown unicast blocked: enabled
> 
> Unknown multicast blocked: enabled
> 
> Appliance trust: none
> 
> sw1#
> 
> **说明：**可以看到，交换机接口上已经开启拒绝泛洪未知目标MAC的单播流量和组播流量，并且两个可以同时开启。
> 

> 
>