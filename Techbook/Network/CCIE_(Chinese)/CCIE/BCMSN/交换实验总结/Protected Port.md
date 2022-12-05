# Protected Port

Protected Port

2011年7月7日

14:38

> 在某些特殊需求下，需要禁止同台交换机上相同VLAN的主机之间通信，但又不能将这些不能通信的主机划到不同VLAN，因为还需要和VLAN中的其它主机通信，只是不能和部分主机通信。要限制交换机上相同VLAN的主机通信，通过将交换机上的接口配置成Protected Port来实现，如果交换机上某个VLAN有三个接口，其中有两个是Protected Port，有一个是正常端口，那么两个 Protected Port之间是不能通信的，但是Protected Port与正常端口之间的流量还是保持正常，而不受任何限制。
> 
> 
> Protected Port可以拒绝unicast，broadcast以及multicast在这些端口之间通信，也就是说Protected Port与Protected Port之间没有任何流量发送。Protected Port只在单台交换机上有效，也就是说只有单台交换机上的Protected Port与Protected Port之间是不能通信的，但是不同交换机的Protected Port与Protected Port之间通信还是保持正常。
> 
> 配置Protected Port时，可以在物理接口和EtherChannel上配置，如果是配在EtherChannel上，那么配置将对EtherChannel中的所有物理接口生效。
> 
> **配置**
> 

![Protected%20Port%20ff3167fcecf945ed8b2c673fd8f396c5/image1.png](Protected%20Port/image1.png)

> 
> 
> 
> **说明：**以上图为例，配置protected port，SW1的F0/1，F0/2，F0/3以及SW2的F0/4都在VLAN 10中。
> 
> **1.配置交换机**
> 
> **（1）配置SW1**
> 
> sw1(config)#vlan 10
> 
> sw1(config-vlan)#exit
> 
> sw1(config)#int range f0/1 - 3
> 
> sw1(config-if-range)#switchport mode access
> 
> sw1(config-if-range)#switchport access vlan 10
> 
> sw1(config)#int f0/23
> 
> sw1(config-if)#switchport trunk encapsulation dot1q
> 
> sw1(config-if)#switchport mode trunk
> 
> **（2）配置SW2**
> 
> sw2(config)#vlan 10
> 
> sw2(config-vlan)#exit
> 
> sw2(config)#int f0/4
> 
> sw2(config-if)#switchport mode access
> 
> sw2(config-if)#switchport access vlan 10
> 
> sw2(config)#int f0/23
> 
> sw2(config-if)#switchport trunk encapsulation dot1q
> 
> sw2(config-if)#switchport mode trunk
> 
> **2.配置路由器**
> 
> **（1）配置R1**
> 
> r1(config)#int f0/0
> 
> r1(config-if)#ip add 10.1.1.1 255.255.255.0
> 
> **（2）配置R2**
> 
> r2(config)#int f0/0
> 
> r2(config-if)#ip add 10.1.1.2 255.255.255.0
> 
> **（3）配置R3**
> 
> r3(config)#int f0/0
> 
> r3(config-if)#ip add 10.1.1.3 255.255.255.0
> 
> **（4）配置R4**
> 
> r4(config)#int f0/1
> 
> r4(config-if)#ip add 10.1.1.4 255.255.255.0
> 
> **3.测试正常情况下的通信**
> 
> **（1）测试R1到R2的连通性**
> 
> r1#ping 10.1.1.2
> 
> Type escape sequence to abort.
> 
> Sending 5, 100-byte ICMP Echos to 10.1.1.2, timeout is 2 seconds:
> 
> !!!!!
> 
> Success rate is 100 percent (5/5), round-trip min/avg/max = 1/2/4 ms
> 
> r1#
> 
> **说明：**因为没有配置protected port，所以R1到R2通信正常。
> 
> **（2）测试R1到R3的连通性**
> 
> r1#ping 10.1.1.3
> 
> Type escape sequence to abort.
> 
> Sending 5, 100-byte ICMP Echos to 10.1.1.3, timeout is 2 seconds:
> 
> !!!!!
> 
> Success rate is 100 percent (5/5), round-trip min/avg/max = 1/2/4 ms
> 
> r1#
> 
> **说明：**因为没有配置protected port，所以R1到R3通信正常。
> 
> **（3）测试R1到R4的连通性**
> 
> r1#ping 10.1.1.4
> 
> Type escape sequence to abort.
> 
> Sending 5, 100-byte ICMP Echos to 10.1.1.4, timeout is 2 seconds:
> 
> !!!!!
> 
> Success rate is 100 percent (5/5), round-trip min/avg/max = 1/2/4 ms
> 
> r1#
> 
> 说明：因为没有配置protected port，所以R1到R4通信正常。
> 
> **3.配置protected port**
> 
> **（1）在SW1上将F0/1和F0/2配置为protected port**
> 
> sw1(config)#int f0/1
> 
> sw1(config-if)#switchport protected
> 
> sw1(config)#int f0/2
> 
> sw1(config-if)#switchport protected
> 
> **(2) 在SW2上将F0/4 配置为protected port**
> 
> sw2(config)#int f0/4
> 
> sw2(config-if)#switchport protected
> 
> **4.测试配置了protected port的网络通信**
> 
> **（1）测试R1到同台交换机的正常端口F0/3的连通性**
> 
> r1#ping 10.1.1.3
> 
> Type escape sequence to abort.
> 
> Sending 5, 100-byte ICMP Echos to 10.1.1.3, timeout is 2 seconds:
> 
> !!!!!
> 
> Success rate is 100 percent (5/5), round-trip min/avg/max = 1/1/4 ms
> 
> r1#
> 
> **说明：**因为protected port与正常端口之间的通信不受影响，所以R1到R3通信正常。
> 
> **（2）测试R1到同台交换机的protected port F0/2的连通性**
> 
> r1#ping 10.1.1.2
> 
> Type escape sequence to abort.
> 
> Sending 5, 100-byte ICMP Echos to 10.1.1.2, timeout is 2 seconds:
> 
> .....
> 
> Success rate is 0 percent (0/5)
> 
> r1#
> 
> **说明：**因为同台交换机上protected port与protected port之间的流量被拒绝，所以R1到R2通信失败。
> 
> **（3）测试R1到远程交换机SW2的protected port F0/4的连通性**
> 
> r1#ping 10.1.1.4
> 
> Type escape sequence to abort.
> 
> Sending 5, 100-byte ICMP Echos to 10.1.1.4, timeout is 2 seconds:
> 
> !!!!!
> 
> Success rate is 100 percent (5/5), round-trip min/avg/max = 1/2/4 ms
> 
> r1#
> 
> **说明：**因为只有单台交换机上的Protected Port与Protected Port之间是不能通信的，但是不同交换机的Protected Port与Protected Port之间通信还是保持正常，所以R1到R4的通信正常。
> 
> **（4）在交换机上查看Protected Port**
> 
> sw1#sh int f0/1 switchport
> 
> （输出被省略）
> 
> Protected: true
> 
> Unknown unicast blocked: disabled
> 
> Unknown multicast blocked: disabled
> 
> Appliance trust: none
> 
> sw1#
> 
> **说明：**可以看到交换机上接口的Protected Port功能已经开启。
> 

> 
>