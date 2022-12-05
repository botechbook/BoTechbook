# EIGRP Lab

EIGRP实验

2011年6月21日

15:22

**关于命令router eigrp as-number**

**解释：在EIGRP和OSPF中的自治系统与边界网关协议（BGP）中的自治系统不是同一回事。在EIGRP和OSPF中，自治系统是一组运行相同路由协议的路由器。网络中可能有多个EIGRP自治系统（组）。**

**实验一：测试不同AS NUM能不能建起邻居。**

**关于命令network**

**R2(config)#router eigrp 90**

**R2(config-router)#network 12.1.1.0 0.0.0.255**

**R2(config-router)#network 2.2.0.0 255.255.0.0　（正/反掩码皆可）**

**关于命令ip hello-interval eigrp和ip hold-time eigrp**

**解释：接口下命令，用于修改hello时间和保持时间**

**实验二：测试Hello/Hold Timer不一致能不能建起邻居。**

**注意：本地设置hold-timer是显示在对端的邻居表中的**

**关于命令：metric weights**

**解释：用于修改K值**

**例子：**

**R3(config)#router eigrp 90**

**R3(config-router)#metric weights 0 1 1 1 0 0**

**关于命令no auto-summary命令**

**解释：默认情况下，EIGRP在主类网络边界会自动汇总，一般情况下要改变这种状况，使用此命令。**

**自动汇总有2个特点：**

**1.自动汇总会在路由表中产生一条指向Null0的汇总路由，指向Null0是为了防环**

**2.仅将本地的路由汇总成主类，对于收到的路由不做汇总，然后发出。**

![EIGRP%20Lab%2012b5b45018a04ba78a3af17608f17b04/image1.jpg](EIGRP%20Lab/image1.jpg)

**关于命令bandwidth、delay**

**解释：接口下命令,用于配置接口的配置带宽**

**delay 后面加的数值在show interface时看到的会乘以10**

**关于命令ip summary-address eigrp**

**解释：接口下命令，用于手工汇总，注意，EIGRP的手工汇总是在接口下做的，这点和RIP是一样的**

**手工汇总有3个特点：**

**1.本地必须有明细路由，才会从做汇总的接口发出汇总路由**

**2.直到明细的最后一条路由消失，汇总才会消失**

**3.汇总路由的Metric值取最小的Metric值**

**注意：EIGRP汇总的AD值（在本地路由器那条指向null0的路由）是5，传递出去的汇总路由管理距离还是90**

**EIGRP域间或外部重分布进RIP的路由AD值为170**

**域内是90**

**EIGRP 中的汇总管理距离为5 ，只在本地有效，在路由表中看不到，和指向null0一样的为了防环。**

**关于指向接口null0防环的假设：**

**假设本地没有这条指向null0的路由，邻居A恰好关闭了水平分割，则有可能接收这条汇总过的路由，并且指向邻居A。这时如果本地的明细路由没出问题的话，没什么影响。如果本地的某条明细丢失就麻烦了，则邻居A发过来的去往这条明细的数据包会被本地转发给A（走的是汇总路由），而A会转发给本地（还是汇总），环路产生。**

**验证此环路的产生：**

**汇总的时候将管理距离改的大于90，并且邻居关闭水平分割，然后让本地一条明细路由丢失。**

**注意：如果只是关闭邻居的水平分割，则只会产生暂时的环路，原因是本地接收了邻居的汇总路由后本地不再将这条路由发回给邻居（水平分割），所以最后邻居学不到汇总路由，并且本地还是会选择了指向null0的汇总路由，所以也要关闭本地的水平分割。**

**关于命令maximum-paths**

**解释：指定本路由器支持的负载均衡的条数---注意点：和路由表联系起来**

**关于命令traffic-share [balanced | min across-interfaces]**

**解释：该命令仅在非等价负载均衡中有作用，如果在等价负载均衡中，两个参数的意义是一样的**

**如果指定参数balanced，则路由器分配给各条路由的流量与其度量值呈反比**

**如果指定参数min across-interfaces，则路由器将只使用成本最小的路由**

**关于命令maximum-paths和traffic-share的区别**

**答：maximum-paths关心的是路由如何写入路由表**

**traffic-share关心的是实际传输包的时候路由表中的路由如何使用**

**关于命令variance**

**解释：用于不等价负载均衡的命令，默认情况下variance的值是1，也就是只支持等价负载均衡，进程下**

**公式：FD*variance>AD**

**计算方法：在拓扑数据库中的两个FD相除就可以了**

**EIGRP是唯一一个支持不等价负载均衡的路由协议**

**关于命令ip bandwidth-percent eigrp**

**解释：接口下的命令，用于改变接口下EIGRP使用的带宽。默认情况下，EIGRP最多只占接口的配置带宽的50%，注意了，这里的配置带宽是指用bandwidth命令配置的带宽，并不是物理支持的带宽。**

