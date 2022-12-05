# Introducing Traffic Policing and Shaping

Introducing Traffic Policing and Shaping

2011年7月7日

15:39

**流量监管与流量整形是流量调节机制。一般来说，这些流量调节机制主要用于网络边缘。**

**流量整形一般是缓存那些超出策略/协定规定的超额流量，一般用于出方向**

**流量监管或者是丢弃超额流量或者是将超额流量标记为低优先级（重标记），一般用于出方向或入方向。**

**所以，总结一下：**

**流量监管=丢弃或者重标记**

**流量整形=缓存 -----所以只能用在出方向**

**入向做不了shaping和queuing，因为这两个要用到buffer，buffer只有在出向才有，但是在思科12000+的设备上，入向也有了buffer**

**如下图：**

![Introducing%20Traffic%20Policing%20and%20Shaping%20575624207beb4193b38b187aa5a7dfb5/image1.jpg](Introducing%20Traffic%20Policing%20and%20Shaping/image1.jpg)

**由于流量监管仅仅是丢弃或重标记超额流量，所以不会给正常（非超额）流量引入时延。**

**流量整形可以缓存超额流量并基于策略规范有规则地传送这部分流量。流量整形有多种变化形式，包括基于类别的流量整形、FRTS、GTS（Generic Traffic Shaping，通用流量整形）。需要注意的是，Cisco IOS的流量整形工具没有流量重标记功能。**

**关于SLA（Service Level Agreement，服务级别协定）：SLA是企业与服务提供商之间签订的一种合约，主要涉及带宽、流量速率、可靠性、可用性、QoS和计费等内容。**

**关于流量监管：**

**流量监管的主要目的及功能如下：**

**1.将流量速率降低到物理接入速率之下**

**2.对每种流量类别进行速率限制**

**3.重标记流量**

**关于流量整形：**

**流量整形的主要目的及功能如下：**

**1.降低通过WAN服务（如帧中继或ATM）发送到其他站点的流量速率**

**2.遵从订购的速率**

**3.以不同的速率发送不同类别的流量**

**流量监管和流量整形一般用于哪些场合？**

**答：服务提供商一般在网络边缘设备（从客户端设备接受流量的接口或向客户端设备发送流量的接口）上实施流量监管机制。**

**而流量整形则一般用于CE设备(Customer Edge,客户边缘)向服务提供商发送流量的输出接口**

**如下图：**

**服务提供商设备 s1/1 ------------------------------------------s1/0 CE**

**在这个接口实行流量监管 在这个接口实行流量整形**

**流量监管和流量整形的异同点？**

**答：1.流量监管和流量整形都是流量监管机制，有时对不同流量类别进行分开测量**

**2.流量监管可以应用于出流量和入流量（相对于接口而言），而流量整形则仅用于出流量**

**3.流量整形缓存超额流量并按照预配置速率发送超额流量，而流量监管是丢弃或重标记超额流量**

**4.流量整形需要内存来缓存超额流量，会带来可变时延和抖动。而流量监管则不需要额外的内存资源，不会产生可变时延**

**5.流量监管丢包后某些类型的流（如基于TCP的流）会重传被丢弃的流量，非TCP流量可能会重传比被丢弃流量更多的流量**

**6.流量监管可以重标记流量，而流量整形不可以重标记流量**

**7.流量整形的配置可以基于网络状况和网络信号，而流量监管则无法响应网络状况和网络信号 -----这一条是针对与帧中继流量整形而言的**

**如下图：**

![Introducing%20Traffic%20Policing%20and%20Shaping%20575624207beb4193b38b187aa5a7dfb5/image2.jpg](Introducing%20Traffic%20Policing%20and%20Shaping/image2.jpg)

![Introducing%20Traffic%20Policing%20and%20Shaping%20575624207beb4193b38b187aa5a7dfb5/image3.jpg](Introducing%20Traffic%20Policing%20and%20Shaping/image3.jpg)

**流量监管和流量整形的前提是先测量出流量速率，问题来了，如何测量流量速率？**

**答：Cisco设备上的操作系统可以利用桶和令牌来测量流量速率**

**令牌桶算法（token bucket algorithm）**

在实施QOS策略时，可以将用户的数据限制在特定的带宽，当用户的流量超过额定带宽时，超过的带宽将采取其它方式来处理。要衡量流量是否超过额定的带宽，网络设备并不是采用单纯的数字加减法来决定的，也就是说，比如带宽为100K，而用户发来的流量为110K，网络设备并不是靠110K减去100K等于10K，就认为用户超过流量10K。网络设备

