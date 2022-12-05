# GRE over IPSEC

GRE over IPSEC

2011年8月2日

22:04

GRE over IPSEC Configuration

IPSec-Over-GRE和GRE-Over-IPSec方式配置上的区别为：

**GRE-Over-IPSec IPSec-Over-GRE**

ACL定义 GRE数据流 内网数据流

IKE peer中指定的remote-address 对方公网地址 对方GRE tunnel地址

应用端口 公网出口 GRE tunnel上

IPsec over GRE 跟IPsec配置的区别

acl 内网数据流 内网数据流

peer tunnel地址 对方公网地址

应用端口 tunnel端口 公网出口

GRE over IPsec 跟IPsec配置的区别

acl GRE数据流 内网数据流

peer 对方公网地址 对方公网地址

应用端口 公网出口 公网出口

技术特点:

IPSec (ESP) tunnel only IP unicast traffic

GRE encryption non-ip and ip multicast or broadcast packets into ip unicast packets

Using a GRE tunnel inside an ipsec tunnel uses only three SA (at maximum)

GRE---Generic Routing Encapsulation

GRE是一个三层协议,无连接,没有安全性,支持的协议:IP / IPX / Apple Talk

Tunnel Mode 包结构: | IP | ESP | IP | GRE | IP | TCP | Data | ESP |

|<=== Encrypted Payload ===>|

Transport Mode 包结构: | IP | ESP | GRE | IP | TCP | Data | ESP |

|<=== Encrypted Payload ===>|

实验 1 :

本实验Tunnel Mode的包结构:

..| Peer source Peer destination| ESP| GRE的源地址 GRE的目标地址| GRE | 源IP 目标IP | data | ESP |..

本实验Transport Mode 包结构:

由于"Peer source Peer destination"(加密点)等于"GRE的源地址 GRE的目标地址"(通信点),所以包结构更改为: ...| GRE的源地址 GRE的目标地址| ESP| GRE | 源IP 目标IP | data | ESP |...

![GRE%20over%20IPSEC%20ec9aa840c5454982a5e7bd389e04bd85/image1.png](GRE%20over%20IPSEC/image1.png)

老命令:

起Tunnel:

R2(config)#interface tunnel 23

R2(config-if)#ip address 23.1.1.2 255.255.255.0 <===起tunnel地址

R2(config-if)#tunnel source 12.1.1.2

R2(config-if)#tunnel destination 13.1.1.3

- -------------------------------------------

R3(config)#interface tunnel 23

R3(config-if)#ip address 23.1.1.3 255.255.255.0

R3(config-if)#tunnel source 13.1.1.3

R3(config-if)#tunnel destination 12.1.1.2

宣告:

R2(config-if)# router eigrp 90 <===不用宣告连接Internet的接口

R2(config-router)#no auto-summary

R2(config-router)#network 100.2.2.0 0.0.0.255 <====宣告内部网络

R2(config-router)#network 23.1.1.0 0.0.0.255 <====宣告tunnel地址

- ----------------------------------------------

R3(config-if)#router eigrp 90

R3(config-router)#no auto-summary

R3(config-router)#network 100.3.3.0 0.0.0.255

R3(config-router)#network 23.1.1.0 0.0.0.255

IKE Phase I Policy:

R2(config)#crypto isakmp policy 1

R2(config-isakmp)#authentication pre-share

R2(config-isakmp)#hash md5

R2(config-isakmp)#encryption 3des

R2(config-isakmp)#group 2

R2(config)#crypto isakmp key 0 ccnp address 13.1.1.3 <===使用物理口地址

- ----------------------------------------------------

R3(config)#crypto isakmp policy 1

R3(config-isakmp)#authentication pre-share

R3(config-isakmp)#hash md5

R3(config-isakmp)#encryption 3des

R3(config-isakmp)#group 2

R3(config)#crypto isakmp key 0 ccnp address 12.1.1.2

IPSec Phase II Policy:

R2(config)#crypto ipsec transform-set cisco esp-des esp-sha-hmac

模式:

R2(cfg-crypto-trans)#mode tunnel <===使用"tunnel"模式

或者: R2(cfg-crypto-trans)#mode transport <=== 使用"transport"模式.(只有"Peer source Peer destination"等于"GRE的源地址 GRE的目标地址"的特例中,才能使用,且只能在25系列路由器上做)

R2(config)#ip access-list extended gre

R2(config-ext-nacl)#**permit gre any any** <===对条件可以抓的更细(any:可换成GRE的SOURCE/DESTINATION)

R2(config)#crypto map huawei 10 ipsec-isakmp

R2(config-crypto-map)#set peer 13.1.1.3 <===使用物理口地址

R2(config-crypto-map)#set transform-set cisco

R2(config-crypto-map)#set pfs

R2(config-crypto-map)#match address gre

- ----------------------------------------------

R3(config)#crypto ipsec transform-set cisco esp-des esp-sha-hmac

R3(cfg-crypto-trans)#mode tunnel

R3(config)#ip access-list extended gre

R3(config-ext-nacl)#permit gre any any <===对条件可以抓的更细

R3(config)#crypto map huawei 10 ipsec-isakmp

R3(config-crypto-map)#set peer 12.1.1.2

R3(config-crypto-map)#set transform-set cisco

R3(config-crypto-map)#set pfs

R3(config-crypto-map)#match address gre

Apply VPN Configuration

R2(config)#interface ethernet 0/0

R2(config-if)#crypto map huawei

- -----------------------------------

R3(config)#interface ethernet 0/0

R3(config-if)#crypto map huawei

新命令: 不需要感兴趣流,不需要MAP,不需要set peer

... <===之前的都一样

IPSec Phase II Policy:

R2(config)#crypto ipsec transform-set cisco esp-des esp-sha-hmac

R2(config)#crypto ipsec profile GREPRO <===只有26系列以上路由器才支持

R2(ipsec-profile)#set transform-set cisco

Apply VPN Configuration

R2(config)#interface tunnel 23

R2(config-if)#tunnel protection ipsec profile GREPRO

R2#show crypto ipsec sa <===可以查看协商成"transport"模式