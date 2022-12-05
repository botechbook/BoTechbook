# EIGRP 理论

EIGRP 理论

2009年9月19日

23:58

> 1、Features
> 
- 思科私有协议
- Advanced distance vector
- Fast convergence
- Support for VLSM and discontiguous subnets
- Partial updates
- Support for multiple network-layer protocols(IP/IPX/Appletalk)
- Flexible network design
- Multicast and unicast instead of broadcast address，used multicast address 224.0.0.10
- Manual summarization at any point
- 100% loop-free classless routing
- Easy configuration for WANs and LANs
- Load balancing across equal- and unequal-cost pathways

> 
> 
> 
> **EIGRP是最典型的平衡混合路由选择协议，它融合了距离**
> 
> **矢量和链路状态两种路由选择协议的优点，使用闪速更新**
> 
> **算法，能最快的达到网络收敛（convergence）**
> 
> 2、EIGRP四大模块
> 
- Neighbor discovery/recovery
    - Uses hello packets between neighbors
- Reliable Transport Protocol (RTP)
    - Guaranteed, ordered delivery of EIGRP packets to all neighbors

> Reliable packets ：Update/Query/Reply
> 
> 
> Unreliable packets ：Hello/ACK
> 
- DUAL finite-state machine
    - Selects lowest-cost, loop free, paths to each destination
- Protocol-dependent modules (PDMs)
    - EIGRP supports IP, AppleTalk, Novell NetWare （ipx）.
    - Each protocol has its own EIGRP module and operates independently of any of the others that may be running.

> 
> 
> 
> 3、三张表
> 
> 邻居表（Neighbor table）：包含所有直连形成邻接关系的邻居路由信息，确保直接邻居之间能够双向通信
> 
> 拓扑表（topology table）：满足可行性条件写进拓扑表 （AD < FD），拓扑表中存放着前往目标地址的所有路由
> 
> 路由表（routing table）：将拓扑表中最短开销的路由条目写进路由表
> 
> 4、关于EIGRP的5个包
> 
> （1）Hello：用于邻居发现和恢复进程。
> 
> 小于T1（1.544Mbps）链路时，60S单播方式发送；
> 
> 大于T1链路5S组播方式发送，不可靠。
> 
> **邻居：是指网络上直连的通告EIGRP的路由器**
> 
> （2）Update：用于传递路由更新信息。EIGRP中update包只在必要时候传递必要信息，且仅仅传递给需要路由信息的路由器。当只有某一指定路由器需要路由更新时，update是单播的，当有多台路由器需要更新时，更新数据包时组播发送的。 可靠
> 
> （3）Query：以组播形式发送，当重传时以单播形式发送 可靠
> 
> （4）Reply：单播相应query 可靠
> 
> （5）ACK：对可靠包的确认 不可靠
> 
> 如果任何数据包通过可靠的方式组播出去，而没有从邻居那里收到一个ACK数据包，那么这个数据包就会以单播方式被重新发送给那个没有响应的邻居。若经过16次这样的单播重传还没有收到一个ACK数据包的话，那么这个邻居就会被宣告为无效。
> 
> EIGRP重传策略：
> 
> （1）每个路由器都保存着邻居表和为每个邻居维护一个重传列表.
> 
> （2）每个需要确认的数据包 (update, query, reply) 再没有收到确认之前都将重传.
> 
> （3）当重传次数超过16次的时候邻居关系将被重置
> 
> 5、关于EIGRP建立邻居的6个过程
> 
> <<EIGRP建立邻居过程.pptx>>
> 
> ![EIGRP%20%E7%90%86%E8%AE%BA%20b333e4e92d3e4d97a9aeaf53020abbae/image1.png](EIGRP%20%E7%90%86%E8%AE%BA%20b333e4e92d3e4d97a9aeaf53020abbae/image1.png)
> 
> A ----------------hello----------> B
> 
> A <------hello + update ---- B
> 
> A ------------ack-------------->B
> 
> A 将B信息写进拓扑表
> 
> A -------------update----------->B
> 
> A <---------------ack----------------B
> 
> 6、建立邻居关系的条件
> 
> **k值、AS号、验证 必须一致**
> 
> 关于EIGRP的Metric值
> 
> K1＝带宽bandwidth（源和目的之间的最小带宽）
> 
> K2＝负载loading（源和目的之间的最大负载）
> 
> K3＝延迟delay（源和目的之间的延迟总和）
> 
> K4＝可靠性reliability（源和目的之间的最低可靠性）
> 
> K5＝MTU（源和目的之间的最小MTU）（最大传输单元）
> 
> 默认情况下Metric值的计算：
> 
> {K 1* [(10^7/Min bandwidth)] +K3*[ Sum delay/10]}*****256 = metric
> 
> 常见接口默认带宽及延时值
> 
> Interface　　BW（kbps）　　DLY（μsec）
> 
> Ethernet　　　10000　　　　1000
> 
> Serial　　　 1544　　　　 20000
> 
> Loopback　 　8000000　　　5000
> 
> 7、DUAL算法
> 
> DUAL算法：
> 
> 当一台路由器从它的邻居路由器收到一个Hello数据包时，该数据包将包含一个抑制时间（holdtime）。这个抑制时间告诉本路由器，在它收到后续的Hello数据包之前等待的最长时间。若holdtime超时，路由器还没接收到Hello包，将宣告这个邻居不可达。
> 
> **DUAL的设计思想是，即使暂时的路由选择环路也会对一个网络性能造成损害**。
> 
> **（1）邻接（adjacency）**
> 
> 刚启动时，路由器使用Hello数据包发现它的邻居并标识自己给邻居识别。当邻居被发现时，EIGRP协议将试图和它的邻居形成一个邻接关系。邻接是指两个互相交换路由信息的邻居之间形成的一条逻辑的关联关系。一旦邻接成功地建立，路由器就可以从它们的邻居那里接受路由更新消息了。这里的路由更新消息包括发送路由器所知道的所有路由和这些路由的度量值。对于每一条路由，路由器都将会基于它邻居通告的距离和到它的邻居的链路代价计算出一个距离。
> 
> **（2）可行距离（Feasible Distance，FD）**
> 
> **本地路由器到达每一个目的地的最小度量将作为该目的网络的可行距离。**
> 
> **（3）通告距离（Advertised Distance，AD），邻居通告的到达目的网络的最小距离。**
> 
> **（4）可行性条件（Feasibility Condition，FC）邻居路由器的AD<本地路由器的FD才可被写进拓扑表**
> 
> **（5）可行后继路由器（Feasible Successor，FS）**
> 
> **满足FC条件的邻居路由器**
> 
> **（6）后继路由器（successor）**
> 
> 对于在拓扑表中列出的每一个目的网络，将选用**拥有最小度量值**的路由并放置到路由表中。通告这条路由的**邻居**就成为一个后继。
> 
> 可行后继路由器和可行性条件的概念是避免环路的一项核心技术，因为可行后继路由器总是“下游路由器（downstream）”（也就是说，可行后继路由器到达目的地的度量距离比本地路由器的可行距离（FD）更短，）所以路由器从来不会选择一条导致反过来还要经过它本身的路径。而这样的路径一般有一个大于本地路由器FD的距离。
> 
> ![EIGRP%20%E7%90%86%E8%AE%BA%20b333e4e92d3e4d97a9aeaf53020abbae/image2.png](EIGRP%20%E7%90%86%E8%AE%BA%20b333e4e92d3e4d97a9aeaf53020abbae/image2.png)
>