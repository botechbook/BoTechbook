# TCP拦截

TCP拦截

2012年5月4日

18:04

TCP 拦截功能的目的是防止SYN攻击内部主机，。T C P三路握手的第一个报文设置了S Y N位。当某台设备接收到一个请求服务的初始报文时，该设备响应这个报文，发回一个设置了S Y N和A C K位的报文，并等待源端来的A C K应答。如果请求的发出者不作响应，主机就会因为超时而结束连接。当主机在等待这个事务完成时，这种h a l f - o p e n的连接消耗了主机的资源。在等待三路握手时资源被耗尽就是攻击的本质所在。

而启用了TCP拦截特性后，外部的主机就不是直接和内部受保护的主机直接建立TCP连接，而是由路由器来代替内部主机和外部主机进行TCP握手。在T C P连接请求到达目标主机之前， T C P拦截通过对其进行拦截和验证来阻止这种攻击。这个特征可以在两种模式上工作：拦截和监视。在拦截模式下，路由器拦截所有到达的TCP同步请求，并代表服务器建立与客户机的连接，并代表客户机建立与服务器的连接。如果两个连接都成功地实现，路由器就会将两个连接进行透明的合并。路由器有更为严格的超时限制，以防止其自身的资源被SYN攻击耗尽。在监视模式下，路由器被动地观察halt-open连接（没有完成T C P三路握手的连接）的数目。如果超过了所配置的时间，路由器也会关闭连接。访问表用来定义要进行T C P拦截的源和目的地址。

要开启TCP拦截，有以下两个必须步骤：

1.配置访问表，设置需要保护的IP地址

access-list [*100-199* | *WORD*] [deny | permit] tcp *source source-wildcast destination destination-wildcast*

2*.*开启TCP拦截

ip tcp intercept list *access-list-number*

T C P拦截可以在拦截和监视两种模式下工作，缺省为拦截模式。在这种模式下，路由器

响应到达的S Y N请求，并代替服务器发送一个响应初始源I P地址的S Y N - A C K报文，然后等待客户机的A C K。如果收到A C K，再将原来的S Y N报文发往服务器，路由器代替原来的客户机与服务器一起完成三路握手过程。这种模式增加了路由器的内存和C P U的额外开销，并且增加了一些初始会话的延时。在监视模式下，路由器允许S Y N请求直接到达服务器。如果这个会话在3 0秒钟内（缺省值）没有建立起来，路由器就给服务器发送一个R S T，以清除这个连接。路由器等待的时间是可以配置的。其模式可以使用下面的命令设置：

ip tcp intercept mode {intercept | watch}

缺省模式是intercept

TCP intercept配置简例：

Router(config)# access-list 101 permit tcp any 192.168.1.0 0.0.0.255

Router(config)# ip tcp intercept list 101

Router(config)# ip tcp intercept mode intercept

Router(config)# ip tcp intercept drop-mode ramdon   //当TCP半连接数达到门限值时，启用随机丢弃半连接。另外一种丢弃模式是oldest，即只丢弃最老的半连接

Router(config)# ip tcp intercept finrst-timeout 10   //设置FIN交换之后管理TCP连接的时间长度，而不是马上关闭TCP会话，这是为了让TCP 会话的关闭更加graceful

Router(config)# ip tcp intercept connection-timeout 3600   //配置TCP截取的非活跃连接时间为一个小时，之后丢弃连接，默认时间为24小时

Router(config)# ip tcp intercept max-incomplete low 10000   //当半连接总数低于10000时，退出野蛮模式(aggressive mode)。当TCP未完成连接的总数或者在一分钟之内的TCP连接请求到达门限值时，TCP截取进入野蛮模式。路由器认为在野蛮模式下受到了SYN洪泛攻击，每一个新连接请求的到来都会导致老的半连接被丢弃，也可以设置成随机模式。

Router(config)# ip tcp intercept max-incomplete high 15000   //当半连接总数达到15000时，路由器进入野蛮模式

查看TCP拦截的连接状况：

R2#sh tcp intercept connections

Incomplete:

Client                             Server                State        Create       Timeout           Mode

Established:

Client                             Server                State        Create         Timeout           Mode

192.168.23.3:45885    1.1.1.1:23            ESTAB    00:46:42     23:24:10              I

查看TCP拦截的统计信息：

R2#sh tcp inter sta

Watching new connections using access-list 100

0 incomplete, 1 established connections (total 1)

0 connection requests per minute