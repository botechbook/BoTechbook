# Introducing Congestion Avoidance

Introducing Congestion Avoidance

2011年7月7日

15:50

**拥塞避免技术有两种：**

**1.尾丢弃**

**2.RED（包括变体WRED和CBWRED）**

**尾丢弃有3个缺点：**

**1.造成TCP同步**

**2.造成TCP饿死**

**3.没有区分的丢弃**

**关于TCP同步**

![Introducing%20Congestion%20Avoidance%20c5c648eb5da04efeab1d6c4dbfd5ded5/image1.jpg](Introducing%20Congestion%20Avoidance/image1.jpg)

**1.多个TCP会话在不同的时间开始**

**2.TCP窗口的大小增加**

**3.尾丢弃造成多个会话的包同时丢弃**

**4.TCP的会话的窗口在同一时间同时增加**

**这个就叫做同步**

**当同时增加到让接口产生尾丢弃，又同时减少，然后再次同时增加，这样的结果就是接口突然很多很多数据包，突然很少的包。**

关于主动流（aggressive flows）

主动流就是那种流量很大的流，会侵占其他的流的空间

关于TCP饿死

**由于尾丢弃是指当软件的队列满了以后，再来的数据包就会被丢弃。这种没有区分的丢弃会让一些TCP的流一直窗口都很小，这种就是TCP饿死**。

用图片说明一下就是

![Introducing%20Congestion%20Avoidance%20c5c648eb5da04efeab1d6c4dbfd5ded5/image2.jpg](Introducing%20Congestion%20Avoidance/image2.jpg)

图一

![Introducing%20Congestion%20Avoidance%20c5c648eb5da04efeab1d6c4dbfd5ded5/image3.jpg](Introducing%20Congestion%20Avoidance/image3.jpg)

图二

![Introducing%20Congestion%20Avoidance%20c5c648eb5da04efeab1d6c4dbfd5ded5/image4.jpg](Introducing%20Congestion%20Avoidance/image4.jpg)

图三

![Introducing%20Congestion%20Avoidance%20c5c648eb5da04efeab1d6c4dbfd5ded5/image5.jpg](Introducing%20Congestion%20Avoidance/image5.jpg)

图四

**关于RED**

**RED是为了解决尾丢弃所造成的问题才出现的**

**RED是一种在队列慢之前就随机丢包的机制**

关于RED Profiles（RED简档）

![Introducing%20Congestion%20Avoidance%20c5c648eb5da04efeab1d6c4dbfd5ded5/image6.jpg](Introducing%20Congestion%20Avoidance/image6.jpg)

RED Profiles其实就是RED的配置参数

RED的配置参数有：**最小门限、最大门限**、**MPD**（Mark Probability Denominator，标记概率分母）

**1.平均队列大小<最小门限：不丢弃（No drop）**

**2.平均队列大小>最大门限：尾丢弃（Full drop，Tail drop）**

**3.最小门限<平均队列大小<最大门限：随机丢弃（Random drop），**如果MPD=10，那么此时到达的包被丢弃的概率就是10%

![Introducing%20Congestion%20Avoidance%20c5c648eb5da04efeab1d6c4dbfd5ded5/image7.jpg](Introducing%20Congestion%20Avoidance/image7.jpg)

**注意这两幅图的平均链路利用率：使用RED以后会比使用尾丢弃要高**

关于WRED

WRED与RED是一样的。唯一的区别是WRED引入了IP优先级或者DSCP值来区分丢弃策略，可以为不同的IP优先级或DSCP值设定不同的流量简档，从而对不同的优先级报文提供不同的丢弃特性。

![Introducing%20Congestion%20Avoidance%20c5c648eb5da04efeab1d6c4dbfd5ded5/image8.jpg](Introducing%20Congestion%20Avoidance/image8.jpg)

注意上图：WRED也是使用的平均队列长度

上图的说明：当数据包到达时，首先基于包的IP优先级或者DSCP值来识别流量简档，然后基于流量简档和当前的平均队列长度，确定该包什么时候会被随机丢弃。如果包没有被随机丢弃，那么仍然有可能会被尾丢弃。所有未被丢弃的包都将进入队列（FIFO）进行排队。此时当前的平均队列长度也会被更新。

注意：WRED不能与PQ、CQ、WFQ应用于同一接口，但是在CBWFQ中可以把WFQ与WRED连用