衡量流量是否超过额定带宽，需要使用令牌桶算法来计算。下面详细介绍令牌桶算法机制：

当网络设备衡量流量是否超过额定带宽时，需要查看令牌桶，而令牌桶中会放置一定数量的令牌，一个令牌允许接口发送或接收1bit数据（有时是1 Byte数据），当接口通过1bit数据后，同时也要从桶中移除一个令牌。当桶里没有令牌的时候，任何流量都被视为超过额定带宽,只有当桶中有令牌时，数据才可以通过接口。令牌桶中的令牌不仅仅可以被移除，同样也可以往里添加，所以为了保证接口随时有数据通过，就必须不停地往桶里加令牌，由此可见，往桶里加令牌的速度，就决定了数据通过接口的速度。因此，我们通过控制往令牌桶里加令牌的速度从而控制用户流量的带宽。而设置的这个用户传输数据的速率被称为承诺信息速率（CIR），通常以秒为单位。比如我们设置用户的带宽为1000 bit每秒，只要保证每秒钟往桶里添加1000个令牌即可。

**例：**

将CIR设置为8000 bit/s，那么就必须每秒将8000个令牌放入桶中，当接口有数据通过时，就从桶中移除相应的令牌，每通过1 bit，就从桶中移除1个令牌。当桶里没有令牌的时候，任何流量都被视为超出额定带宽，而超出的流量就要采取额外动作。

每秒钟往桶里加的令牌就决定了用户流量的速率，这个速率就是CIR，但是每秒钟需要往桶里加的令牌总数，并不是一次性加完的，一次性加进的令牌数量被称为Burst size（Bc），如果Bc只是CIR的一半，那么很明显每秒钟就需要往桶里加两次令牌，每次加的数量总是Bc的数量。

还有就是加令牌的时间，Time interval（Tc），Tc表示多久该往桶里加一次令牌，而这个时间并不能手工设置，因为这个时间可以靠CIR和Bc的关系计算得到， Bc/ CIR= Tc。

**例：**

如果CIR是8000,Bc是4000，那就是每秒加两次，Tc就是4000/8000=0.5，也就是0.5秒，即500 ms。

如果Bc设为2000，那Tc就是2000/8000=0.25, 也就是250 ms。

**单速双色**

单速指的是只有一个CIR速率，双色指的是会产生出两种行为，即符合和超出

在单速双色的令牌桶算法中，只存在一个令牌桶，并且流量只会出现两种结果，即符合CIR（conform）和超出CIR（exceed）。

**例：**

将CIR设置为8000 bit，每一秒都会往桶里加8000个令牌，在一秒钟结束后，没有用完的令牌会被全部清空，由下一秒重新加入。

**如**

第1秒，加入8000令牌，用户使用5000后，剩余3000被清空

第2秒，加入8000令牌，用户使用6000后，剩余2000被清空

第3秒，加入8000令牌，用户使用8000后，没有剩余

第4秒，加入8000令牌，用户使用7000后，剩余1000被清空

从以上过程可以看出，用户每秒都可以使用8000令牌，也就是每秒速度均可达到8000 bit，而无论上一秒钟是否传过数据，这一秒都可以保持在8000 bit/s，并且如果每秒流量超过了8000后，超过的流量都会采取已经设定的动作。

**单速三色**

在单速三色的令牌桶算法中，使用两个令牌桶，用户每秒的可用带宽，总是两个桶的令牌之和，第一个桶的令牌机制和单速双色算法没有任何区别，关键在于第二个桶。第二个桶的令牌不能直接加入，只有当一秒钟结束后，第一个桶中存在剩余令牌时，这些剩余令牌就可以从第一个桶中被转移到第二个桶中。但不是第一个桶所有未用令牌都可以放入第二个桶，是有限制的，最大数量被称为 Excess Burst size（Be），由此可见，Be是不可能超过CIR的，因为第一个桶每秒的所有令牌就是CIR，即使所有令牌全部被移到第二个桶，Be最多也只能等于CIR而不能超过。而Be和Bc却毫无关系。需要注意的是，在每一秒结束时，如果用户没有将第二个桶的令牌用完，那么第二个桶的令牌也是要全部被清除的，第二个桶中的令牌，都是来自于上一秒第一个桶没用完的令牌。

