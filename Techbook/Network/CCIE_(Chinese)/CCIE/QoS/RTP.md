# RTP

RTP

2011年7月7日

15:40

**提纲：**

**1.RTP协议**

**2.RTCP协议**

**3.cRTP协议**

**关于RTP协议**

**RTP（Real-Time Transport Protocol，实时传输协议）是传送实时音频和视频的一种可选协议，在UDP包头之后增加了一个头部，包括了重建时间戳、序列号、安全和内容标识等信息。**

**注意：RTP不会占用过多的带宽**

**由于进入RTP优先队列的报文进行了限速，超出规定流量的报文被丢弃，这样在接口拥塞的情况下可以保证属于RTP优先队列的报文不会占用超出规定的带宽，保护了其他报文的应得带宽，解决了PQ的高优先级队列的流量可能饿死低优先级流量的问题。**

**关于RTP的配置：**

**1.在MQC中的配置**

**命令：**

**Router（config-cmap）# match protocol rtp [audio|video|payload-type payload-type-string]**

**其中**

**可选关键字audio指定匹配音频净荷类型的流量（0-23预留给音频流量）**

**可选关键字video指定匹配视频净荷类型的流量（24-33预留给视频流量）**

**可选关键字payload-type指定匹配某特殊净荷类型，从而可以比audio或video关键字更灵活的控制手段**

**注意：RTP可以与任何一种队列包括FIFO、PQ、CQ、WFQ或CBWFQ结合使用，它的优先级是最高的。**

**2.在接口下的配置**

**命令：**

**Router(config-if)#ip rtp priority {*starting-rtp-port-number port-number-range*} {*bandwidth*}**

**starting-rtp-port-number：定义起始端口**

**port-number-range：定义端口范围**

**bandwidth：定义预留的带宽**

**案例一：RTP和CBWFQ的结合使用**

**在接口s1/1中，对于DSCP值为EF的流量设置带宽为3Mbps，并使用早期随机检测技术，当包长度在32到256之间的时候随机丢弃数据包，并且数据包被丢弃的概率是10%。同时，针对与RTP流量，端口号在16384-32767范围内的数据包设置带宽40kbps。**

**ip rtp priority 16384 16383 40**

**关键配置：**

**class-map match-all EF**

**match ip dscp ef**

**policy-map CBWFQ**

**class EF**

**bandwidth 3000**

**random-detect dscp-based**

**random-detect dscp 46 32 256 100**

**interface Serial1/1**

**bandwidth 100000 -------这里该带宽是为了实验能够做出来，没有别的意思**

**service-policy output CBWFQ**

**关于RTCP协议**

**RTP有一个姊妹协议，是RTCP（Real-Time Control Protocol，实时控制协议）。**

**RTP使用UDP偶数端口（默认从16384开始），RTCP则使用UDP奇数端口。**

**NBAR的深度包检测功能允许用户基于RTP净荷类型（音频或视频）进行流量分类，也可以基于音频或视频CODEC的类型进行深层的流分类。**

**关于cRTP协议**

**RTP的包头部分会比较大**

**20字节的IPv4包头+8字节的UDP包头+12字节的RTP包头，因此最少为40字节。所以出现了cRTP，专门对RTP的头部进行压缩。**

**cRTP是一种逐跳的压缩机制。可以把40字节压缩到2-5字节。当广域网接口带宽不高，并且RTP数据流量过大的话，应该考虑使用CRTP；但是对于高于T1线路速率的接口，无需使用CRTP。**

**关于cRTP的基本配置**

**1.在物理接口下启用cRTP**

**Router（config-if）#ip rtp header-compression [passive]**

**passive：当进站的RTP数据包的IP/UDP/RTP包头被压缩，才相应的压缩出站的RTP数据包的IP/UDP/RTP包头；如果不指定passive，则会对所有的IP/UDP/RTP包头进行压缩**

**2.更改IP/UDP/RTP包头压缩的连接数，默认是16条，最多500条**

**Router（config-if）#ip rtp compression-connections {number}**

**关于Frame Relay中的cRTP配置**

**1.在物理接口下启用cRTP**

**Router（config-if）#frame-relay ip rtp header-compression [passive]**

**注意：如果物理接口下启用了cRTP，子接口会自动继承**

**2.更改IP/UDP/RTP包头压缩的连接数，默认16条**

**Router（config-if）#frame-relay ip rtp compression-connections {number}**

**3.只针对特定的PVC启用cRTP**

**Router（config-if）#frame-relay map ip {ip-address} {dlci} [broadcast] rtp header-compression [active|passive] [connections number]**