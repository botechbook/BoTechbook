# Zone-Based Policy Firewall

Zone-Based Policy Firewall

2011年8月2日

22:16

在Cisco IOS版的路由器中，可以实施一种防火墙功能，被称为Zone-Based Policy Firewall（基于区域策略的防火墙），也就是说这种防火墙是基于zone的，是基于区域的。既然是基于区域的防火墙，那么配置的防火墙策略都是在数据从一个区域发到另外一个区域时才生效，在同一个区域内的数据是不会应用任何策略的。而要配置这些策略，方法像使用MQC来配置QOS一样配置防火墙策略，但是两个的配置方法并不完全一致，因为双方的格式会有一些不同。

要完全理解Zone-Based Policy Firewall的工作，必须理解以下一些参数：

Zone

Zone就是区域，因为区域化防火墙是基于区域的，策略也只能在区域间传递数据时才生效**，在区域内是不生效的，**所以我们就可以将需要使用策略的接口划入不同的区域，这样就可以应用我们想要的策略。但是，有时某些接口之间可能不需要彼此使用策略，那么这样的接口只要划入同一个区域，它们之间就可以任意互访了。**Zone是应用防火墙策略的最小单位**，一个zone中可以包含一个接口，也可以包含多个接口。

Security Zones

Security Zones和上面的zone并没有区别，意思完全相同，只是因为Security Zones是指应用了策略的zone，而且Security Zones应该是要包含接口的。

在配置好Security Zones之后，当一个接口属于Security Zones的成员时，所有发到此接口和从此接口发出去的（但发到路由器和路由器发给它的除外）数据是默认被丢弃的，也就是说区域间的接口默认是不能通信的，数据将全部被丢弃。

Virtual Interfaces也可以作为Security Zones 的成员，在将Virtual Interfaces划入Security Zones 时，使用interface virtual-template。

特别的是，如果一个接口不属于任何一个zone，那么这个接口永远也不可以和任何zone的任何接口通信。

以下图解释通信过程：

> 
> 

![Zone-Based%20Policy%20Firewall%2030bcb988cf224e4f973d35a669d3ec53/image1.png](Zone-Based%20Policy%20Firewall/image1.png)

> 
> 

R2和R3属于区域zone1

R4属于区域zone2

R5不属于任何区域

默认的通信权限为：

R2和R3可以自由通信，

Zone1的R2和R3不能和zone2的R4互访，因为双方属于不区zone，必须明确配置策略允许。

而R5永远不能和任何路由器通信，因为它不属于任何区域，即使策略也做不到。

Zone-Pairs

因为在Security Zones之间的所有数据默认是全部被丢弃的，所以必须配置相应的策略来允许某些数据的通过。要注意，同区域的接口是不需要配置策略的，因为他们默认就是可以自由访问的，我们只需要在区域与区域之间配置策略，而配置这样的区域与区域之间的策略，必须定义从哪个区域到哪个区域，即必须配置方向，比如配置从Zone1到Zone2的数据全部被放行。可以看出，Zone1是源区域，Zone2是目的区域。配置一个包含源区域和目的区域的一组策略，这样的一个区域组，被称为**Zone-Pairs**。因此可以看出，一个Zone-Pairs，就表示了从一个区域到另一个区域的策略，而配置一个区域到另一个区域的策略，就必须配置一个Zone-Pairs，并加入策略。

当配置了一个区域到另一个区域的策略后，如果策略动作是inspect，则并不需要再为返回的数据配置策略，因为返回的数据是默认被允许的。

> 如果有两个zone，并且希望在两个方向上都应用策略，比如zone1到 zone2 或zone2 到 zone1,就必须配置两个zone-pairs ,就是每个方向一个zone-pairs。
> 

有时可以将self zone 即作源又作目的。self zone 是system-defined zone，即系统定义的zone，它是没有接口的。当zone-pair 包含self zone时，被应用的策略只对发到路由器和路由器发出的数据生效，通过路由器中转的数据不生效。

> 路由器上最好有两个zone来做策略，其中不包含self zone。
> 

策略

当接口被划入不同的zone之后，想要相互通信，就必须配置策略，再将配置好的策略应用于Zone-Pairs，因为一个Zone-Pairs就表示了一个区域到另一个区域的策略情况。

在为zone之间配置策略，使用的方法类似于用MQC配置QOS，但格式会有略微的差异。配置策略的方法为先使用Class Map匹配出指定的数据，然后再利用Policy Map调用Class Map匹配到的数据，做出相应的策略动作，最终将Policy Map应用于Zone-Pairs。下面分别针对Zone-Based Policy Firewall中的Class Map和Policy Map来做详细介绍。

3/4层Class Maps和Policy Maps

因为Class Map可以匹配OSI中第三层数据和第四层数据，也可以匹配第七层应用层数据，但是匹配三四层数据和匹配第七层数据是完全不一样的，我们把匹配第三四层数据的Class Maps和Policy Maps称为顶级Class Maps和顶级Policy Maps。他们与普通MQC中的Class Map和Policy Map的区别在于，顶级Class Maps和顶级Policy Maps分别表示为inspect class maps和inspect policy maps，而除了顶级Class Maps和顶级Policy Maps可以用在zone-pair中，其它统统不可以应用于zone-pair中。

