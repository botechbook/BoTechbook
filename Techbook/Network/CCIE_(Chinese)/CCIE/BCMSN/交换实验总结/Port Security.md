# Port Security

Port Security

2011年7月7日

14:40

> 交换机在转发数据包时，需要根据数据包的目标MAC地址来决定出口，因此，交换机会将MAC地址与相对应的接口记录在一张表中，以供转发数据包使用，这张表就是MAC地址表。在正常情况下，MAC地址表允许一个接口可以与多个MAC地址相对应，只要接口上有相应的MAC地址，那么数据包就可以从这个接口发出去。一个接口上对应着什么样的MAC地址，一个接口允许多少个MAC地址与之相对应，这都影响到交换机对数据的转发。为了让用户对交换机的MAC地址表有更高的控制权限，交换机接口上的Port Security功能提供更多的安全保护。
> 
> 
> Port Security可以控制交换机上特定的接口与特定的MAC地址的对应关系，也可以限制接口上最大的MAC地址数量。
> 
> 具有Port Security功能的接口，被称为secure port，secure port接口上通过控制数据包的源MAC地址来控制流量，绝不会转发预先定义好的MAC地址之外的流量。准确地说，是secure port只转发合法的流量，对于违规的流量，是不放行的。区别是否违则，有以下两种情况：
> 
> 1．当接口上MAC地址数量达到最大允许数量后，还有更多的MAC要访问，就算违规。
> 
> 2．一个secure port接口上的合法MAC在另外一个secure port接口上访问，也算违规。
> 
> 被Port Security允许的MAC地址，就是合法的MAC地址，称为安全MAC地址（Secure MAC Addresses），secure port接口只放行源MAC为安全MAC地址的数据包。
> 
> 要在secure port接口上定义安全MAC地址，有以下几种方法：
> 
> **静态手工配置**
> 
> 手工添加MAC地址与接口的对应关系，会保存在地址表和running configuration中。
> 
> **动态学习**
> 
> 将接口上动态学习到的MAC地址作为安全MAC地址，但此MAC地址只保存在MAC地址表中，交换机重启后将丢失。
> 
> **Sticky secure MAC addresses**
> 
> 为了结合静态手工配置与动态学习MAC地址的优势，Sticky将动态学习到的MAC地址作为安全MAC地址，并且将结果保存到running configuration中。
> 
> 一个secure port接口上可以允许的MAC地址数量是系统可支持的最大MAC地址数量。对于违规的流量，可以采取以下四个可执行的动作：
> 
> **Protect**
> 
> 只丢弃不允许MAC地址的流量，其它合法流量正常，但不会通知有流量违规了。
> 
> **Restric**
> 
> 只丢弃不允许MAC地址的流量，其它合法流量正常，但会有通知，发送SNMP trap，并会记录syslog。
> 
> **Shutdown**
> 
> （默认模式） 将接口变成error-disabled并shut down，并且接口LED灯会关闭，也会发SNMP  trap，并会记录syslog。
> 
> **shutdown vlan**
> 
> 相应VLAN变成error-disabled ，但接口不会关，也会发SNMP trap，并会记录syslog。
> 
> **注：**
> 
> ★当一个secure port接口上的MAC地址在另外一个secure port接口出现后，就算违规，而违规动作是对出现重复地址的接口实施的，是为了防止攻击。
> 
> ★当接口被error-disabled后，要恢复，请在接口上使用命令：shutdown 后no shutdown。
> 
> 以下是来自思科官方的模式与结果对应表：
> 
> ![Port%20Security%20a065b93841a5479ab386c0c19b8e0c6b/image1.jpg](Port%20Security/image1.jpg)
> 
> **注：**
> 
> ★默认接口上Port Security是关闭的，Port Security默认只允许1个安全MAC地址。
> 
> ★只能在静态access接口和静态trunk接口上配Port Security，不能在dynamic接口上配。
> 
> ★Port Security接口不能是SPAN的目标接口，不能在EtherChannel中。
> 
> Port Security Aging Time （Port Security MAC地址老化时间）
> 
> 在正常接口下动态学习到的MAC地址，在老化时间到了之后，交换机会将它从MAC地址表中删除。
> 
> 而对于Port Security接口下的MAC地址，如果是通过安全命令静态手工添加的，则不受MAC地址老化时间的限制，也就是说通过安全命令静态手工添加的MAC在MAC地址表中永远不会消失。而即使在Port Security接口下动态学习到的MAC地址，也永远不会消失。
> 
> 基于上述原因，有时限制了Port Security接口下的最大MAC地址数量后，当相应的地址没有活动了，为了腾出空间给其它需要通信的主机使用，则需要让Port Security接口下的MAC地址具有老化时间，也就是说需要交换机自动将安全MAC地址删除。
> 
> 对于在Port Security接口下设置MAC地址的老化时间，分两种类型：absolute和inactivity，其中absolute表示绝对时间，即无论该MAC地址是否在通信，超过老化时间后，立即从表中删除；inactivity为非活动时间，即该MAC地址在没有流量的情况下，超过一定时间后，才会从表中删除。
> 
> 配置MAC地址老化时间的单位是分钟，范围是0-1440，对于sticky得到的MAC地址，不受老化时间限制，并且不能更改。
> 
> **配置**
> 

