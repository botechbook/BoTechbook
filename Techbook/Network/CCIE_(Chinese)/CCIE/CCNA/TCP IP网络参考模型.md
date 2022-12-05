# TCP IP网络参考模型

TCP/IP网络参考模型

2009年9月8日

21:47

> 内容：
> 
> 
> 掌握TCP/IP分层模型
> 
> 掌握三次握手过程
> 
> 理解OSI和TCP/IP模型的区别和联系
> 
> 一、TCP/IP分层
> 
> ![TCP%20IP%E7%BD%91%E7%BB%9C%E5%8F%82%E8%80%83%E6%A8%A1%E5%9E%8B%20862234bb70394a8196dd30526de342be/image1.png](TCP%20IP网络参考模型/image1.png)
> 
> ![TCP%20IP%E7%BD%91%E7%BB%9C%E5%8F%82%E8%80%83%E6%A8%A1%E5%9E%8B%20862234bb70394a8196dd30526de342be/image2.png](TCP%20IP网络参考模型/image2.png)
> 
> **应用层协议**：
> 
> 文件传输- TFTP 简单的文件传输协议，FTP文件传输协议， NFS网
> 
> 络文件系统。
> 
> E-Mail - SMTP，pop3（Post Office Protocol 3）
> 
> 远程登陆 - Telnet ，ssh (security shell )
> 
> 网络管理 - SNMP(简单的网络管理协议)
> 
> 名称管理 - DNS (URL 网址和IP地址之间的映射)
> 
> **主机到主机层**：
> 
> 传输控制协议（Transmission Control Protocol，TCP）是一种面向连接的、可靠的、基于字节流的主机到主机层通信协议，由IETF的RFC 793说明。在简TCP/IP模型中，它完成运输层所指定的功能。
> 
> <<传输层协议.ppt>>
> 
> <<神奇的传输层.docx>>
> 
> TCP协议
> 
> **TCP** 数据格式
> 
> ![TCP%20IP%E7%BD%91%E7%BB%9C%E5%8F%82%E8%80%83%E6%A8%A1%E5%9E%8B%20862234bb70394a8196dd30526de342be/image3.png](TCP%20IP网络参考模型/image3.png)
> 
> 1 源端口和目的端口— —字段长度各为16位,它们为封装的数据指定了源和目的应用程序。
> 
> Source and Destination Port are 16-bit fields that specify the source and destination applications for the encapsulated data. Like other numbers used by TCP/IP, RFC 1700 describes all port numbers in common and not-so-common use. A port number for an application, when coupled with the IP address of the host the application resides on, is called a socket. A socket uniquely identifies every application in a network.
> 
> 2 序列号— —字段长度为32位,序列号确定了发送方发送的数据流中被封装的数据所在位置。
> 
> Sequence Number is a 32-bit number that identifies where the encapsulated data fits within a data stream from the sender. For example, if the sequence number of a segment is 1343 and the segment contains 512 octets of data, the next segment should have a sequence number of 1343 + 512 + 1 = 1856.
> 
> 3 确认号— —字段长度为32位,确认号确定了源点下一次希望从目标接收的序列号。如果主机收到的确认号与它下一次打算发送(或已发送)的序列号不符,那么主机将获悉丢失的数据（差错控制机制）。
> 
> Acknowledgment Number is a 32-bit field that identifies the sequence number the source next expects to receive from the destination. If a host receives an acknowledgment number that does not match the next sequence number it intends to send (or has sent), it knows that packets have been lost.
> 
> 4 报头长度 — —又叫数据偏移量,长度为4位,报头长度指定了以32位字为单位的报头长度。由于可选项字段的长度可变,所以这个字段标识出数据的起点是很有必要的。
> 
> Header Length, sometimes called Data Offset, is a four-bit field indicating the length of the header in 32-bit words. This field is necessary to identify the beginning of the data because the length of the Options field is variable.
> 
> 5 （1）保留— —字段长度为4位,通常设置为0。
> 
> （2）标记（Flag）--包括8个1位的标记，用于流和连接控制。它们从左到右分别是：拥塞窗口减少（Congestion Window Reduced，CWR）、ECN-Echo（ECE）、紧急（URG）、确认（ACK）、弹出（PSH）、复位（RST）、同步（SYN）和结束（FIN）。
> 
> The Reserved field is four bits, which are always set to zero.Flags are eight 1-bit flags that are used for data flow and connection control. The flags,from left to right, are Congestion Window Reduced (CWR), ECN-Echo(ECE), Urgent (URG), Acknowledgment (ACK), Push (PSH), Reset (RST), Synchronize (SYN), and Final (FIN).
> 
> 6 窗口大小-——字段长度为16位,主要用于流控制。窗口大小指明了自确认号指定的八位组开始,接收方在必须停止传输并等待确认之前发送方可以接收的数据段的八位组长度。用来指明发送方发送数据的大小（用于流控）
> 
> Window Size is a 16-bit field used for flow control. It specifies the number of octets, starting with the octet indicated by the Acknowledgment Number, that the sender of the segment will accept from its peer at the other end of the connection before the peer must stop transmitting and wait for an acknowledgment.
> 
> 7 校验和— —字段长度为16位,它包括报头和被封装的数据,校验和允许错误检测。
> 
> Checksum is 16 bits, covering both the header and the encapsulated data, allowing error detection.
> 
> 8 紧急指针— —字段仅当URG标记置位时才被使用。这个16位数被添加到序列号上用于指明紧急数据的结束。
> 
> Urgent Pointer is used only when the URG flag is set. The 16-bit number is added to the Sequence Number to indicate the end of the urgent data.
> 
> 9 可选项— —字段用于指明TCP的发送进程要求的选项。最常用的可选项是最大段长度,最大段长度通知接收者发送者愿意接收的最大段长度。为了保证报头的长度是一个八位组的倍数,所以使用0填充该字段的剩余部分。
> 
> Options, as the name implies, specifies options required by the sender's TCP process. The most commonly used option is Maximum Segment Size, which informs the receiver of the largest segment the sender is willing to accept. The remainder of the field is padded with zeros to ensure that the header length is a multiple of 32 octets.
> 
> TCP三次握手
> 
> <<TCP 三次握手.pptx>>
> 
> ![TCP%20IP%E7%BD%91%E7%BB%9C%E5%8F%82%E8%80%83%E6%A8%A1%E5%9E%8B%20862234bb70394a8196dd30526de342be/image4.png](TCP%20IP网络参考模型/image4.png)
> 
> **在TCP/IP协议中，TCP协议提供可靠的连接服务，采用三次握手建立一个连接。**
> 
> **第一次握手：建立连接时，客户端发送syn包(syn=j)到服务器，并进入SYN_SEND状态，等待服务器确认；**
> 
> **第二次握手：服务器收到syn包，必须确认客户的SYN（ack=j+1），同时自己也发送一个SYN包（syn=k），即SYN+ACK包，此时服务器进入SYN_RECV状态；**
> 
> **第三次握手：客户端收到服务器的SYN＋ACK包，向服务器发送确认包ACK(ack=k+1)，此包发送完毕，客户端和服务器进入ESTABLISHED状态，完成三次握手。**
> 
> **客户端与服务器端将保持活动状态，直到任何一方发送FIN（结束）信号**
> 
> 三次握手的过程也就是源和目的端同步的过程。 保证下面传输的可靠性。在此过程完成之后发送数据流。
> 
> DoS攻击介绍
> 
> Denial of service
> 
> 启用TCP拦截
> 
> DDoS
> 
> Distribute denial of service 分布式拒绝服务攻击
> 
> SYN flood 攻击
> 
> 死亡之ping
> 
> IP碎片攻击
> 
> TCP的4次挥手
> 
> 由于TCP连接是全双工的，因此每个方向都必须单独进行关闭。这原则是当一方完成它的数据发送任务后就能发送一个FIN来终止这个方向的连接。收到一个 FIN只意味着这一方向上没有数据流动，一个TCP连接在收到一个FIN后仍能发送数据。首先进行关闭的一方将执行主动关闭，而另一方执行被动关闭。
> 
> （1） TCP客户端发送一个FIN，用来关闭客户到服务器的数据传送。
> 
> （2） 服务器收到这个FIN，它发回一个ACK，确认序号为收到的序号加1。和SYN一样，一个FIN将占用一个序号。
> 
> （3） 服务器关闭客户端的连接，发送一个FIN给客户端。
> 
> （4） 客户段发回ACK报文确认，并将确认序号设置为收到序号加1。
> 
> **差错控制与流量控制机制：**
> 
> **1**
> 
> ![TCP%20IP%E7%BD%91%E7%BB%9C%E5%8F%82%E8%80%83%E6%A8%A1%E5%9E%8B%20862234bb70394a8196dd30526de342be/image5.jpg](TCP%20IP网络参考模型/image5.jpg)
> 
> **2 滑动窗口**
> 
> **为什么使用滑动窗口机制？**
> 
> **TCP是一种可靠的协议，要确定数据包可靠的到达。本来对于每一个发送出去的TCP数据包，都应该给发送者一个ACK回应。但是每个包都回应的话会加剧带宽的拥塞，所以引入了滑动窗口机制。这样只需要一堆数据包发送一个ACK就可以了，至于一次发送多少数据包是要靠窗口大小协商。**
> 
> **而且通过窗口大小的协商也能够知道在网络拥塞的时候控制发送数据的大小，进而达到流控的目的。**
> 
> **举例：**
> 
> 如果窗口大小只有1个，OK ，那每次发送方 发完一个数据包后都得等待回应，只有收到回应后才能发送第二个包，这样就减缓了处理速度。
> 
> 如果发送方的窗口很多 有100个，OK 他一次发送100个数据，但是请求方只能处理50个数据，他就会处理完50个数据，告诉发送方 他下次要的数据要从第51号开始，发送方接收到这个信息后，就知道请求方一次只能处理50个数据，就会改变窗口的大小置50，然后一次发送50个数据，**这个滑动窗口会根据请求方的接受能力不断变化，所以称为滑动窗口。**
> 
> **TCP通过控制发送方窗口大小来控制拥塞。**
> 
> **决定发送窗口大小的因素有两个：**
> 
> **（1） 接收方通告的窗口大小**
> 
> **（2）发送端的拥塞窗口限制**
> 
> **发送窗口大小取两者的最小值。**
> 
> <<TCP 滑动窗口.pptx>>
> 
> ![TCP%20IP%E7%BD%91%E7%BB%9C%E5%8F%82%E8%80%83%E6%A8%A1%E5%9E%8B%20862234bb70394a8196dd30526de342be/image6.jpg](TCP%20IP网络参考模型/image6.jpg)
> 
> **起初，假定发送端拥塞窗口尺寸为3，含义为：在收到对方的确认之前可以连续发送3个字节，同时假定接收方通告的窗口大小也是3，取两者的最小值作为发送窗口尺寸，结果是3.因此图中那个发送者发送完3字节后等待接收方确认。接收方由于缓冲区变化造成第3字节的数据被丢弃，因此接收方在返回给发送者的确认数据中只提示收到2字节。确认码为3表示收到2字节，等待第3个。同时接收方在它的确认数据中将窗口尺寸改为2，这个数值是由TCP头中的窗口字段表示的。发送方收到这个确认后得知第3字节丢失，重新传送第3字节的内容，并且调整发送窗口尺寸为两者中的最小者，结果是2.**
> 
> **这样将解决丢包现象。**
> 
> <<TCP慢启动和滑动窗口.txt>>
> 
> **UDP协议**
> 
> ![TCP%20IP%E7%BD%91%E7%BB%9C%E5%8F%82%E8%80%83%E6%A8%A1%E5%9E%8B%20862234bb70394a8196dd30526de342be/image7.png](TCP%20IP网络参考模型/image7.png)
> 
> UDP协议有如下的特点：
> 
> 1、UDP传送数据前并不与对方建立连接，即**UDP是无连接的**，在传输数据前，发送方和接收方相互交换信息使双方同步。
> 
> 2、**UDP不对收到的数据进行排序**，在UDP报文的首部中并没有关于数据顺序的信息（如TCP所采用的序号），而且报文不一定按顺序到达的，所以接收端无从排起。
> 
> 3、**UDP对接收到的数据报不发送确认信号**，发送端不知道数据是否被正确接收，也不会重发数据。
> 
> 4、**UDP传送数据较TCP快速**，系统开销也少。
> 
> 5、由于**缺乏拥塞控制**（congestion control），需要基于网络的机制来减小因失控和高速UDP流量负荷而导致的拥塞崩溃效应。换句话说，因为UDP发送者不能够检测拥塞，所以像使用包队列和丢弃技术的路由器这样的网络基本设备往往就成为降低UDP过大通信量的有效工具。数据报拥塞控制协议(DCCP)设计成通过在诸如流媒体类型的高速率UDP流中增加主机拥塞控制来减小这个潜在的问题。
> 
> ![TCP%20IP%E7%BD%91%E7%BB%9C%E5%8F%82%E8%80%83%E6%A8%A1%E5%9E%8B%20862234bb70394a8196dd30526de342be/image8.png](TCP%20IP网络参考模型/image8.png)
> 
> 常用端口号：
> 
> TCP:FTP 20,21 文件传输协议 file transport protocol
> 
> telnet 23 远程登录协议
> 
> smtp 25 简单邮件传输协议 simple mail transport protocol
> 
> http 80 超文本传输协议 hyper text transport protocol
> 
> https 443 安全超文本传输协议 hyper text transport protocol security
> 
> UDP:tftp 69
> 
> TFTP（Trivial File Transfer Protocol）,简单文件传输协议
> 
> RIP 520 路由信息协议（routing information protocol）
> 
> RIPng 521 rip应用于IPV6网络当中
> 
> pop3 110
> 
> POP3(Post Office Protocol 3)即邮局协议的第3个版本
> 
> SNMP 161 简单网络管理协议 simple network management protocol
> 
> **其中DNS比较特殊，既使用TCP，又使用UDP，端口号是53**
> 
> ***DNS***
> 
> **区域传输使用TCP，其他使用UDP**
> 
> 区域传输：dns的规范规定了2种类型的dns服务器，一个叫主服务器，一个叫辅助服务器。在一个区中主dns服务器从自己本机的数据文件中读取该区的dns数据信息，而辅助dns服务器则从区的权威dns服务器中读取该区的dns数据信息。当一个辅助dns服务器启动时，它需要与主dns服务器通信，并加载数据信息，这就叫做区传送（zone transfer）
> 
> **网络层**
> 
> 1)、协议
> 
> ![TCP%20IP%E7%BD%91%E7%BB%9C%E5%8F%82%E8%80%83%E6%A8%A1%E5%9E%8B%20862234bb70394a8196dd30526de342be/image9.png](TCP%20IP网络参考模型/image9.png)
> 
> 2）、IP报文
> 
> ![TCP%20IP%E7%BD%91%E7%BB%9C%E5%8F%82%E8%80%83%E6%A8%A1%E5%9E%8B%20862234bb70394a8196dd30526de342be/image10.png](TCP%20IP网络参考模型/image10.png)
> 
> Version（版本）：该字段占4位，且是4
> 
> HL（包头长度）：该字段占4位，表示IPv4的头部长度，一般情况下是5，即5*4=20字节
> 
> 头部长度指的是**首部占32 bit字的数目**，包括任何选项。由于它是一个4比特字段，因此首部最长为60个字节。因为是4bit所以，最大是15，也就是15x4字节是60字节的
> 
> Type of Service（服务类型）：该字段占8位，用来做QoS
> 
> Total Length（总长度）：该字段占16位，表示IPv4包的总长
> 
> Identification （标识符）字段长度为16位,通常与标记字段和分段偏移字段一起用于数据包的分段。唯一地标识主机所发送的一个数据段，通常每发送一个数据段后加一。如果数据包原始长度超过数据包所要经过的数据链路的最大传输单元 (MTU),那么必须将数据包分段为更小的数据包。
> 
> 例如,一个大小为5000字节的数据包在穿过网络时,如果遇到一条MTU为1500字节的数据链路,即数据帧最多容纳大小为1500字节的数据包。路由器需要在数据成帧之前将数据包分段成多个数据包,其中每个数据包长度不得超过1500字节;然后路由器在每片数据包的标识字段上打上相同的标记,以便接收设备可以识别出属于一个数据包的分段。
> 
> Flags（标志）：该字段占3位，
> 
> 第一位是保留的，还未使用
> 
> 第二位是DF位，即不分段位，如果取0，表示可以分段，如果取1，表示不可以分段。
> 
> 第三位是MF位，即更多段位，如果取0，表示该包是最后的包，如果取1，表示该包后面还有更多的包。
> 
> Fragment Offset（分段偏移）：该字段占13位，用来表示该分段相对于第一个分段的偏移。
> 
> 以8个八位组为单位,用于指明分段起始点相对于报头起始点的偏移量。由于分段到达时可能错序,所以分段偏移字段可以使接收者按照正确的顺序重组数据包。
> 
> Time to Live（TTL，即生存时间）：该字段占8位，每经过一台路由器减一，为0时丢弃。从255开始
> 
> Protocol ID（协议ID）：该字段占8位，用来反映上层协议
> 
> Header Checksum（头部校验和）：该字段占16位，用来做头部的校验
> 
> Source Address（源地址）：该字段占32位
> 
> Destination Address（目标地址）：该字段占32位
> 
> Options（可选项）：如果使用可选项，有可能IPv4包头会比IPv6包头还要大。
> 
> Padding（填充项）。
> 
> 3）、协议域:
> 
> ![TCP%20IP%E7%BD%91%E7%BB%9C%E5%8F%82%E8%80%83%E6%A8%A1%E5%9E%8B%20862234bb70394a8196dd30526de342be/image11.png](TCP%20IP网络参考模型/image11.png)
> 
> 4）、ICMP协议几个典型的值
> 
> ![TCP%20IP%E7%BD%91%E7%BB%9C%E5%8F%82%E8%80%83%E6%A8%A1%E5%9E%8B%20862234bb70394a8196dd30526de342be/image12.png](TCP%20IP网络参考模型/image12.png)
> 
> 5）、ARP
> 
> 已知对端IP求对端MAC地址
> 
> ![TCP%20IP%E7%BD%91%E7%BB%9C%E5%8F%82%E8%80%83%E6%A8%A1%E5%9E%8B%20862234bb70394a8196dd30526de342be/image13.png](TCP%20IP网络参考模型/image13.png)
> 
> ![TCP%20IP%E7%BD%91%E7%BB%9C%E5%8F%82%E8%80%83%E6%A8%A1%E5%9E%8B%20862234bb70394a8196dd30526de342be/image14.jpg](TCP%20IP网络参考模型/image14.jpg)
> 
> **ARP (Address Resolution Protocol)** : 当一台设备需要发现另一台设备的数据链路标识符时,它将建立一个ARP请求数据包。这个请求数据包中包括目标设备的IPv4地址以及请求设备 (发送者)的源点IPv4地址和数据链路标识符(MAC地址)。然后ARP请求数据包被封装在数据帧中,其中带有作为源的发送者的MAC地址和作为目标的广播地址
> 
> 广播地址意味着数据链路上的所有设备都将收到该帧,并 且要检查帧内封装的数据包。除了目标机可以识别此数据包外,其他所有设备都会丢弃此数据包。目标机将向源地址发送ARP响应数据包,提供它的MAC地址
> 
> RARP
> 
> 已知MAC求对端IP
> 
> ![TCP%20IP%E7%BD%91%E7%BB%9C%E5%8F%82%E8%80%83%E6%A8%A1%E5%9E%8B%20862234bb70394a8196dd30526de342be/image15.png](TCP%20IP网络参考模型/image15.png)
> 
> 代替映射硬件地址到已知IPv4地址,反向ARP(RARP)可 以实现IPv4地址到已知硬件地址的映射。某些设备,如无盘工作站在启动时可能不知道自己启动时的IPv4地址。嵌入这些设备固件中的RARP程序可以允许它们发送ARP请求,其中硬件地址为设备的硬件编入地址。RARP服务器将会向这些设备回复相应的IPv4地址
> 
> TCP/IP和OSI参考模型不同之处：
> 
- TCP/IP考虑到多种**异构网**的互连问题，将网际协议IP作为TCP/IP的组成部分。ISO只考虑到全球使用一种统一的标准，将各种不同的 系统互连在一起。
- TCP/IP就对面向连接服务和无连接服务并重。OSI只强调面向连接。
- TCP/IP有较好的网络管理功能，OSI后来才开始考虑这个问题。

![TCP%20IP%E7%BD%91%E7%BB%9C%E5%8F%82%E8%80%83%E6%A8%A1%E5%9E%8B%20862234bb70394a8196dd30526de342be/image16.png](TCP%20IP网络参考模型/image16.png)