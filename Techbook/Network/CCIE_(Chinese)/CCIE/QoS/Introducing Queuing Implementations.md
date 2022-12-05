# Introducing Queuing Implementations

Introducing Queuing Implementations

2011年7月7日

15:36

**当接口的输入速率超出了输出速率时，就会产生拥塞。**

**有3种情况可能会产生拥塞：**

**1.速率不匹配问题（speed mismatch problem）：从高速接口进入网络设备的流量必须通过低速接口输出，这样就会在低速接口上产生拥塞**

**2.汇聚问题（aggregation problem）：从多个接口来的流量汇聚到一个没有足够容量的接口时会产生拥塞**

**3.合流问题（confluence problem）：连接多个流量流而导致的接口出现拥塞，个人感觉是帧中继，多个spoke汇聚到了hub会产生拥塞**

**永久性的解决拥塞问题的方法是增大容量，而不是部署排队技术，排队技术仅仅是针对临时性拥塞的一种解决方案。**

**每个接口的排队机制都包括硬件组件和软件组件。**

**如果硬件队列不是拥塞，则不会将数据包保持在软件队列中，此时数据包会被直接交换到硬件队列中，并基于FIFO机制被快速的发送到传输介质上。**

**如果硬件队列出现拥塞，数据包会被保持在软件队列中进行处理，并基于软件排队规则释放到硬件队列中。**

**关于硬件队列**

**硬件队列只有FIFO一种**

**硬件队列过大或者过小都不好，过大则会引入FIFO延迟，过小则效率太低，增加了许多不必要的CPU中断。**

**许多因素（如硬件平台，软件版本，二层介质，在接口上应用了特殊的软件排队机制等）都会影响硬件队列的大小。某些平台还可以通过易行的QoS机制自动调整硬件队列的大小。**

**IOS可以基于接口的配置带宽有效的确定硬件队列的尺寸**

**在有必要的时候可以通过使用tx-ring-limit命令设置硬件队列的大小。可以通过命令show controllers serial查看接口的硬件队列的大小。**

**注意：子接口和软件接口（如隧道和拨号接口）都没有专用的硬件队列，而是使用主接口的队列。**

**关于软件队列**

**平时说的队列技术特指软件队列，常见的软件队列有FIFO，PQ，CQ，RR，WRR，FQ,WFQ，CBWFQ，LLQ。**

**关于FIFO**

![Introducing%20Queuing%20Implementations%203f411368b43b44cda20b10112ff78747/image1.jpg](Introducing%20Queuing%20Implementations/image1.jpg)

**对于FIFO队列，数据包的类别、优先级和类型都不起任何作用。**

**大于2.048Mbps的接口默认是这个队列。**

**关于PQ**

![Introducing%20Queuing%20Implementations%203f411368b43b44cda20b10112ff78747/image2.png](Introducing%20Queuing%20Implementations/image2.png)

**PQ提供了4种可用队列，分别为高优先级队列，中优先级队列，正常优先级队列和低优先级队列。**

**管理人员需要将数据包分配到不同的队列中，或者默认进入正常优先级队列。一般都采用访问列表来定义哪些数据包可以进入哪些类型的r队列。**

**只要高优先级队列中有数据包，PQ调度器就始终仅转发高优先级中的数据包。**

**只有高优先级队列为空时，才会去处理中优先级队列中的数据包。**

**只有高、中优先级队列为空时，才会去处理正常优先级队列中的数据包。**

**只有高、中、正常优先级队列为空时，才会去处理低优先级队列中的数据包。**

**也就是说，在高优先级队列中的数据包都被处理完并转发到硬件队列之前，中、正常、低优先级队列中的所有数据包都没有被处理的机会。**

**PQ使用的限制和缺点：**

**1.由于PQ是静态配置的，因此它不能适应网络结构的改变。**

**2.由于数据包要经过处理器卡的分类，因此PQ对数据包的转发速度要比FIFO慢。**

**3.PQ不支持隧道接口。**

**4.PQ的一个非常显著的缺点就是如果高优先级的队列没有发送完成，低优先级的数据将永远不会被发送，因此会造成低级别的队列中的数据被饿死。**

