# Control Plane Policing (CoPP)

Control Plane Policing (CoPP)

2011年8月2日

22:18

Control Plane Policing (CoPP)被称为控制面板策略，控制面板策略这个特性让用户通过配置QOS过滤来管理控制面板中的数据包，从而保护路由器和交换机免受DOS的攻击，控制面板可以无论在流量多大的情况下都能管理数据包交换和协议的状态情况。

> 在控制面板中，只能通过MQC配置常规的QOS，并且out方向的QOS并不是所有IOS都支持，请自行检查，其中配置的QOS策略中，只有drop和policy两个动作可以使用。而且NBAR功能也不能很好的支持。当在控制面板中配置QOS后，不用在接口下应用该策略，因为控制面板下的策略对所有接口生效。
> 
> 
> **配置**
> 

![Control%20Plane%20Policing%20(CoPP)%20f05dc3b533f847de99114beb399b9cf4/image1.png](Control%20Plane%20Policing%20(CoPP)/image1.png)

**1.测试R2到R1的数据流量**

r2#ping 12.1.1.1

Type escape sequence to abort.

Sending 5, 100-byte ICMP Echos to 12.1.1.1, timeout is 2 seconds:

!!!!!

Success rate is 100 percent (5/5), round-trip min/avg/max = 1/2/4 ms

r2#

**说明：**R1在没有使用任何QOS的情况下，通信正常

**2.配置QOS**

**说明：**这里配置QOS丢弃所有的包，以作测试用。

**（1）配置匹配源自R2的数据**

r1(config)#access-list 2 permit 12.1.1.2

r1(config)#class-map r2

r1(config-cmap)#match access-group 2

r1(config-cmap)#exit

**（2）配置丢弃源自R2的数据**

r1(config)#policy-map copp

r1(config-pmap)#class r2

r1(config-pmap-c)#drop

**3.将QOS应用于COPP**

r1(config)#control-plane

r1(config-cp)#service-policy input copp

**4.测试到R1的通信**

r2#ping 12.1.1.1

Type escape sequence to abort.

Sending 5, 100-byte ICMP Echos to 12.1.1.1, timeout is 2 seconds:

.....

Success rate is 0 percent (0/5)

r2#

**说明：**可以看到，并没有将所配置的QOS用于接口，只用在了控制面板下，所有接口都执行控制面板下的QOS策略，从而数据包被丢弃了，网络不通。

> 
>