# DTP(Dynamic Trunking Protocol)

DTP(Dynamic Trunking Protocol)

2011年7月7日

14:18

> 在需要使用Trunk链路时，通常是手工静态配置接口模式，并且手工指定Trunk封装协议。然而，当交换机与交换机的接口相连时，多数都需要配置为Trunk模式，而连接主机时，都需要配置为access模式，为了能够让交换机自动判断什么时候该将接口设置为Trunk，因此开发出了动态Trunk配置协议（Dynamic Trunking Protocol），DTP能够在需要将交换机接口配置为Trunk模式时，自动将接口配置为Trunk，并自动选择Trunk封装协议，默认ISL优先。
> 
> 
> DTP采用协商的方式来决定是否将接口配置为Trunk，可配置的接口模式，准确地讲，应该是3种，分别为ON，desirable， auto，下面详细介绍各模式功能：
> 
> **ON**
> 
> 其实就是手工静态配置为Trunk，并且还会向对方主动发起DTP信息，要求对方也工作在Trunk模式，无论对方邻居在什么模式，自己永远工作在Trunk模式。
> 
> **Desirable**
> 
> 此模式为DTP主动模式，工作在此模式的接口会主动向对方发起DTP信息，要求对方也工作在Trunk模式，如果对方回复同意工作在Trunk模式，则工作在Trunk模式，如果没有DTP回复，则工作在access模式。
> 
> **Auto**
> 
> 此模式为DTP被动模式，工作在此模式的接口不会主动发起DTP信息，只会等待对方主动发起DTP信息，如果收到对方的DTP信息要求工作在Trunk模式，则自己回复对方同意工作在Trunk模式，最后的模式为Trunk，如果DTP被动模式收不到DTP要求工作在Trunk的信息，则工作在access模式。
> 
> 以上三种接口模式都会产生DTP信息，ON和desirable是主动产生DTP信息，而auto是被动生产DTP信息，如果手工将接口配置成Trunk模式后，可以关闭DTP信息以节省资源，关闭DTP的模式为nonegotiate。
> 
> **注：**
> 
> Access模式不是DTP的一部分。
> 
> 开启DTP协商的双方都必须在相同的VTP域内，否则协商不成功。
> 
> 交换机的型号不同，默认的DTP模式会有所不同，3550默认为desirable模式，3560默认为auto模式。
> 
> 当收不到对方DTP回复时，则选择工作在access模式。
> 
> 接口配置模式与最终工作模式对照表如下:
> 
> ![DTP(Dynamic%20Trunking%20Protocol)%201f9525dbd64649798f1e4ae58c120ef0/image1.jpg](DTP(Dynamic%20Trunking%20Protocol)/image1.jpg)
> 
> **配置**
> 

![DTP(Dynamic%20Trunking%20Protocol)%201f9525dbd64649798f1e4ae58c120ef0/image2.png](DTP(Dynamic%20Trunking%20Protocol)/image2.png)

**1.配置SW1为desirable，SW2为Trunk**

**（1）配置DTP**

sw1(config)#int f0/23

sw1(config-if)#switchport mode dynamic desirable

sw2(config)#int f0/23

sw2(config-if)#switchport trunk encapsulation dot1q

sw2(config-if)#switchport mode trunk

**（2）查看结果**

sw1#sh int f0/23 switchport

Name: Fa0/23

Switchport: Enabled

Administrative Mode: dynamic desirable

Operational Mode: trunk

Administrative Trunking Encapsulation: negotiate

Operational Trunking Encapsulation: dot1q

Negotiation of Trunking: On

（输出被省略）

sw1#

sw2#sh int f0/23 switchport

Name: Fa0/23

Switchport: Enabled

Administrative Mode: trunk

Operational Mode: trunk

Administrative Trunking Encapsulation: dot1q

Operational Trunking Encapsulation: dot1q

Negotiation of Trunking: On

（输出被省略）

sw2#

**说明：**可以看到，双方接口的DTP协商是开启的，因为双方都会主动发起DTP要求对方工作在trunk，所以最终双方的工作模式为Trunk。

**2.配置SW1为desirable，SW2为auto**

**（1）配置DTP**

sw1(config)#int f0/23

sw1(config-if)#switchport mode dynamic desirable

sw2(config)#int f0/23

**sw2(config-if)#switchport mode dynamic auto**

**（2）查看结果**

sw1#sh int f0/23 switchport

Name: Fa0/23

Switchport: Enabled

Administrative Mode: dynamic desirable

Operational Mode: trunk

Administrative Trunking Encapsulation: negotiate

Operational Trunking Encapsulation: isl

Negotiation of Trunking: On

（输出被省略）

sw1#

sw2#sh int f0/23 switchport

Name: Fa0/23

Switchport: Enabled

Administrative Mode: dynamic auto

Operational Mode: trunk

Administrative Trunking Encapsulation: negotiate

Operational Trunking Encapsulation: isl

Negotiation of Trunking: On

（输出被省略）

sw2#

**说明：**可以看到，双方接口的DTP协商是开启的，因为SW1会主动发起DTP要求对方工作在trunk，而SW2会同意工作在Trunk，所以最终双方的工作模式为Trunk，并且封装协议优选ISL。