注意：在单速双色模型中实际上也有类似于Be的概念，在下面的Be中提出

由于使用了两个桶，所以用户的流量也会出现三种结果：

小于或等于CIR（也就是符合CIR） （conform）

大于CIR并小于或等于CIR与Be之和（也就是符合两个桶令牌之和）（exceed）

超过CIR与Be之和（也就是超过两个桶令牌之和）（violate）

**例：**

将CIR设置为8000 bit，Be设置为2000，每一秒都会往第一个桶里加8000个令牌，每一秒结束后，所有第一个桶未使用完的令牌都将放入第二个桶，并且用户每一秒能使用的带宽总是两个桶之和。

**如：**

第一个桶令牌数   用户用掉的带宽数  第二个桶令牌数  用户可用带宽总数

第1秒          8000             6000             0               8000

第2秒          8000             7000             2000            10000

第3秒          8000             6000             1000            9000

第4秒          8000             9000             2000            10000

第5秒          8000             8000             0               8000

第6秒          8000             6000             0               8000

第7秒          8000             10000            2000            10000

**说明:**

在第1秒时，第一个桶加入CIR的数量8000个令牌后，第二个桶为空，所以用户可用带宽总数为8000。用户实际使用了6000；

在第2秒时，第一个桶加入8000个令牌后，由于上一秒用户实际使用了6000，所以第二个桶获得2000令牌，此时用户可用带宽为10000，用户实际用户了7000；

在第3秒时，第一个桶加入8000个令牌后，由于上一秒用户实际使用了7000，所以第二个桶获得1000令牌，此时用户可用带宽为9000，用户实际用户了5000；

在第4秒时，第一个桶加入8000个令牌后，由于上一秒用户实际使用了6000，所以第二个桶获得2000令牌，此时用户可用带宽为10000，用户实际用户了9000；

在第5秒时，第一个桶加入8000个令牌后，由于上一秒将第一个桶中令牌用光，所以第二个桶没有获得令牌，此时用户可用带宽为8000，用户实际用户了8000；

在第6秒时，第一个桶加入8000个令牌后，由于上一秒将第一个桶中令牌用光，所以第二个桶没有获得令牌，此时用户可用带宽为8000，用户实际用户了6000；

在第7秒时，第一个桶加入8000个令牌后，由于上一秒用户实际使用了6000，所以第二个桶获得2000令牌，此时用户可用带宽为10000，用户实际用户了10000；

从上面可以看出，第一个桶中的令牌数永远都是CIR的数量，而第二个令牌桶只能在上一秒第一个桶存在没有用完的令牌的情况下，才能够获得令牌，但获得令牌的最大数量不能超过Be。用户的流量也可以出现三种结果：

即小于或等于CIR,即小于8000，如6000

大于CIR并小于或等于CIR+Be，如9000

大于两个桶之后，如11000

要使用户在某一秒的速度能够达到CIR+Be，唯一的办法是用户在上一秒钟以低于CIR的速度传输。因此，用户不可能每一秒都以CIR+Be的速度传输。

**双速三色**

在单速三色的令牌桶算法中，用户若想要在某一秒以CIR+Be的速度传输，只能在上一秒钟以低于CIR的速度传输。因此，用户不可能每一秒都以CIR+Be的速度传输。而在双速三色的令牌桶算法中，同样使用两个令牌桶，然而这两个桶是相互独立的，并不会将第一个桶未用的令牌放入第二个桶。第一个桶与以往的算法相同，也就是每秒都有CIR的数量，而第二个桶可以直接设置为CIR+Be之和，称为PIR，也就是说第二个桶总是比第一个桶要大，用户的流量总是以第二个桶的大小传输，而不用像单速三色的令牌桶算法中，需要在上一秒钟以低于CIR的速度传输。当用户的数据通过接口时，总是先检查第二个桶的最大速率，即PIR，如果超出则采取动作，如果未超出，再检查是是否符合第一个桶的CIR，如果超出CIR，则采取相应动作，如果未超过，则正常传输。

虽然在双速三色的令牌桶算法中，直接设置两个速率，然而，用户可以直接以CIR+Be之和的速率进行传输，此外，还可以判断出三种结果。

**TC实际上是亚秒级时间片，之所以有这样的设定是为了是流量在单位秒得时间内能够平滑的流动。**

![Introducing%20Traffic%20Policing%20and%20Shaping%20575624207beb4193b38b187aa5a7dfb5/image4.jpg](Introducing%20Traffic%20Policing%20and%20Shaping/image4.jpg)