**默认情况下，EIGRP最多占用接口或子接口配置带宽的50%。**

**在帧中继的主接口，点到点子接口，多点子接口默认的配置带宽都是T1的速率，也就是1.544Mbps，这样的话按默认使用百分之五十算就是使用了768kbps，但是如果对端（比如电信）给的CIR是56kbps，这样的话如果发生了拥塞就麻烦了。所以要给接口分配实际的带宽。**

**对于点到点子接口，应该将配置带宽设置为对端提供的CIR**

**对于多点子接口，应该将配置带宽设置为PVC中对端最低的CIR*PVC的数量**

**例子:**

![EIGRP%20Lab%2012b5b45018a04ba78a3af17608f17b04/image2.png](EIGRP%20Lab/image2.png)

**例子：**

![EIGRP%20Lab%2012b5b45018a04ba78a3af17608f17b04/image3.png](EIGRP%20Lab/image3.png)

**关于EIGRP的认证**

**R2(config)#key chain R2（本地有效）定义KEY库名为R2**

**R2(config-keychain)#key 1（两端一致）定义KEY号为1**

**R2(config-keychain-key)#key-string cisco 定义KEY值为cisco**

**R2(config-if)#ip authentication key-chain eigrp 90 R2 指定使用哪个库**

**R2(config-if)#ip authentication mode eigrp 90 md5 开启认证**

**R1#show key chain**

**R1#debug eigrp packet**

**R2(config-keychain-key)#Accept-lifetime 04:00:00 jan 2006 infinite 定时接收**

**R2(config-keychain-key)#Send-lifetime 04:00:00 jan 2006 04:01:00 jan 2006 定时发送**

**R2(config-keychain-key)#Send-lifetime 04:00:00 jan 2006 duration 300 有效期300S**

**关于no ip split-horizon eigrp命令**

**解释：默认情况下，对于任何类型的链路，不管是LAN还是WAN，宣告进EIGRP的接口的水平分割都是打开的，但是在帧中继的Hub端的接口上要使用此命令关闭EIGRP的水平分割，不然无法传路由**

**关于命令metric maximum-hops**

**解释：用于修改EIGRP的最大跳数，默认是224，最大可修改为255.IGRP的默认跳数是255.**

**关于passive-interface**

**passive-interface 在不同路由协议中的意义**

**第一种是RIP与IGRP.这一种routing protocol的特色是不会与对方router建立关系。所以, router是每隔一段时间,就会把routing information广播出去。这一类的routing protocol在使用passive-interface的时候,就会发生只收不发的状况.换句话说,只要routing protocol的process还在运作, routing update还是可以收进来,只不过因为passive-interface指令的关系, update会发不出去.所以,如果要阻止update送进router中,还要加上distribute-list来过滤incoming update.这是第一种状态.**

**第二种情况是像OSPF, EIGRP,之类的routing protocol.这一种路由协议的特色是会与对方router建立关系.也就是说router之间会建neighbor.所以,一但打了passive-interface之后,你就断了router之间的关系. 因为no relationship, no update.因此,所有的update送不出去,但是也收不进来.这是第二种状态**

**关于EIGRP产生默认路由**

**在EIGRP区域产生默认路由的方法：**

**1、ip route 0.0.0.0 0.0.0.0 null0**

**redistribute static**

**//这里产生的是EIGRP外部默认路由，以D* EX表示，(默认是按静态路由出接口类型计算Metric）**

**2、ip route 0.0.0.0 0.0.0.0 null0**

**network 0.0.0.0**

**//这里产生的是EIGRP区域内的默认路由，以D*表示，（写下一跳不行，必须写接口），注意这里静态路由不能写下一跳地址，否则不会产生缺省路由**

**缺点:会在宣告的路由器上,将所有接口激活.包括你不想激活的接口**

**3、ip default-network 172.16.0.0**

**必须先把出接口宣告进EIGRP中，再用下面的命令**

**R1(config)#ip default-network 192.12.1.0（写成主类）**

**这样就可以把这条路由下发给其它的路由器**

**注意：接口也必须是主类地址**

**能够配置成default-network的网络必须是主类网络。**

**并且该主类网络必须存在于其路由器的路由表中**

![EIGRP%20Lab%2012b5b45018a04ba78a3af17608f17b04/image4.png](EIGRP%20Lab/image4.png)

**4、ip summary-address eigrp 100 0.0.0.0 0.0.0.0 5**

**以D*的形式显示 于路由表中**

**缺点:具有方向性.具有抑制明细的特点。**

**当RIP时必须创建默认路由,才能传播进去**

**注意这里有个"5"是默认的，EIGRP手动汇总路由的管理距离默认=5；防环机制；本地有效；**

**在EIGRP中default-information 不是用来传递默认路由而是用来控制**

**default-information allow in 是默认在进程中开启,允许所有可传递的默认网络进入本路由器**

