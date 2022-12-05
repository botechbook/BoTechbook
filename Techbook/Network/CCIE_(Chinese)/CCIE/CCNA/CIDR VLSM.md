# CIDR VLSM

CIDR/VLSM

2009年9月13日

8:34

> 掌握IP地址分类，子网掩码的作用，识别网络标识号、主机标识号，子网的数目、主机的数目
> 
> 
> 1、10—>2进制转换
> 
> ![CIDR%20VLSM%20f22c90f7767d4fe6a03a4aedf0bcf31e/image1.png](CIDR%20VLSM/image1.png)
> 
> 2、IP地址**分类**
> 
> ![CIDR%20VLSM%20f22c90f7767d4fe6a03a4aedf0bcf31e/image2.png](CIDR%20VLSM/image2.png)
> 
> A 0.0.0.0 - 126.255.255.255
> 
> B 128.0.0.0 - 191.255.255.255
> 
> C 192.0.0.0 - 223.255.255.255
> 
> D 224.0.0.0 - 239.255.255.255
> 
> E 240.0.0.0 - 255.255.255.255
> 
> 一些**特殊**的IP 地址:
> 
> 1.IP 地址127.0.0.1:本地回环(loopback)测试地址（注意和路由器的loopback接口区分开）
> 
> 2.广播地址:255.255.255.255
> 
> 3.IP 地址0.0.0.0代表任何网络（0代表网段号）
> 
> 4.主机号全为1:代表该网段的所有主机
> 
> 广播地址TCP/IP 协议规定,主机号部分各位全为1 的IP 地址用于广播.所谓广播地址指同时向网上所有的主机发送报文,也就是说,不管物理网络特性如何,Internet 网支持广播传输.如136.78.255.255 就是B 类地址中的一个广播地址,你将信息送到此地址,就是将信息送给网络号为136.78 的所有主机.
> 
> **私有I**P地址:
> 1）.A 类地址中:10.0.0.0 到10.255.255.255
> 2）.B 类地址中:172.16.0.0 到172.31.255.255
> 3）.C 类地址中:192.168.0.0 到192.168.255.255
> 
> 为什么在配置NAT时内网一定用私有地址？
> 
> 如果内网不用私有地址，万一你要访问的网络服务使用的刚好和你布在内网的地址重了你就悲剧了。。。。
> 
> 3、可用主机地址计算
> 
> 二的N（主机位后面连续零的个数）次方—2
> 
> Host = 2^n-2
> 
> ![CIDR%20VLSM%20f22c90f7767d4fe6a03a4aedf0bcf31e/image3.png](CIDR%20VLSM/image3.png)
> 
> ![CIDR%20VLSM%20f22c90f7767d4fe6a03a4aedf0bcf31e/image4.png](CIDR%20VLSM/image4.png)
> 
> 4、子网划分好处
> 1）.缩减网络流量
> 2）.优化网络性能
> 3）.简化管理
> 4）.更为灵活地形成大覆盖范围的网络
> 
> ![CIDR%20VLSM%20f22c90f7767d4fe6a03a4aedf0bcf31e/image5.jpg](CIDR%20VLSM/image5.jpg)
> 
> ![CIDR%20VLSM%20f22c90f7767d4fe6a03a4aedf0bcf31e/image6.png](CIDR%20VLSM/image6.png)
> 
> ![CIDR%20VLSM%20f22c90f7767d4fe6a03a4aedf0bcf31e/image7.png](CIDR%20VLSM/image7.png)
> 
> ![CIDR%20VLSM%20f22c90f7767d4fe6a03a4aedf0bcf31e/image8.png](CIDR%20VLSM/image8.png)
> 
> ![CIDR%20VLSM%20f22c90f7767d4fe6a03a4aedf0bcf31e/image9.png](CIDR%20VLSM/image9.png)
> 
> ![CIDR%20VLSM%20f22c90f7767d4fe6a03a4aedf0bcf31e/image10.png](CIDR%20VLSM/image10.png)
> 
> ![CIDR%20VLSM%20f22c90f7767d4fe6a03a4aedf0bcf31e/image11.png](CIDR%20VLSM/image11.png)
> 
> **=======================================**
> 
> **子网划分练习**
> 
> <<子网计算.txt>>
> 
> **=======================================**
> 
> **VLSM**
> 
> 变长子网掩码(Variable-Length Subnet Masks,VLSM)的出现是打破传统的以类(class)为标准的地址划分方法,是为了缓解IP 地址紧缺而产生的。
> 
> 作用:节约IP 地址空间
> 注意事项：使用VLSM 时,所采用的路由协议必须能够支持它,这些路由协议包括RIPv2,OSPF,EIGRP 和BGPv4。
> 
> 地址范围: 192.168.1.64 - 192.168.1.79
> 
- 前缀长度为/28
- 192.168.1.64/28

[Untitled](CIDR%20VLSM/Untitled%20Database%2005c326f2e6eb4a22a3bfd5e827519a4d.csv)

> 
> 
> 
> **CIDR classless internal domain router**
> 
> **无类域间路由**
> 
> CIDR的概念：忽略A、B、C类网络的规则，定义前缀相同的一组网络为一个块，即一条路由条目。（如：199.0.0.0/8）
> 
- 减少了网络数目，缩小了路由选择表。
- 从网络流量、CPU和内存方面说，开销更低。
- 对网络进行编址时，灵活性更大。

> 
> 
- 
    
    ![CIDR%20VLSM%20f22c90f7767d4fe6a03a4aedf0bcf31e/image12.png](CIDR%20VLSM/image12.png)
    

> 
> 
> 
> ![CIDR%20VLSM%20f22c90f7767d4fe6a03a4aedf0bcf31e/image13.png](CIDR%20VLSM/image13.png)
> 

A./24 10.1.0.0--10.1.0. 255

B./25 10.1.0.