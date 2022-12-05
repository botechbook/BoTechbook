# 交换机自身MAC地址

交换机自身MAC地址

2011年7月7日

14:12

> 以太网中，每一个节点，都需要一个MAC地址，而以太网交换机可以与多个终端连接，也就有多个节点，因此，交换机上也会有多个MAC地址存在，如交换机的每个接口都有一个MAC地址，包含物理接口和SVI接口。除此之外，还有一个MAC地址是用来表示整台交换机的。
> 
> 
> **注：**都知道2层交换机的VLAN 1为管理VLAN，一个表示整台交换机的MAC地址通常就是VLAN 1的MAC地址，但这种情况又需要根据交换机型号而定，并不适用于任何型号的交换机。
> 
> 某些型号的交换机，所有VLAN的SVI接口MAC地址全部相同，但某些型号却是不同的，但是连续的。
> 
> **查看交换机的MAC地址**
> 
> **（1）查看表示整台交换机的MAC地址**
> 
> Switch#sh version
> 
> （输出被省略）
> 
> 512K bytes of flash-simulated non-volatile configuration memory.
> 
> Base ethernet MAC Address       : 00:1A:6C:6F:FB:00
> 
> Motherboard assembly number     : 73-9897-06
> 
> Power supply part number        : 341-0097-02
> 
> Motherboard serial number       : CAT10475C57
> 
> Power supply serial number      : AZS104407JE
> 
> Model revision number           : D0
> 
> Motherboard revision number     : A0
> 
> Model number                    : WS-C3560-24TS-S
> 
> System serial number            : CAT1047RJNU
> 
> Top Assembly Part Number        : 800-26160-02
> 
> Top Assembly Revision Number    : C0
> 
> Version ID                      : V02
> 
> CLEI Code Number                : COMMG00ARB
> 
> Hardware Board Revision Number  : 0x01
> 
> Switch   Ports  Model              SW Version              SW Image
> 
> - ----- ----- ----- ---------- ----------
> - 1 26 WS-C3560-24TS 12.2(35)SE1 C3560-ADVIPSERVICESK
> 
> Configuration register is 0xF
> 
> Switch#
> 
> **说明：**表示整台交换机的MAC地址为00:1A:6C:6F:FB:00。
> 
> **（2）查看物理接口的MAC地址**
> 
> Switch#sh int f0/1
> 
> FastEthernet0/1 is up, line protocol is up (connected)
> 
> Hardware is Fast Ethernet, address is 001a.6c6f.fb03 (bia 001a.6c6f.fb03)
> 
> （输出被省略）
> 
> Switch#sh int f0/2
> 
> FastEthernet0/2 is up, line protocol is up (connected)
> 
> Hardware is Fast Ethernet, address is 001a.6c6f.fb04 (bia 001a.6c6f.fb04)
> 
> （输出被省略）
> 
> Switch#sh int f0/3
> 
> FastEthernet0/3 is up, line protocol is up (connected)
> 
> Hardware is Fast Ethernet, address is 001a.6c6f.fb05 (bia 001a.6c6f.fb05)
> 
> （输出被省略）
> 
> **说明：**可以看到，物理接口的MAC地址是连续的，但无论什么型号的交换机，物理接口的MAC地址一定是不同的。
> 
> **（3）查看SVI接口的MAC地址**
> 
> Switch#sh int vlan 1
> 
> Vlan1 is up, line protocol is up
> 
> Hardware is EtherSVI, address is 001a.6c6f.fb40 (bia 001a.6c6f.fb40)
> 
> （输出被省略）
> 
> Switch#sh int vlan 2
> 
> Vlan2 is up, line protocol is up
> 
> Hardware is EtherSVI, address is 001a.6c6f.fb41 (bia 001a.6c6f.fb41)
> 
> （输出被省略）
> 
> Switch#sh int vlan 3
> 
> Vlan3 is up, line protocol is up
> 
> Hardware is EtherSVI, address is 001a.6c6f.fb42 (bia 001a.6c6f.fb42)
> 
> （输出被省略）
> 
> **说明：**可以看到，交换机SVI接口的MAC地址是连续的，但某些型号的交换机，所有SVI接口的MAC地址全部是相同的。
> 

> 
>