顶级Policy Maps只能调用顶级Class Maps，并且能执行的动作只有：drop, inspect, police, pass, service-policy, and urlfilter。而顶级Class Maps只能匹配OSI第三层数据和第四层数据，无法匹配第七层数据。

MQC的Police Maps是在接口的，而inspect policy Maps是对zone-pair的，如果两个都配，zone-pair policer 是在接口进方向策略之后的，但在出策略之前。但两不冲突。

如果在inspect policy Maps中，默认没有被匹配到的数据是被丢弃。

7层Class Maps和Policy Maps

7层 class maps只能应用于7层Policy Maps，而7层Policy Maps也只能调用7层 class maps,并且7层Policy Maps不能直接应用于zone-pair中，只能嵌套于3/4层Policy Maps中。如果7层Policy Maps嵌套在3/4层Policy Maps中，那么3/4层Policy Maps称为parent policy，而7层Policy Maps称为child policy。

7层Class Maps和Policy Maps在配置时，必须指定协议名，比如HTTP协议，就配置Class Maps为class-map type inspect http，Policy Maps为policy-map type inspect http。

当7层Policy Maps没有匹配到的数据，默认是要返回让顶层Policy Maps来处理的。

Parameter Maps

是用来定义动作和标准的，分别用在policy map and 和class map中，有三种：

Inspect parameter map

URL Filter parameter map

Protocol-specific parameter map

Inspect parameter map是可选的，如果两级都有，低等级的有效。

URL Filter parameter map在URL过滤时需要，在34层policy MAP中

Protocol-specific parameter map 只有7层policy map需要。

**配置**

> 
> 

![Zone-Based%20Policy%20Firewall%2030bcb988cf224e4f973d35a669d3ec53/image2.png](Zone-Based%20Policy%20Firewall/image2.png)

> 
> 

**1.测试默认通信：**

**说明：**在没有配置防火墙的情况下，测试通信情况

**（1）测试R2到R3、R4、R5的ICMP通信情况：**

r2#ping 13.1.1.3

Type escape sequence to abort.

Sending 5, 100-byte ICMP Echos to 13.1.1.3, timeout is 2 seconds:

!!!!!

Success rate is 100 percent (5/5), round-trip min/avg/max = 72/144/244 ms

r2#ping 15.1.1.5

Type escape sequence to abort.

Sending 5, 100-byte ICMP Echos to 15.1.1.5, timeout is 2 seconds:

!!!!!

Success rate is 100 percent (5/5), round-trip min/avg/max = 72/147/368 ms

r2#ping 14.1.1.4

Type escape sequence to abort.

Sending 5, 100-byte ICMP Echos to 14.1.1.4, timeout is 2 seconds:

!!!!!

Success rate is 100 percent (5/5), round-trip min/avg/max = 40/157/352 ms

r2#

**说明：**可以看到，默认没有配置防火墙的情况下，ICMP畅通无阻。

**（2）测试R2到R4的telnet情况：**

r2#telnet 14.1.1.4

Trying 14.1.1.4 ... Open

r4>

**说明：**可以看到，默认没有配置防火墙的情况下，telnet畅通无阻。

**2.创建security zone**

**（1）创建zone1**

r1(config)#zone security zone1

r1(config-sec-zone)#

**（2）创建zone2**

r1(config)#zone security zone2

r1(config-sec-zone)#exi

**3.将接口划入zone**

**(1)将连R2和R3的接口划入zone1**

r1(config)#interface f0/0

r1(config-if)#zone-member security zone1

r1(config-if)#exit

r1(config)#int s1/0

r1(config-if)#zone-member security zone1

r1(config-if)#exit

**(2)将连R4的接口划入zone2**

r1(config)#int f0/1

r1(config-if)#zone-member security zone2

r1(config-if)#exit

**（3）查看结果**

r1#sh zone security

zone self

Description: System defined zone

zone zone1

Member Interfaces:

FastEthernet0/0

Serial1/0

zone zone2

Member Interfaces:

FastEthernet0/1

r1#

**说明：**结果与配置一致。

**4.测试通信**

**（1）测试zone1同区域的通信情况**

r2#ping 13.1.1.3

Type escape sequence to abort.

Sending 5, 100-byte ICMP Echos to 13.1.1.3, timeout is 2 seconds:

!!!!!

Success rate is 100 percent (5/5), round-trip min/avg/max = 56/188/408 ms

r2#

**说明：**在没有配置策略的情况下，同区域的通信不受限制

**（2）测试不通区域的通信情况**

r2#ping 15.1.1.5

Type escape sequence to abort.

Sending 5, 100-byte ICMP Echos to 15.1.1.5, timeout is 2 seconds:

.....

Success rate is 0 percent (0/5)

r2#

r2#ping 14.1.1.4

Type escape sequence to abort.

Sending 5, 100-byte ICMP Echos to 14.1.1.4, timeout is 2 seconds:

