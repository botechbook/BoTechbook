# Configuring CBWFQ and LLQ

Configuring CBWFQ and LLQ

2011年7月7日

15:38

**CBWFQ（Class-Based Weighted Fair Queuing，基于类别的加权公平队列）解决了PQ、CQ和WFQ的一些局限性。可以创建用户自定义的类别，并为所有类别分配专属队列，每个队列都有用户自定义的最小保证带宽，而且在有可用带宽时队列可以使用更多的带宽。**

**与PQ不同，CBWFQ中的任何队列都不会没有处理机会。**

**与PQ和CQ不同，在CBWFQ中不需要使用复杂的访问列表为不同队列定义流量类别。**

**与WFQ不同，WFQ不允许创建用户自定义类别，但是CBWFQ可以这么做，而且可以不用使用访问列表。**

**WFQ与CBWFQ的区别，使用这种MQC配置方式的CBWFQ，因为可以自定义类，而早期的直接在接口下打入fair-queue那种方式是WFQ，那里面只能基于事先分好的优先级去自动分配带宽，不如CBWFQ灵活性大。**

**但与WFQ和CQ相似，CBWFQ并没有解决实时应用（如VoIP）的低延时的需求，而LLQ可以实现这一点**

**关于CBWFQ**

![Configuring%20CBWFQ%20and%20LLQ%20ede13d7fceee4a908cfa179fdd6e6222/image1.png](Configuring%20CBWFQ%20and%20LLQ/image1.png)

**CBWFQ最多可以创建64个用户自定义队列，每个队列都是有保证带宽和最大包门限的FIFO队列，一旦队列达到其最大包门限，就会产生尾丢弃，为了避免出现尾部丢弃，可以在队列上应用WRED。**

**注意：WRED可以同时用于CBWFQ的一个或多个队列，但不能直接应用于接口。**

**除了用户可以定义的64个队列以外，CBWFQ还有一个class-default（默认队列）的队列，所有与已定义类别都不匹配的数据包被分配到该队列中。**

**64个用户自定义队列和class-default队列都属于FIFO队列，但也可以将class-default队列定义成WFQ队列，如果没有为class-default队列类别定义预留带宽，则该队列将使用接口的剩余带宽。**

**CBWFQ也是根据权值为每个队列提供调度和带宽保证功能，而这个权值是根据带宽值，带宽百分比或带宽剩余百分比计算得到的。**

**1.带宽：使用bandwidth命令。该带宽将从接口最大预留带宽中的未用预留带宽部分剪掉。默认情况下，接口的最大预留带宽是接口全部可用带宽的75%，但也可以人为的修改这个值，使用命令max-reserved-bandwidth修改。**

**2.带宽百分比：使用bandwidth percent命令。公式是：最大预留带宽*百分比**

**3.带宽剩余百分比：使用命令bandwidth remaining percent。**

**公式是：可用带宽*百分比**

**可用带宽=（接口带宽*最大可预留带宽比例）-所有已预留的带宽之和**

**注意：在policy-map中，不能给一个类别使用bandwidth命令，一个类别使用bandwidth percent命令，也就是说，要么全用bandwidth，要么全用bandwidth-precent**

**注意：之所以将最大可预留带宽设置为75%，是因为剩余25%的接口带宽用于网络开销，包括二层开销（如CDP）。虽然允许用户修改该默认值，但一定要小心。**

**对于queue-limit命令：**

**该命令用于修改每个队列的包的最大数量，超过了就尾丢弃，默认是64.**

**案例一：**

**需求：对于DSCP为EF或者是AF41的流量，设置带宽为100kbps,队列长度为128.对于源于10.1.1.0/24网段的telnet流量设置带宽为20kbps，队列长度为64.对于从接口fa0/0进入的流量，设置带宽200kbps，队列长度为128.**

**关键配置：**

**class-map match-any A**

**match ip dscp ef**

**match ip dscp af41**

**access-list 110 permit tcp 10.1.1.0 0.0.0.255 any eq telnet**

**class-map match-all B**

**match access-group 110**

**class-map match-all C**

**match input-interface FastEthernet0/0**

**policy-map PM**

**class A**

**bandwidth 100**

**queue-limit 128**

**class B**

**bandwidth 20**

**class C**

**bandwidth 200**

**queue-limit 128**

**interface s1/1**

**service-policy output PM**

**关于LLQ**

**LLQ相当于CBWFQ+改进后的PQ**

**LLQ是在CBWFQ中引入了PQ，加了一个优先级队列，当优先级队列中有数据包的时候，就会先传优先级队列，但是LLQ对PQ的一个改进的地方就是，可以设置优先级队列的带宽，如果在传输优先级队列时超过指定的带宽，则会传其他的队列，这点可以防止优先级队列将其他队列饿死，所以说是改进的PQ。**

**Router(config-pmap-c)#priority {bandwidth}**

**刚才在CBWFQ中使用bandwidth命令是用于定义普通队列的，但是如果改用priority，配置的就是低延时队列，凌驾于CBWFQ的上面**

**案例二：使用LLQ给视频，音频流量提供保留带宽**

![Configuring%20CBWFQ%20and%20LLQ%20ede13d7fceee4a908cfa179fdd6e6222/image2.jpg](Configuring%20CBWFQ%20and%20LLQ/image2.jpg)

**需求：交换机与路由器之间起单臂路由，如图所示**

**1.PC1从一台视频服务器中收看视频，此视频流量已经打上DSCP标签AF41，要求对于此流量从fa0/0.1子接口出去的时候优先传输，并且设置带宽为100kbps，并且将标签重新设置成CoS4，以便交换机做QoS用，其余流量尽量占用带宽**

**class-map match-all VEDIO_IN**

**match ip dscp af41**

**policy-map PM1**

**class VEDIO_IN**

**priority 100**

**set cos 4**

**class class-default**

**fair-queue**

**2.PC2从一台音频服务器中收听广播，此音频流量已经打上DSCP标签EF，要求对于此流量从fa0/0.2子接口出去的时候优先传输，并且设置带宽为30kbps，并且将标签重新设置成CoS5，以便交换机做QoS用，其余流量尽量占用带宽**

**关键配置：**

**class-map match-all AUDIO_IN**

**match ip dscp ef**

**policy-map PM2**

**class AUDIO_IN**

**priority 30**

**set cos 5**

**class class-default**

**fair-queue**

**然后应用到子接口就可以了，有些IOS版本不支持应用到子接口，但知道个大概的概念就可以了**