**如果待发送数据量（以字节为单位）大于令牌数，则称该流量是超额的（exceeding），在流量超额的情况下，不从令牌桶中移除令牌，但需要执行超额操作（exceed action），或者是缓存超额流量，或者是稍后再发送超额流量（在实施了流量整形的情况下），或者是丢弃超额流量，或者是标记超额流量（在实施了流量监管的情况下）。**

**如下图：**

![Introducing%20Traffic%20Policing%20and%20Shaping%20575624207beb4193b38b187aa5a7dfb5/image5.jpg](Introducing%20Traffic%20Policing%20and%20Shaping/image5.jpg)

**注意点：对于单桶模型来说，在桶满的时候令牌就会溢出，导致令牌浪费。**

**Cisco设备的操作系统仅在有活动流量的时候才向桶中丢入令牌，而不是连续不断地向桶中丢入令牌，而且在桶满时，会丢弃刚刚丢入桶中的令牌。**

**关于令牌桶方案如下：**

![Introducing%20Traffic%20Policing%20and%20Shaping%20575624207beb4193b38b187aa5a7dfb5/image6.jpg](Introducing%20Traffic%20Policing%20and%20Shaping/image6.jpg)

**CIR（committed information rate）：承诺信息速率**

**Bc（committed burst size）：承诺突发量**

**Be（excess burst size）：超出突发量**

**Tc：承诺时间间隔**

**这几个参数之间的关系是：CIR(比特/秒)=Bc（比特）/Tc（秒）**

**网络管理员一般会指定CIR和Bc的值，Tc值由系统自动计算得到。**

**Bc值越大，表示允许的突发数据量就越大；大的Bc值能够节约大量令牌（就是不丢弃超过Bc的令牌，所以Bc越大越能节省令牌）。**

**关于Be**

**注意：基于最传统的技术，也就是在接口下配置rate-limit这种方式，提出的Be的概念，注意这时使用的模型实际上是单速双色的，后面基于MQC配置方式的监管技术实际上是使用的单速三色模型，或者是双速三色模型，那个Be的概念参见令牌桶算法。**

**如果令牌桶(小Bc)中有足够的令牌，则分组被传输出去；如果令牌不够，则超出突发量（Be）将发挥作用。有两种形式的令牌桶方案:**

**1.标准令牌桶：Be=Bc**

**也就是说令牌桶没有扩展突发功能，其扩展突发量等于Bc，在这种情况下，当令牌不够用时将丢弃分组。**

**2.具有扩展突发功能的令牌桶：Be>Bc**

**与标准令牌桶方案不同，具有扩展突发能力的令牌桶允许暂借更多的令牌。**

**实际上这种基于单速双色模型的传统CAR技术中Be的概念只是指的允许临时单次添加更多的令牌，因为令牌是每Tc时间添加一次的，每次添加Bc个，所以如果在该亚秒级时间片（Tc）中如果添加的令牌Bc的数量不足以满足临时的数据量，则可以在该Tc时间内多加点令牌，当然不能超过Be-Bc，只要在一秒时间内总量不超过CIR就可以了。**

**关于流量监管的配置：**

**流量监管的实现使用CAR技术，其实可以把流量监管等同于CAR（区分出传统的CAR和MQC方式下的CAR），就像拥塞管理等同于队列技术一样**

**1.在接口下配置：**

**接口下这种配置方式实际上使用的是CAR**

**CAR是CISCO IOS软件中提供的最古老的管制工具，古老原因有：**

**CAR与DiffServ RFC不兼容。**

**没有基本百分比的带宽规范和分层管制**

**CAR不能使用MQC语法。**

**NBAR不能用在CAR中**

**基本配置：**

**注意：在接口下这种配置方式是传统的CAR技术，使用的模型是单速双色模型**

**Router(config-if)#rate-limit {input|output} {CIR Bc Be} conform-action {action} exceed-action {action}**

**针对于DSCP值的配置：**

**Router(config-if)#rate-limit {input|output} [dscp dscp] {CIRBc Be} conform-action {action} exceed-action {action}**

**针对于ACL的配置：**

**Router(config-if)#rate-limit {input|output}access-group {ACL} {CIR Bc Be} conform-action {action} exceed-action {action}**

**针对于限速ACL的配置：**

**第一句话：写ACL匹配感兴趣流**