.....

Success rate is 0 percent (0/5)

r2#

**说明：**从结果中看出，从zone1到zone2，再到没有区域的网段，都是不通的。

**5.创建zone-pair**

**说明：**创建zone1 为源， zone2为目的的zone-pair

r1(config)#**zone-pair security ccie source zone1 destination zone2**

r1(config-sec-zone-pair)#exit

r1(config)#

**6.配置策略**

**（1）配置class-map匹配zone1到zone2的流量**

r1(config)#access-list 100 permit ip any host 14.1.1.4

r1(config)#class-map type inspect c1（type inspect c1 名字）

r1(config-cmap)#match access-group 100

**说明：**7层class-map能匹配的协议很少，所以用3/4层

**（2）配置policy-map允许zone1到zone2的流量**

r1(config)#policy-map type inspect p11

r1(config-pmap)#class type inspect c1

r1(config-pmap-c)#pass

r1(config-pmap-c)#exit

**说明：**动作pass是不会创建返回流量的。

**7.应用策略到zone-pair**

r1(config)#zone-pair security ccie source zone1 destination zone2

r1(config-sec-zone-pair)#service-policy type inspect p11

r1(config-sec-zone-pair)#

8.测试通信情况

r2#ping 14.1.1.4

Type escape sequence to abort.

Sending 5, 100-byte ICMP Echos to 14.1.1.4, timeout is 2 seconds:

.....

Success rate is 0 percent (0/5)

r2#

**说明：**已经应用了策略，zone1到zone2还是不通，因为动作pass没有创建返回的流量。

**9.创建zone2到zone1返回流量**

**（1）配置class-map匹配流量**

r1(config)#access-list 101 permit ip any any

r1(config)#class-map type inspect c2

r1(config-cmap)#match access-group 101

r1(config-cmap)#exit

**（2）配置policy-map允许流量**

r1(config)#policy-map type inspect p22

r1(config-pmap)#class type inspect c2

r1(config-pmap-c)#pass

r1(config-pmap-c)#exit

**（3）应用策略到返回流量**

r1(config)#zone-pair security ccsp source zone2 destination zone1

r1(config-sec-zone-pair)#service-policy type inspect p22

**10.测试zone1到zone2通信情况**

**（1）测试R2到R4的ICMP通信情况**

r2#ping 14.1.1.4

Type escape sequence to abort.

Sending 5, 100-byte ICMP Echos to 14.1.1.4, timeout is 2 seconds:

!!!!!

Success rate is 100 percent (5/5), round-trip min/avg/max = 36/112/360 ms

r2#

**说明：**ICMP通信正常。

**（2）测试R2到R4的telnet通信情况**

r2#telnet 14.1.1.4

Trying 14.1.1.4 ... Open

r4>

**(3)zone1到非zone的通信情况**

r2#ping 15.1.1.5

Type escape sequence to abort.

Sending 5, 100-byte ICMP Echos to 15.1.1.5, timeout is 2 seconds:

.....

Success rate is 0 percent (0/5)

r2#

**说明：**区域中和非区域是永远也不能通信的。

**11.配置3/4层class-map直接匹配协议**

**说明：**使用3/4层class-map直接匹配telnet协议，其它协议不管

**（1）配置class-map匹配telnet协议**

r1(config)#class-map type inspect c3

r1(config-cmap)#match protocol telnet

r1(config-cmap)#exit

**（2）配置policy-map允许telnet协议**

r1(config)#policy-map type inspect p33

r1(config-pmap)#class c3

r1(config-pmap-c)#inspect

r1(config-pmap-c)#

**说明：**这里的动作是inspect，所以不用创建返回流量的允许策略。

**（3）应用策略到zone-pair**

r1(config)#zone-pair security ccie source zone1 destination zone2

r1(config-sec-zone-pair)#service-policy type inspect p33

r1(config-sec-zone-pair)#exit

r1(config)#

**12.测试通信情况**

**（1）测试zone1到zone2的ICMP通信情况**

r2#ping 14.1.1.4

Type escape sequence to abort.

Sending 5, 100-byte ICMP Echos to 14.1.1.4, timeout is 2 seconds:

.....

Success rate is 0 percent (0/5)

r2#

**说明：**因为没有允许除telnet外的协议，所以ICMP不能通过。

**（2）测试telnet通信情况**

r2#telnet 14.1.1.4

Trying 14.1.1.4 ... Open

r4>

**说明：**因为策略明确允许telnet通过，所以telnet通信正常。

**(3)测试到同区域的ICMP**

r2#ping 13.1.1.3

Type escape sequence to abort.

Sending 5, 100-byte ICMP Echos to 13.1.1.3, timeout is 2 seconds:

!!!!!

Success rate is 100 percent (5/5), round-trip min/avg/max = 156/224/352 ms

r2#

**说明：**同区域中，不需要策略允许，所有通信正常。

**（4）测试到非区域的通信情况**

r4#telnet 12.1.1.2

Trying 12.1.1.2 ...

% Connection timed out; remote host not responding

r4#

**说明：**区域到不同区域的通信永远不能通过。