![Port%20Security%20a065b93841a5479ab386c0c19b8e0c6b/image2.png](Port%20Security/image2.png)

**1.查看当前路由器的MAC地址**

**（1）查看R1的接口F0/0的MAC地址**

r1#sh int f0/0

FastEthernet0/0 is up, line protocol is up

Hardware is AmdFE, address is 0013.1a85.d160 (bia 0013.1a85.d160)

Internet address is 10.1.1.1/24

（输出被省略）

r1#

**说明：**R1的接口F0/0的MAC地址为0013.1a85.d160

**（2）查看R2的接口F0/0的MAC地址**

r2#sh int f0/0

FastEthernet0/0 is up, line protocol is up

Hardware is AmdFE, address is 0013.1a2f.1200 (bia 0013.1a2f.1200)

（输出被省略）

R2：

**说明：**R2的接口F0/0的MAC地址为0013.1a2f.1200

**2.配置交换机的port-security**

**（1）配置F0/1**

sw1(config)#int f0/1

sw1(config-if)#switchport mode access

sw1(config-if)#switchport port-security

sw1(config-if)#switchport port-security maximum 1

sw1(config-if)#switchport port-security mac-address 0013.1a85.d160

sw1(config-if)#switchport port-security violation shutdown

**说明：**将接口静态配置成access后，再开启port-security，允许最大地址数量为1，默认也是为1，定义的最大地址数量值不能比已学到的MAC地址少，否则无效。手工静态指定的安全MAC地址为0013.1a85.d160，在违规后采取动作shutdown。

**（2）查看F0/1的配置**

sw1#sh run int f0/1

Building configuration...

Current configuration : 136 bytes

!

interface FastEthernet0/1

switchport mode access

switchport port-security

switchport port-security mac-address 0013.1a85.d160

end

sw1#

**说明：**因为默认允许的最大地址数量为1，所有不显示出来。

**（3）配置F0/2**

sw1(config)#int f0/2

sw1(config-if)#switchport mode access

sw1(config-if)#switchport port-security

sw1(config-if)#switchport port-security maximum 2

sw1(config-if)#switchport port-security mac-address sticky

sw1(config-if)#switchport port-security violation shutdown

**说明：**将接口静态配置成access后，再开启port-security，允许最大地址数量为2，指定安全MAC地址的方式为sticky，在违规后采取动作shutdown。

**（4）查看F0/2的配置**

sw1#sh run int f0/2

Building configuration...

Current configuration : 224 bytes

!

interface FastEthernet0/2

switchport mode access

switchport port-security maximum 2

switchport port-security

switchport port-security mac-address sticky

switchport port-security mac-address sticky 0013.1a2f.1200

end

sw1#

**说明：**因为指定安全MAC地址的方式为sticky，所以此接口连接的R2上的MAC地址0013.1a2f.1200已经被载入配置中。