**第二句话：Router（config-if）#rate-limit {input|output} access-group rate-limit {ACL} {CIR Bc Be} conform-action {action} exceed-action {action}**

**2.在MQC中的配置**

**注意：在MQC的配置方式中，实际上使用的是单速三色或者是双速单色模型**

**典型的单速三色模型：**

**policy-map RFC2697-POLICER**

**class class-default**

**police cir 256000 bc 8000 be 8000**

**conform-action set-dscp-transmit af31**

**exceed-action set-dscp-transmit af32**

**violate-action set-dscp-transmit af33**

**典型的双速三色模型：**

**policy-map RFC2698-POLICER**

**class class-default**

**police cir 8000 bc 1000 pir 10000 be 2000**

**conform-action set-dscp-transmit af31**

**exceed-action set-dscp-transmit af32**

**violate-action set-dscp-transmit af32**

**Router(config-pmap-c)#police {CIR Bc Be} conform-action {action} exceed-action {action} [violate-action {action}]**

**案例一：接口下基本配置**

**interface Hssi0/0/0**

**description 45Mbps to R1**

**rate-limit input 15000000 2812500 2812500 conform-action transmit exceed-action drop**

**ip address 200.200.14.250 255.255.255.252**

**rate-limit output 15000000 2812500 2812500 conform-action transmit exceed-action drop**

High－Speed Serial Interface（HSSI） 高速串行接口（HSSI），是一个由Cisco System 和T3plus Networking公司共同推出的串行接口标准。它的最高数据传输率为52Mbps，最远的传输距离为15米（50英尺）。

**解释：**

**hssi高速串口是45M的带宽，但是ISP的接入承诺信息速率为15M，并且限定普通突发大小为2812500，最大突发大小也是2812500超过这个值的话，就丢掉数据包**

**案例二:针对于DSCP值的配置**

**需求：对IP DSCP值为1的出站流量进行限速（基于DSCP值）**

**interface Serial1**

**ip address 10.0.0.1 255.255.255.252**

**rate-limit output dscp 1 20000000 24000 32000 conform-action transmit exceed-action drop**

**案例三：针对于ACL的配置**

**案例拓扑：**

![Introducing%20Traffic%20Policing%20and%20Shaping%20575624207beb4193b38b187aa5a7dfb5/image7.png](Introducing%20Traffic%20Policing%20and%20Shaping/image7.png)

**案例要求：**

**1、所有的www流量限制速率为20Mbps，承诺突发量为24000字节，超出突发量为32000字节。遵从流量设置ip优先级为5,不遵从的流量设置IP优先级为0(尽力而为的传输)。**

**2、所有的ftp流量限制速率为10Mbps，承诺突发量为24000字节，超出突发量为32000字节。遵从流量设置ip优先级为5,不遵从的流量就丢弃。**

**3、其他剩余流量限制到8Mbps，承诺突发量为16000byte,最大突发大小为24000byte；遵从策略的流量设ip precedence为5,超出的流量扔包。**

**关键配置：**

**access-list 101 per tcp any any eq www**

**access-list 102 per tcp any any eq ftp**

**interface hssi0/0/0**

**desription 45Mbps to R2**

**ip address 10.1.0.9 255.255.255.0**

**rate-limit output accees-group 101 20000000 24000 32000 conform-action set prec-transmit 5 exceed-action set-prec-transmit 0**

**rate-limit output access-group 102 10000000 24000 32000 conform-action set-prec-tranmit 5 exceed-action drop**

**rate-limit output 8000000 16000 24000 conform-action set-prec-transmit 5 exceed-action drop**

**案例四：针对于限速ACL的配置**

**需求：对IP优先级为3 的出站流量进行限速:**

**access-list rate-limit 10 3 （基于限速ACL）**

**interface Serial1**

**ip address 10.0.0.1 255.255.255.252**

**rate-limit output access-group rate-limit 10 20000000 24000 32000 conform-action transmit exceed-action drop**

**案例五：针对于限速ACL的配置**

**需求：对于源mac地址是00e0.34b0.7777的流量进行限速**

**access-list rate-limit 100 00e0.34b0.7777 （基于限速ACL）**

**interface Fddi2/1/0**

**ip address 200.200.6.1 255.255.255.0**

**rate-limit input access-group rate-limit 100 80000000 64000 80000 conform-action transmit exceed-action drop**

**案例六：结合NBAR和CAR技术**

**需求：对HTTP流量进行限速，凡是下载的图像格式包括jpg，jpeg和gif的，速率限制为100kbps，超出的丢弃。**