**注意：虽然PQ只有在高优先级队列数据包全部传完的情况下，才会传下一个队列，但是可以限制每个队列一次性传输的最大数据包个数，当某个队列传输的数据包达到最大数量之后，无论是否还有数据包，都必须传递下一个队列。**

**关于PQ的配置**

**配置4步：**

**1.定义优先级列表，可以基于协议或基于进站接口**

**基于协议：**

**Router(config)#priority-list *list-number* protocol *protocol-name*{high|medium|normal|low}**

**基于接口：**

**Router(config)#priority-list *list-number* interface *slot/number* {high|medium|normal|low}**

**2.定义默认的优先级队列，未分类的流量默认被分配进该队列，优先级队列默认是normal，这句可以不写，如果不写默认队列就是normal队列：**

**Router(config)#priority-list {list} default {high|medium|normal|low}**

**3.定义每个队列中数据包的最大个数，由高到低，默认是20，40，60和80.可以更改：**

**Router(config)#priority-list {list} queue-limit {high-limit medium-limit normal-limit low-limit}**

**4.把优先级列表应用到接口上：**

**Router(config-if)#priority-group {list}**

**查看命令：**

**show queue [interface]：显示接口队列信息**

**show queueing priority：显示PQ列表信息**

**案例一：**

**需求：接口s1/1轻度拥塞的时候使用PQ队列，给从接口fa0/0进入的流量设置为高优先级级别，源自10.1.1.0/24网段，目标地址为20.1.1.0/24网段的Telnet流量设置为正常优先级别，WWW的流量设置为低优先级别，其他流量为中等优先级别；并且设置高、中、正常、低优先级别的流量的队列深度分别为30，40，50，60**

**关键配置：**

**priority-list 1 interface FastEthernet0/0 high**

**access-list 110 permit tcp 10.1.1.0 0.0.0.255 20.1.1.0 0.0.0.255 eq telnet**

**priority-list 1 protocol ip normal list 110**

**priority-list 1 protocol ip low tcp www**

**priority-list 1 default medium**

**priority-list 1 queue-limit 30 40 50 60**

**int s1/1**

**priority-group 1**

**案例二：基于长度指定分组的优先次序**

**某企业发现，其WAN链路上关键任务的交易通信和分组小于100字节的VoIP通信的延迟很长，而且变化不定。该公司希望路由器收到分组小于100字节的分组，就立即处理，而不管其他等待调度的通信，路由器只有在队列中没有小于100字节的分组时，才处理其他通信。**

**关键配置：**

**priority-list 1 protocol ip high lt 100**

**int s1/1**

**priority-group 1**

**关于RR**

**RR（Round-Robin，循环）是一种完全不同于PQ的排队规则，简单的RR有多个队列，流量会被分配到不同的队列中，RR调度器在完成一个队列的一个数据包后，会接着处理另一个队列中的一个数据包，一直下去，最后又从第一个队列开始再次循环。**

**关于WRR**

**RR的一个改进版本就是WRR（Weighted Round-Robin，加权循环），WRR允许用户为每个队列分配一个权值，根据该权值，每个队列都能获得一定的接口带宽，但不再均等。**

**WRR的一个例子就是CQ，在CQ中可以配置必须为每个队列处理的字节数。**

**注意WRR和CQ中的权值其实就是一个字节数，是个数目，而在WFQ中的权值是用优先级计算出来的，可见对于不同的队列权值的概念一点也不相同。**

**关于加权**

**CQ(WRR)的加权是字节数**

**WFQ的加权是优先级**

**CBWFQ的加权是带宽**

**关于CQ**

![Introducing%20Queuing%20Implementations%203f411368b43b44cda20b10112ff78747/image3.jpg](Introducing%20Queuing%20Implementations/image3.jpg)

**CQ对报文进行分类，最多可以分16类，分别属于CQ的16个队列中的一个，即队列编号1到16.注意还有一个0队列，0队列是超级优先队列，路由器总是先把0队列中的报文发送完然后才处理1到16号队列，所以0号队列一般作为系统队列，通常把实时性要求高的交互式协议和链路层协议报文放到0号队列中。**

**CQ采用的是轮询调度。**

**为了使每个队列分配一定的带宽，必须为每个队列定义一定字节的数据包（也就是权值，或叫做权重）。**

**关于CQ的配置**

**1.定义每个队列中数据包的最大个数：**