**3.配置SW1为auto，SW2为auto**

**（1）配置DTP**

sw1(config)#int f0/23

sw1(config-if)#switchport mode dynamic auto

sw2(config)#int f0/23

sw2(config-if)#switchport mode dynamic auto

**（2）查看结果**

sw1#sh int f0/23 switchport

Name: Fa0/23

Switchport: Enabled

Administrative Mode: dynamic auto

Operational Mode: static access

Administrative Trunking Encapsulation: negotiate

Operational Trunking Encapsulation: native

Negotiation of Trunking: On

（输出被省略）

sw1#

sw2#sh int f0/23 switchport

Name: Fa0/23

Switchport: Enabled

Administrative Mode: dynamic auto

Operational Mode: static access

Administrative Trunking Encapsulation: negotiate

Operational Trunking Encapsulation: native

Negotiation of Trunking: On

（输出被省略）

sw2#

**说明：**可以看到，双方接口的DTP协商是开启的，但由于双方都不会主动发起DTP要求对方工作在trunk，所以最终双方的工作模式为access。

**4.配置SW1为desirable，SW2为Trunk，并且关闭DTP（即为nonegotiate）**

**（1）配置DTP**

sw1(config)#int f0/23

sw1(config-if)#switchport mo dynamic desirable

sw2(config)#int f0/23

sw2(config-if)#switchport trunk encapsulation dot1q

sw2(config-if)#switchport mode trunk

sw2(config-if)#switchport nonegotiate

**（2）查看结果**

sw1#sh int f0/23 switchport

Name: Fa0/23

Switchport: Enabled

Administrative Mode: dynamic desirable

Operational Mode: static access

Administrative Trunking Encapsulation: negotiate

Operational Trunking Encapsulation: native

Negotiation of Trunking: On

（输出被省略）

sw1#

sw2#sh int f0/23 switchport

Name: Fa0/23

Switchport: Enabled

Administrative Mode: trunk

Operational Mode: trunk

Administrative Trunking Encapsulation: dot1q

Operational Trunking Encapsulation: dot1q

Negotiation of Trunking: Off

（输出被省略）

sw2#

**说明：**可以看到，SW1的DTP协商是开启的，而SW2的DTP协商是关闭的， 所以最终SW1的接口选择工作在access模式，而SW2的模式永远都为Trunk。

**5.配置双方都为desirable，但VTP不在相同域内**

**（1）配置DTP**

sw1(config)#vtp domain ccie

sw1(config)#int f0/23

sw1(config-if)#switchport mode dynamic desirable

sw2(config)#vtp domain cisco

sw2(config)#int f0/23

sw2(config-if)#switchport mode dynamic desirable

**（2）查看结果**

sw1#sh vtp status

VTP Version                     : 2

Configuration Revision          : 0

Maximum VLANs supported locally : 1005

Number of existing VLANs        : 5

VTP Operating Mode              : Server

VTP Domain Name                 : ccie

VTP Pruning Mode                : Disabled

VTP V2 Mode                     : Disabled

VTP Traps Generation            : Disabled

MD5 digest                      : 0x04 0x98 0x3D 0x1A 0xA5 0x42 0xDC 0x34

Configuration last modified by 0.0.0.0 at 0-0-00 00:00:00

Local updater ID is 0.0.0.0 (no valid interface found)

sw1#

sw1#sh int f0/23 switchport

Name: Fa0/23

Switchport: Enabled

Administrative Mode: dynamic desirable

Operational Mode: static access

Administrative Trunking Encapsulation: negotiate

Operational Trunking Encapsulation: native

Negotiation of Trunking: On

（输出被省略）

sw1#

sw2#sh vtp status

VTP Version                     : 2

Configuration Revision          : 0

Maximum VLANs supported locally : 1005

Number of existing VLANs        : 5

VTP Operating Mode              : Server

VTP Domain Name                 : cisco

VTP Pruning Mode                : Disabled

VTP V2 Mode                     : Disabled

VTP Traps Generation            : Disabled

MD5 digest                      : 0x57 0x30 0x6D 0x7A 0x76 0x12 0x7B 0x40

Configuration last modified by 0.0.0.0 at 0-0-00 00:00:00

Local updater ID is 0.0.0.0 (no valid interface found)

sw2#

sw2#sh int f0/23 switchport

Name: Fa0/23

Switchport: Enabled

Administrative Mode: dynamic desirable

Operational Mode: static access

Administrative Trunking Encapsulation: negotiate

Operational Trunking Encapsulation: native

Negotiation of Trunking: On

（输出被省略）

sw2#

**说明：**可以看到，双方的DTP协商都是开启的，并且模式都为desirable，正常情况下，双方最终模式应为trunk，然而，由于双方的VTP域名不同，所以DTP协商会失败，所以最终双方的工作模式为access模式。当双方VTP域名不匹配时，开启DTP协商的接口会有如下提示：

01:14:51: %LINK-3-UPDOWN: Interface FastEthernet0/23, changed state to up

01:14:51: %DTP-5-DOMAINMISMATCH: Unable to perform trunk negotiation on port Fa0/23 because of VTP domain mismatch.