**3.测试port-security**

**（1）测试R1以合法MAC地址访问R2**

r1#ping 10.1.1.2

Type escape sequence to abort.

Sending 5, 100-byte ICMP Echos to 10.1.1.2, timeout is 2 seconds:

!!!!!

Success rate is 100 percent (5/5), round-trip min/avg/max = 1/2/4 ms

r1#

**说明：**因为R1以源MAC0013.1a85.d160访问R2，交换机的接口F0/1认为0013.1a85.d160是安全MAC，所以R1访问R2成功。

**（2）测试交换机的F0/1上的port-security违规**

r1(config)#int f0/0

r1(config-if)#standby 1 ip 10.1.1.10

**说明：**因为交换机的F0/1允许的最大MAC地址数量为1，而R1已经有了一个MAC地址，在接口上配置HSRP之后，还会产生一个虚拟MAC地址，所以这个HSRP虚拟MAC地址就是第2个MAC地址，而第2个MAC地址在交换机的F0/1上出现就算是违规。

**（3）查看交换机上port-security违规后的现象**

sw1#

01:39:48: %PM-4-ERR_DISABLE: psecure-violation error detected on Fa0/1, putting Fa0/1 in

err-disable state

01:39:48: %PORT_SECURITY-2-PSECURE_VIOLATION: Security violation occurred, caused by MAC

address 0000.0c07.ac01 on port FastEthernet0/1.

01:39:49: %LINEPROTO-5-UPDOWN: Line protocol on Interface FastEthernet0/1, changed state to

down

01:39:50: %LINK-3-UPDOWN: Interface FastEthernet0/1, changed state to down

sw1#

sw1#sh int f0/1

FastEthernet0/1 is down, line protocol is down (err-disabled)

（输出被省略）

sw1#

**说明：**当交换机的port-security违规后,会出现以上log提示，并且查看交换机的接口为err-disabled状态，并且被shutdown。

**（4）测试交换机上port-security另一种违规**

r2(config)#int f0/0

r2(config-if)#mac-address 0013.1a85.d160

**说明：**将R1的MAC地址0013.1a85.d160添加到R2的接口上，因为一个secure port接口上的合法MAC在另外一个secure port接口上访问，也算违规。

**（5）查看交换机上port-security违规后的现象**

sw1#

01:46:27: %PM-4-ERR_DISABLE: psecure-violation error detected on Fa0/2, putting Fa0/2 in

err-disable state

01:46:27: %PORT_SECURITY-2-PSECURE_VIOLATION: Security violation occurred, caused by MAC

address 0013.1a85.d160 on port FastEthernet0/2.

01:46:28: %LINEPROTO-5-UPDOWN: Line protocol on Interface FastEthernet0/2, changed state to

down

01:46:29: %LINK-3-UPDOWN: Interface FastEthernet0/2, changed state to down

sw1#

sw1#sh int f0/1

FastEthernet0/1 is up, line protocol is up (connected)

（输出被省略）

sw1#

sw1#sh int f0/2

FastEthernet0/2 is down, line protocol is down (err-disabled)

（输出被省略）

sw1#

**说明：**可以看见，当一个secure port接口上的MAC地址在另外一个secure port接口出现后，就算违规，而违规动作是对出现重复地址的接口实施的，是为了防止攻击。

**4.配置Port Security MAC地址老化时间**

**（1）配置Port Security MAC地址老化时间**

sw1(config)#int f0/1

sw1(config-if)#switchport port-security aging time 1

sw1(config-if)#switchport port-security aging type inactivity

**说明：**配置Port Security MAC地址老化时间为1分钟，并且相应MAC在1分钟没有流量的情况下被删除。但此配置只对接口下动态学习到的MAC地址生效。

**（2）配置手工静态指定的MAC地址的老化时间**

sw1(config)#int f0/1

sw1(config-if)#switchport port-security aging static

**说明：**配置手工静态指定的MAC地址在1分钟没有流量的情况下被删除。

> 
>