**关键配置：**

**ip cef**

**class-map match-any HTTP**

**match protocol http url "*.jpeg"**

**match protocol http url "*.gif"**

**policy-map PM**

**class HTTP**

**police 100000 conform-action transmit exceed-action drop**

**interface s1/0**

**ip nbar protocol-discovery**

**service-Policy input PM**

**案例七：MQC中的CAR技术**

**需求：限制来自192.168.0.0/24的进站数据包的平均速率为8000bps，突发流量(Bc)为2000字节，额外突发流量(Be)为4000字节。对突发流量和额外突发流量分别采取转发和设置QoS组ID为25的策略;对违反突发流量和额外突发流量的数据流量采取丢弃的策略:**

**access-list 10 permit 192.168.0.0 0.0.0.255**

**class-map match-all A**

**match access-group 10**

**policy-map PM**

**class A**

**police 8000 2000 4000 conform-action transmit exceed-action set-qos-transmit 25 violate-action drop**

**interface Serial1**

**ip address 172.16.0.1 255.255.255.252**

**service-policy input PM**

**关于CAR的使用限制：**

**1.CAR只能对IP流量限速**

**2.CAR不支持快速以太网通道（FastEtherChannel）**

**3.CAR不支持隧道接口**

**4.CAR不支持ISDN PRI接口**

**小结一下：**

**1.R0(config-if)#rate-limit input ?**

**<8000-2000000000> Bits per second //直接跟速率**

**access-group Match access list //可以跟ACL，或者是限速ACL**

**dscp Match dscp value //针对与DSCP做限速**

**qos-group Match qos-group ID //针对于QoS组做限速**

**2.R0(config-if)#rate-limit input 8000 1000 2000 conform-action ?**

**continue scan other rate limits**

**drop drop packet**

**set-dscp-continue set dscp, scan other rate limits**

**set-dscp-transmit set dscp and send it**

**set-mpls-exp-imposition-continue set exp during imposition, scan other rate**

**limits**

**set-mpls-exp-imposition-transmit set exp during imposition and send it**

**set-prec-continue rewrite packet precedence, scan other rate**

**limits**

**set-prec-transmit rewrite packet precedence and send it**

**set-qos-continue set qos-group, scan other rate limits**

**set-qos-transmit set qos-group and send it**

**transmit transmit packet**

**3.R0(config-if)#$input 8000 1000 2000 conform-action transmit exceed-action ?**

**continue scan other rate limits**

**drop drop packet**

**set-dscp-continue set dscp, scan other rate limits**

**set-dscp-transmit set dscp and send it**

**set-mpls-exp-imposition-continue set exp during imposition and send it**

**set-mpls-exp-imposition-transmit set exp during imposition and send it**

**set-prec-continue rewrite packet precedence, scan other rate**

**limits**

**set-prec-transmit rewrite packet precedence and send it**

**set-qos-continue set qos-group, scan other rate limits**

**set-qos-transmit set qos-group and send it**

**transmit transmit packet**

**小结：conform-action和transmit-action后跟的选项是一样的**

**注意点：在接口下的rate-limit没有violation-action**

**在policy-map下配置的时候有violation-action**

**关于流量整形的配置：**

**流量整形采用3种技术**

**1.GTS（Generic Traffic Shaping，通用流量整形），可以对不规则或不符合预定流量特性的流量进行整形，以利于网络上下游之间的带宽匹配-------为什么叫做通用流量整形呢？原因是在各种网络中都可以用这种方法流量整形，比如在帧中继中，即使可以用帧中继特有的方法整形，但是GTS也是可以实现的**

**2.DTS（7200vip卡才支持）**

**3.FRTS：专门用于帧中继的流量整形**

**配置整形**

> 要对特定的流量进行整形，从而限制其可用带宽，方法为先匹配特定的流量，再使用令牌桶算法将流量限制在额定的带宽，但是对于超额的流量不需要做其它处理，因为这些超额的流量是需要被缓存的。下面分别介绍三种整形技术的配置方法：
> 

**Generic Traffic Shaping (GTS)**

![Introducing%20Traffic%20Policing%20and%20Shaping%20575624207beb4193b38b187aa5a7dfb5/image8.png](Introducing%20Traffic%20Policing%20and%20Shaping/image8.png)

**说明:**以上图为例，将R1到目标网络10.1.1.0/24的流量整形到CIR为8000 bit，而超额的流量不需要做其它处理，这些超额的流量默认被缓存；R1到目标网络20.1.1.0/24的流量正常通过。