**default-information allow out 是默认在进程中开启,允许所有可传递的默认网络传递出本路由器**

**命令前加no跟out或者in.表示不允许进入默认路由或者传递默认路由,而不是no掉此命令**

**关于命令eigrp stub [receive-only | connected | static | summary]**

**解释：用于设置末节路由器**

**除了参数receive-only外，可以以任何方式组合使用这些参数**

**如果仅使用eigrp stub，则默认通告直连和汇总路由**

**关于命令timers active-time [time | disable]**

**解释：是指SIA的时间**

**关于命令show ip protocols**

**解释：显示关于路由器上运行的所有路由选择协议的信息，一般使用该命令看K值，如：**

**R1#show ip protocols**

**Routing Protocol is "eigrp 100"**

**Outgoing update filter list for all interfaces is not set**

**Incoming update filter list for all interfaces is not set**

**Default networks flagged in outgoing updates**

**Default networks accepted from incoming updates**

**EIGRP metric weight K1=1, K2=0, K3=1, K4=0, K5=0**

**EIGRP maximum hopcount 100**

**EIGRP maximum metric variance 1**

**Redistributing: eigrp 100**

**EIGRP NSF-aware route hold timer is 240s**

**<output omitted>**

**Maximum path: 4**

**Routing for Networks:**

**172.16.1.0/24**

**192.168.1.0**

**Routing Information Sources:**

**Gateway Distance Last Update**

**(this router) 90 00:09:38**

**Gateway Distance Last Update**

**192.168.1.102 90 00:09:40**

**Distance: internal 90 external 170**

**关于命令show ip eigrp neighbors**

**解释：用于看邻居，如：**

**R1#show ip eigrp neighbors**

**IP-EIGRP neighbors for process 100**

**H Address Interface Hold Uptime SRTT RTO Q Seq**

**(sec) (ms) Cnt Num**

**0 192.168.1.102 Se0/0/1 10 00:07:22 10 2280 0 5**

**R1#**

**其中:**

**H(handle)：Cisco IOS内部用于跟踪邻居的编号**

**Address：邻居的网络层地址**

**Interface：能够到达邻居的路由器接口**

**Hold：保持时间，收到Hello分组以后，该时间会重置**

**Uptime：本地路由器首次收到Hello分组后经过的时间**

**SRTT（平均往返时间）：说白了就是一来一回的时间**

**RTO：路由器将重传队列中的分组重传给邻居之前所等待的时间，以毫秒记**

**Q（queue count）：在队列中等待发送的分组数，如果该值经常大于0，则可能存在拥塞的问题。**

**Seq（Seq Num）：从邻居那里收到的最后一个更新、查询或应答分组的序列号**

**关于命令show ip eigrp topology**

**解释：用于看拓扑数据库，但是注意：只能显示successor和feasible successor，如果想看拓扑表中的所有条目，使用命令show ip eigrp topology all-links。如：**

**R1#show ip eigrp topology**

**IP-EIGRP Topology Table for AS(100)/ID(192.168.1.101)**

**Codes: P - Passive, A - Active, U - Update, Q - Query, R - Reply,**

**r - reply Status, s - sia Status**

**P 192.168.1.96/27, 1 successors, FD is 40512000**

**via Connected, Serial0/0/1**

**P 192.168.1.0/24, 1 successors, FD is 40512000**

**via Summary (40512000/0), Null0**

**P 172.16.0.0/16, 1 successors, FD is 28160**

**via Summary (28160/0), Null0**

**P 172.16.1.0/24, 1 successors, FD is 28160**

**via Connected, FastEthernet0/0**

**P 172.17.0.0/16, 1 successors, FD is 40514560**

**via 192.168.1.102 (40514560/28160), Serial0/0/1**

**其中：**

**P：表示该网络当前可用，可被加入到路由表中，能不能加进去要看管理距离是否够小**

**A：表示该网络当前不可用，不能加入到路由表中。处于主动状态意味着还有没有得到应答的查询**

**U：网络正在更新，或者路由器正在等待更新分组的确认**

**Q：网络有未被应答的查询分组或者路由器正在等待应答分组的确认**

**R：路由器正在生成该网络的应答或者等待对应答分组的确认**

**S：表示该路由陷入主动状态**

**关于命令show ip eigrp traffic**

**解释：用于显示各种EIGRP分组的数量，如：**

**R1#show ip eigrp traffic**

**IP-EIGRP Traffic Statistics for AS 100**

**Hellos sent/received: 429/192**

**Updates sent/received: 4/4**

**Queries sent/received: 1/0**

**Replies sent/received: 0/1**

**Acks sent/received: 4/3**

**Input queue high water mark 1, 0 drops**

**SIA-Queries sent/received: 0/0**

**SIA-Replies sent/received: 0/0**

**Hello Process ID: 113**

**PDM Process ID: 73**

<<EIGRP 经典小实验.pdf>>

<<EIGRP 经典小实验.net>>