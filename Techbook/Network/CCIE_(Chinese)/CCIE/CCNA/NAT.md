# NAT

NAT

2009年9月30日

13:19

NAT

1作用:

解决IP地址不够用问题

屏蔽内网，使内网更加安全

2 、实现机制

在内部网络中使用内部地址，通过NAT把内部地址翻译成合法的IP地址，在Internet上使用

3、四种地址

**Inside local (IL)— Addresses assigned to inside devices. These addresses are not advertised to the outside.**

**Inside global (IG)— Addresses by which inside devices are known to the outside.**

Outside global (OG) — Addresses assigned to outside devices. These addresses are not advertised to the inside.

Outside local (OL)— Addresses by which outside devices are known to the inside.

① 内部局部（inside local）地址：在内部网络使用的地址，往往是私有地址；

② 内部全局（inside global）地址：用来代替一个或多个本地IP地址的、对外的、向NIC注册过的地址；

③ 外部局部（outside local）地址：一个外部主机相对于内部网络所用的IP 地址。不一定是合法的地址；

④ 外部全局（outside global）地址：外部网络主机的合法IP地址。

> 
> 

![NAT%208a235f9dfc2e4623bb0466b55f40141f/image1.gif](NAT/image1.gif)

> 
> 

4、三种类型

1．静态 NAT

静态 NAT 中，内部网络中的每个主机都被永久映射成外部网络中的某个合法的地址。静态地址转换将内部本地地址与内部合法地址进行一对一的转换， 且需要指定和哪个合法地址进行转换。如果内部网络有 E-mail 服务器或 FTP 服务器等可以为外部用户提供的服务，这些服务器的 IP 地址必须采用静态地址转换，以便外部用户可以使用这些服务。

2．动态 NAT （POOL NAT）

动态 NAT 首先要定义合法地址池，然后采用动态分配的方法映射到内部网络。动态 NAT是动态一对一的映射。

3．PAT

PAT则是把内部地址映射到外部网络的IP地址的不同端口上,从而可以实现多对一的映射。PAT 对于节省 IP 地址是最为有效的。

![NAT%208a235f9dfc2e4623bb0466b55f40141f/image2.jpg](NAT/image2.jpg)

实验一 静态NAT实验

实验步骤

先按图配置好接口地址，其中PC1和PC2用R3和R4来模拟，再起SW1用于连接PC1、PC2、R1

（1）步骤 1：配置路由器 R1 提供 NAT 服务

R1(config)#ip nat inside source static 192.168.1.2 211.1.12.3

//配置静态NAT 映射

R1(config)#ip nat inside source static 192.168.1.3 211.1.12.4

R1(config)#interface e0/0

R1(config-if)#ip nat inside

//配置NAT内部接口

R1(config)#interface s1/2

R1(config-if)#ip nat outside

//配置NAT外部接口

R1(config)#router ei 100

R1(config-router)#no auto-summary

R1(config-router)#network 211.1.12.0 0.0.0.255

（2）步骤 2：配置路由器 R2

R2(config)#router ei 100

R2(config-router)#no auto-summary

R2(config-router)#network 211.1.12.0 0.0.0.255

R2(config-router)#network 2.2.2.0 0.0.0.255

调试：

（1）debug ip nat

该命令可以查看地址翻译的过程。

在 PC1 和 PC2 上 Ping 2.2.2.2（路由器 R2 的环回接口），此时应该是通的

（2）show ip nat translations

该命令用来查看 NAT 表。静态映射时，NAT 表一直存在。

R1#show ip nat translations

实验二 动态NAT

实验步骤

（1）步骤 1：配置路由器 R1 提供 NAT 服务

R1(config)#ip nat pool NAT 211.1.12.3 211.1.12.100 netmask 255.255.255.0

//配置动态NAT 转换的地址池

R1(config)#ip nat inside source list 10 pool NAT

//配置动态NAT 映射

R1(config)#access-list 10 permit 192.168.1.0 0.0.0.255

//允许动态NAT 转换的内部地址范围

R1(config)#interface e0/0

R1(config-if)#ip nat inside

R1(config-if)#interface s1/2

R1(config-if)#ip nat outside

调试：

在 PC1和PC2 上分别 telnet 和ping 2.2.2.2（路由器 R2 的环回接口）

（1）debug ip nat

R1#debug ip nat

IP NAT debugging is on

R1#clear ip nat translation * //清除动态NAT表

（2）show ip nat translations

（3）show ip nat statistics

该命令用来查看 NAT 转换的统计信息。

R1#show ip nat statistics

实验三 PAT配置

@1 基于地址池的负载

（1）步骤 1：配置路由器 R1 提供 NAT 服务

R1(config)#ip nat pool NAT 211.1.12.3 211.1.12.100 netmask 255.255.255.0

R1(config)#ip nat inside source list 10 pool NAT overload //overload是过载，即多对一

R1(config)#access-list 10 permit 192.168.1.0 0.0.0.255

R1(config)#interface e0/0

R1(config-if)#ip nat inside

R1(config-if)#interface s1/2

R1(config-if)#ip nat outside

调试：

在 PC1和PC2 上分别 telnet 和ping 2.2.2.2（路由器 R2 的环回接口）

（1）debug ip nat

R1#debug ip nat

IP NAT debugging is on

R1#clear ip nat translation * //清除动态NAT表

（2）show ip nat translations

（3）show ip nat statistics

该命令用来查看 NAT 转换的统计信息。

R1#show ip nat statistics

通过命令“show ip nat translations verbose”可以查看。

也可以通过下面的命令来修改超时时间：

R1(config)#ip nat translation timeout *timeout*

参数 timeout 的范围是0-2147483

@2 基于端口的负载

如果主机的数量不是很多, 可以直接使用outside接口地址配置PAT， 不必定义地址池，

命令如下：

R1(config)#ip nat inside source list 10 interface s1/2 overload

动态 NAT 的过期时间是 86400 秒，PAT 的过期时间是 60 秒

实验四

端口映射实验

另：

ip nat source 不用在接口上指inside或者outside，要打开ip nat enable，然后转发过程不一样，路由进虚接口---NAT转换---真正路由转发，然后两边是对称的。

.