**1．匹配R1到目标网络10.1.1.0/24的流量**

**（1）通过ACL匹配到网络10.1.1.0/24的流量**

r1(config)#access-list 100 permit ip any 10.1.1.0 0.0.0.255

**（2）class-map调用ACL中的流量**

r1(config)#class-map net10

r1(config-cmap)#match access-group 100

**2．整形到目标网络10.1.1.0/24的流量**

**(1)在policy-map中调用class-map的流量并整形带宽**

r1(config)#policy-map SSS

r1(config-pmap)#class net10

r1(config-pmap-c)#shape average 8000 1000 0

**说明:**整形的CIR为8000bit,虽然建议Bc为CIR的1/100，但Bc请不要小于1000，否则整形不会生效，而Be可以为0。

**3．应用策略到接口**

**（1）将policy-map应用到R1的S0/0出方向**

r1(config)#int s0/0

r1(config-if)#service-policy output SSS

**4．测试效果**

**（1）测试R1到目标网络20.1.1.0/24的流量**

r1#ping 20.1.1.2 size 800 repeat 20

Type escape sequence to abort.

Sending 20, 800-byte ICMP Echos to 20.1.1.2, timeout is 2 seconds:

!!!!!!!!!!!!!!!!!!!!

Success rate is 100 percent (20/20), round-trip min/avg/max = 404/406/409 ms

r1#

**说明:**因为并没有对R1到目标网络20.1.1.0/24的流量进行整形，所以当数据包每个以800字节通过时，一切正常，并且速度正常。

**（2）测试R1到目标网络10.1.1.0/24的流量**

r1#ping 10.1.1.2 size 800 repeat 20

Type escape sequence to abort.

Sending 20, 800-byte ICMP Echos to 10.1.1.2, timeout is 2 seconds:

!!!!!!!!!!!!!!!!!!!!

Success rate is 100 percent (20/20), round-trip min/avg/max = 405/406/409 ms

r1#

**说明:**因为R1到目标网络10.1.1.0/24的流量被整形为8000bit每秒，所以当数据包每个以800字节通过时，并没有丢包，但是速度却不能超过8000bit每秒，此效果在文本下无法看见，需要自己在实验时查看。

**（3）查看policy-map参数**

r1#show policy-map interface

Serial0/0

Service-policy output: SSS

Class-map: net10 (match-all)

20 packets, 16080 bytes

5 minute offered rate 1000 bps, drop rate 0 bps

Match: access-group 100

Traffic Shaping

Target/Average   Byte   Sustain   Excess    Interval  Increment

Rate           Limit  bits/int  bits/int  (ms)      (bytes)

8000/8000      125    1000      0         125       125

Adapt  Queue     Packets   Bytes     Packets   Bytes     Shaping

Active Depth                         Delayed   Delayed   Active

-      0         20        16080     19        15276     no

Class-map: class-default (match-any)

29 packets, 16197 bytes

5 minute offered rate 0 bps, drop rate 0 bps

Match: any

r1#

**说明:**从输出中可以看出被整形的数据包个数以及其它一些参数。

**Frame Relay Traffic Shaping (FRTS)**

![Introducing%20Traffic%20Policing%20and%20Shaping%20575624207beb4193b38b187aa5a7dfb5/image8.png](Introducing%20Traffic%20Policing%20and%20Shaping/image8.png)

**说明:**以上图为例，将R1的出口流量整形到CIR为8000 bit，而超额的流量不需要做其它处理，这些超额的流量默认被缓存。

**1．配置map-class实现FRTS**

**（1）配置map-class**

r1(config)#map-class frame-relay TTT

r1(config-map-class)#frame-relay cir 8000

r1(config-map-class)#frame-relay bc 1000

r1(config-map-class)#frame-relay be 0

**说明:**FRTS的工具map-class不能针对特定流量整形，而只能对接口所有流量整形。

**2．应用FRTS**

**（1）在帧中继接口上开启整形**

r1(config)#int s0/0

r1(config-if)#frame-relay traffic-shaping

**（2）应用map-class**

r1(config-if)#frame-relay interface-dlci 102

r1(config-fr-dlci)#class TTT

**说明:**map-class可以单独应用到某条PVC上，也可以应用在整个接口上。

**3．测试效果**

**（1）测试R1到目标网络10.1.1.0/24的流量**

