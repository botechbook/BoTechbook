# Identifying Methods for Implementing QoS

Identifying Methods for Implementing QoS

2011年7月7日

15:28

**QoS的四种配置方法：**

**1. 传统CLI的配置方法（Legacy CLI）**

**2. MQC（Modular QoS CLI，模块化QoS）-----重点**

**3. Cisco AutoQoS**

**4. Cisco SDM QoS wizard**

**补充一句：无论是AutoQos还是SDM，最终的代码还是MQC**

**传统的CLI配置方法需要在每个接口下打入很多配置命令，配置量非常的大且容易出错，现在基本不用了。**

**MQC配置3步走：**

**1. 分类-----使用Class Map**

**2. 定义策略-----Policy Map**

**3. 应用到接口-----Service-Policy**

**口诀：分类，做策略，应用到接口**

**我们的带宽大小总共有10M，现在利用Qos设置http流量为2M，迅雷为1M，QQ 1M，现在的问题是，其它的流量会占用多少带宽？**

**MQC案例一：对于HTTP流量设置带宽2M，其他流量设置带宽6M**

**配置：**

**class-map HTTP**

**match protocol http ！使用的是NBAR抓出Http流量**

**policy-map PM**

**class HTTP**

> bandwidth 2000
> 

**class class-default ！表示其他流量**

> bandwidth 6000
> 

**interface s1/0**

**service-policy output PM**

**注意点：只要是设置带宽，一定要应用在out方向。**

**MQC案例二：对于IP优先级为5或者DSCP为EF的流量是VoIP流量，要求优先传输，且分配带宽100k，对于目标为10.1.10.20，10.1.10.40的tcp流量设置带宽25k，其他流量尽量占用带宽。**

**配置：**

**access-list 100 permit ip any any precedence 5**

**access-list 100 permit ip any any dscp ef**

**access-list 101 permit tcp any host 10.1.10.20**

**access-list 101 permit tcp any host 10.1.10.40**

**class-map VoIP**

**match access-group 100**

**class-map Application**

**match access-group 101**

**policy-map QoS-Policy**

**class VoIP**

> bandwidth 100
> 

**class Application**

> bandwidth 25
> 

**class class-default**

> fair-queue
> 

**int s1/0**

**service-policy output QoS-Policy**

**关于MQC的show命令**

**1. show class-map：显示class-map**

**2. show policy-map：显示policy-map**

**3. show policy-map interface xxx ：显示接口下挂的policy-map**

**AutoQoS部分其实说白了就是用一句或者几句命令完成QoS的配置，这个是思科私有的。具体内容到后面有。**

**使用SDM配置QoS的方法：做个实验看一下就可以了**

**SDM提供的向导包括：**

**1. 防火墙和NAT**

**2. IPS**

**3. IPSec VPNs**

**4. QoS**

**5. Routing**