当应用过WRED后用show interface []命令后可以看到Queueing strategy: random early detection(RED)

WRED默认认为非IP流量是优先级为0的流量

关于WRED的配置：

基于IP Precedence的配置

1、启用WRED:

Router(config-if)#random-detect

2、设置WRED丢弃数据包的最小门限、最大门限、MPD

Router(config-if)#random-detect precedence {precedence|rsvp} {min max mark}

基于DSCP

1.使用IP DSCP 来配置WRED:

Router(config-if)#random-detect dscp-based

2.设置WRED丢弃数据包的最小门限、最大门限、MPD

Router(config-if)#random-detect dscp {dscp} {min max mark}

案例一：基于IP Precedence的WRED的配置

关键配置：

interface Serial1/1

ip address 192.168.1.1 255.255.255.0

random-detect

random-detect precedence 0 10 25 10

random-detect precedence 1 20 35 10

random-detect precedence 2 15 25 10

random-detect precedence 3 25 35 10

random-detect precedence 4 1 2 1

random-detect precedence 5 35 40 10

random-detect precedence 6 30 40 10

random-detect precedence 7 30 40 10

案例二：基于DSCP的WRED的配置

interface Serial1/0

ip address 192.168.2.1 255.255.255.0

random-detect dscp-based

random-detect dscp 34 10 30 10

random-detect dscp 36 20 30 10

random-detect dscp 38 25 40 10

random-detect dscp 46 30 60 10

关于CBWRED

将WRED应用到CBWFQ就会得到CBWRED

基于类的CBWRED和WRED是一样的

在CBWFQ中应用WRED可以改变队列默认的尾丢弃的行为

案例三：在CBWFQ中加入基于IP Precedence的WRED

需求：

1.Class **mission-critical** is marked with IP precedence values 3 and 4， and should get 30% of interface bandwidth.When the queue of **mission-cirtical** is between 26 and 40，the packet with precedence 3 will drop with 10%；and if the queue is between 28 and 40，the packet with precedence 4 will drop with 10%。

2.Class bulk is marked with IP precedence values 1 and 2 and should get 20% of interface bandwidth.When the queue of bulk is between 22 and 36，the packet with precedence 1 will drop with 10%；and if the queue is between 24 and 36，the packet with precedence 2 will drop with 10%。

3.All other traffic should be per-flow fair-queued.

关键配置：

class-map mission-critical

match ip precedence 3 4

class-map bulk

match ip precedence 1 2

policy-map PM

class mission-critical

bandwidth percent 30

random-detect

random-detect precedence 3 26 40 10

random-detect precedence 4 28 40 10

class bulk

bandwidth percent 20

random-detect

random-detect precedence 1 22 36 10

random-detect precedence 2 24 36 10

class class-default

fair-queue

random-detect

注意：在CBWFQ中，WRED不能与WFQ的queue-limit命令连用。也就是说random-detect和queue-limit是互斥的。为什么呢？因为random-detect会根据定义的最大门限进行尾丢弃，而queue-limit后设定的值也是进行尾丢弃的值，同一尾丢弃不能用两个参数来决定，所以不能连用。

案例四：在CBWFQ中加入基于DSCP的WRED

![Introducing%20Congestion%20Avoidance%20c5c648eb5da04efeab1d6c4dbfd5ded5/image9.jpg](Introducing%20Congestion%20Avoidance/image9.jpg)

需求：

1.Class **mission-critical** is marked using DSCP AF2 and should get 30% of interface bandwidth.and drop the packet from the picture above。

2.Class bulk is marked using DSCP AF1 and should get 20% of interface bandwidth.and drop the packet from the picture above。

3.All other traffic should be per-flow fair-queued.

关键配置：

class-map mission-critical

match ip dscp af21 af22 af23

match ip dscp af21 af22 af23

match ip dscp af21 af22 af23

match ip dscp af21 af22 af23

match ip dscp af21 af22 af23

class-map bulk

match ip dscp af11 af12 af13

policy-map PM

class mission-critical

bandwidth percent 30

random-detect dscp-based

random-detect dscp af21 32 40 10

random-detect dscp af22 28 40 10

random-detect dscp af23 24 40 10

class bulk

bandwidth percent 20

random-detect dscp-based

random-detect dscp af11 32 40 10

random-detect dscp af12 28 40 10

random-detect dscp af13 24 40 10

class class-default

fair-queue

random-detect dscp-based

关于show命令

show policy-map interface s1/1