r1#ping 10.1.1.2 size 800 repeat 20

Type escape sequence to abort.

Sending 20, 800-byte ICMP Echos to 10.1.1.2, timeout is 2 seconds:

!!!!!!!!!!!!!!!!!!!!

Success rate is 100 percent (20/20), round-trip min/avg/max = 405/406/409 ms

r1#

**说明:**因为R1的出口流量被整形到CIR为8000bit每秒，所以当数据包每个以800字节通过时，并没有丢包，但是速度却不能超过8000bit每秒，此效果在文本下无法看见，需要自己在实验时查看。

**Class-Based Shaping**

![Introducing%20Traffic%20Policing%20and%20Shaping%20575624207beb4193b38b187aa5a7dfb5/image8.png](Introducing%20Traffic%20Policing%20and%20Shaping/image8.png)

**说明:**以上图为例，将R1的出口流量整形到CIR为8000 bit，而超额的流量不需要做其它处理，这些超额的流量默认被缓存。Class-Based Shaping和FRTS一样只能对所有流量整形。class-default

**1．配置GTS**

**（1）policy-map中调用class-map的流量并整形带宽**

r1(config)#policy-map ccc

r1(config-pmap)#class class-default

r1(config-pmap-c)#shape average 8000 1000 0

**说明:**Class-Based Shaping只支持对class-default的整形，即对所有流量整形。

**2．配置Class-Based Shaping**

**（1）在map-class中调用GTS**

r1(config)#map-class frame-relay FFF

r1(config-map-class)#service-policy output ccc

**3．应用Class-Based Shaping**

**（1）在帧中继接口上应用Class-Based Shaping**

r1(config)#int s0/0

r1(config-if)#frame-relay class FFF

**说明:**在应用Class-Based Shaping时，接口上必须禁用frame-relay traffic shaping。

**4．测试效果**

**（1）测试R1到目标网络10.1.1.0/24的流量**

r1#ping 10.1.1.2 size 800 repeat 20

Type escape sequence to abort.

Sending 20, 800-byte ICMP Echos to 10.1.1.2, timeout is 2 seconds:

!!!!!!!!!!!!!!!!!!!!

Success rate is 100 percent (20/20), round-trip min/avg/max = 405/406/409 ms

r1#

**说明:**因为R1的出口流量被整形到CIR为8000bit每秒，所以当数据包每个以800字节通过时，并没有丢包，但是速度却不能超过8000bit每秒，此效果在文本下无法看见，需要自己在实验时查看。

**接口直接开启整形**

除了以上的整形方法之外，接口上可以直接配置流理整形，这也是对所有流量生效

![Introducing%20Traffic%20Policing%20and%20Shaping%20575624207beb4193b38b187aa5a7dfb5/image8.png](Introducing%20Traffic%20Policing%20and%20Shaping/image8.png)

**说明:**以上图为例，将R1的出口流量整形到CIR为8000 bit。

**1．开启接口流量整形**

**（1）在R1的S0/0上开启整形**

r1(config)#int s0/0

r1(config-if)#traffic-shape rate 8000 1000 0

**2．测试效果**

**（1）测试R1到目标网络10.1.1.0/24的流量**

r1#ping 10.1.1.2 size 800 repeat 20

Type escape sequence to abort.

Sending 20, 800-byte ICMP Echos to 10.1.1.2, timeout is 2 seconds:

!!!!!!!!!!!!!!!!!!!!

Success rate is 100 percent (20/20), round-trip min/avg/max = 405/406/409 ms

r1#

**说明:**因为R1的出口流量被整形到CIR为8000bit每秒，所以当数据包每个以800字节通过时，并没有丢包，但是速度却不能超过8000bit每秒，此效果在文本下无法看见，需要自己在实验时查看。

**（2）查看接口整形**

r1#sh traffic-shape statistics

Acc. Queue Packets   Bytes     Packets   Bytes     Shaping

I/F               List Depth                     Delayed   Delayed   Active

Se0/0                   0     20        16080     19        15276     no

r1#

**说明:**可以看到被整形的数据包个数。

**向前显示拥塞通知（FECN）：当网络发生拥塞的时候，向目的设备发送一个FECN数据包，来通知拥塞**

**BECN：当网络发生拥塞的时候，向源路由器发送一个BECN数据包，来通知拥塞。同时按25%的比例降低数据包发送速率，降到1/2，但是如果此时网络不拥塞了，会立即回到原来的100%。**