**Router(config)# queue-list** *list-number* **queue** *queue-number* **limit** *limit-number*

**limit-number：指的是队列里面的数量，默认是20个，范围是0到32767**

**2.定义每个队列中每一轮传输的字节数（定义权重）：**

**Router(config)#queue-list** *list-number* **queue** *queue-number* **byte-count** *bytes*

**bytes：指的就是每一轮此队列传输的字节数，默认是1500字节**

**3.将数据包分配到CQ队列中，可以基于协议，也可以基于进站接口**

**基于协议**

**Router(config)#queue-list** *list-number* **protocol** *protocol queue-number queue-keyword*

*keyword-value*

**基于接口**

**Router(config)#queue-list** *list-number* **interface** *interface queue-number*

**4.定义默认的CQ队列，未分类的流量默认被分配到该队列：**

**Router(config)#queue-list** *list-number* **default** *queue-number*

**5.应用到接口**

**Router(config-if)#custom-queue-list** *list-number*

**查看命令**

**show queue [interface]:显示接口队列信息**

**show queueing custom：显示CQ列表信息**

**案例三：**

**对于s1/1接口采用CQ队列，将IPv6的流量放入到1号队列中，将IPv4的流量放入到2号队列中，将IPX的流量放入到3号队列中，1号队列分配15000字节，2号队列分配3500字节，3号队列分配1500字节，将2号队列设置为默认队列。**

**关键配置：**

**queue-list 1 protocol ipv6 1**

**queue-list 1 protocol ip 2**

**queue-list 1 protocol ipx 3**

**queue-list 1 queue 1 byte-count 15000**

**queue-list 1 queue 2 byte-count 3500**

**queue-list** *1* **default** *2*

**int s1/1**

**custom-queue-list 1**

**800:2400:800**

**案例四：**

**某网络管理员想给协议A、B、C分别分配20%、60%和20%的带宽。他发现平均而言，协议A的分组长为400字节，协议B的分组长度600字节，而协议C的分组长度为800字节。为了使用定制队列来实现这个功能，必须为每个协议队列指定合适的字节数以得到预期的带宽分配。A、B、C分别使用tcp目标端口4028，4029，4030**

**做法：**

**设A队列的字节数为x**

**B队列的字节数为y**

**C队列的字节数为z**

**则 {【x/400向上取整】*400}：{【y/600向上取整】*600}：{【z/800向上取整】*800}=20%：60%：20%**

**化简得**

**【x/400取整】*400=800**

**【y/600取整】*600=2400**

**【z/800取整】*800=800**

**最终：x取800，y取2400，z取800**

**此时满足条件**

**关键配置：**

**queue-list protocol ip 1 tcp 4028**

**queue-list protocol ip 2 tcp 4029**

**queue-list protocol ip 3 tcp 4030**

**queue-list 1 queue 1 byte-count 800**

**queue-list 1 queue 2 byte-count 2400**

**queue-list 1 queue 3 byte-count 800**

**int s1/1**

**custom-queue-list 1**

**基本的WRR和CQ有一个缺点：如果分配给队列的字节数（权值）与接口的MTU大小接近的话，那么在队列之间分配带宽的计划很可能完全达不到规划的效果。**

**例如，假设某接口的MTU为1500字节，建立了3个队列，并且希望在每个周期为每个队列处理3000个字节，如果某队列有一个1450字节的数据包和两个1500字节的数据包，那么这3个数据包都会在一个周期内被转发出去，这样一个周期内为该队列处理的字节数就达到了4450字节，与所规划的3000字节相差很远。**

**另一方面，如果分配给队列的字节数（权值）远大于接口的MTU，那么将会增大排队延迟。**

**所以说权值太大不好，太小也不好。**

**关于CQ与CBWFQ的比较**

**虽然定制队列可以为每个通信类预留带宽，如同CBWFQ一样，但是相比之下，CBWFQ有很多优点：**

**1.CBWFQ设置更简单，直接**

**2.就带宽分配而言，RSVP依赖于CBWFQ**

**3.在CBWFQ中，对于每个通信类除了分配最小带宽外，还可以应用分组丢弃策略，例如RED（Random Early Detection）**

**4.不受16个定制队列的限制，CBWFQ支持64个类**