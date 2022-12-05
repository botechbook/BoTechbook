# RIP Lab

RIP实验

2011年6月21日

14:55

**关于命令：version**

解释：如果不打此命令，默认情况下RIP发1，接1，2

**关于命令：auto-summary**

解释：默认情况下，不管是RIPv1还是RIPv2，都会再主类网络边界自动汇总

RIPv2可以是用no auto-summary关闭边界自动汇总

对于RIPv1，此命令没有作用

**关于RIP的标配**

Router rip

version 2

no auto-summary

最佳简写：

router r

ve 2

no au

**关于命令：no ip split-horizon**

解释：关闭水平分割

RIP默认是简单水平分割

**关于水平分割的小结**

默认情况下，RIP使用简单水平分割

EIGRP使用简单水平分割，并且是触发更新

OSPF中就没有什么水平分割的概念，原因是OSPF传的是LSA，全网泛洪

**关于命令：passive-interface**

解释：只收不发

**关于命令：neighbor**

解释：单播更新，一般情况下在与passive-interface连用

**关于命令：timer**

解释：设置计时器

**关于命令：distance**

解释：修改管理距离，注意，只能本地有效

**关于命令：offset-list**

解释：修改Metric值

**关于命令：ip rip send/receive version 1/2/1 2**

解释：接口下命令，用于设置该接口可以发送和接收哪种版本的RIP消息

**关于命令：ip summary-address**

解释：接口下命令，用于设置汇总，注意RIP的汇总是在接口下做的

**关于命令：validate-update-source**

解释：默认此句是打开的，也就是当一个接口收到更新信息的时候，会查看更新信息的源是否与该接口处于同一网段，如果不在，就会丢弃该包，有些时候不需要此功能，可以使用命令no validate-update-source关闭

![RIP%20Lab%20475ae22cb89342cb87e80c9f74185a57/image1.png](RIP%20Lab/image1.png)

**关于命令：maximum-path**

解释：定义等价路径的个数

对于等价路径，默认4条，最大16条（现在有些IOS可以支持到16条），可以使用该命令进行修改

**实验一：不连续子网与第二地址**

实验拓扑：

![RIP%20Lab%20475ae22cb89342cb87e80c9f74185a57/image2.png](RIP%20Lab/image2.png)

实验需求：如上图运行RIPv1，问R1上会出现什么问题？注意，要关闭CEF才能看出现象

![RIP%20Lab%20475ae22cb89342cb87e80c9f74185a57/image3.jpg](RIP%20Lab/image3.jpg)

为了解决不连续子网的问题，使用第二地址（辅助地址）。

在接口上使用第二地址，实质上是使用第二地址同时发送更新，对方收时由于也配置了第二地址这样就可能解决这个不连续的问题，但是注意收发更新规则！！

补充：距离矢量路由协议的第三方下一跳问题

![RIP%20Lab%20475ae22cb89342cb87e80c9f74185a57/image4.png](RIP%20Lab/image4.png)

将R3的f0/0口passive掉，单播指R1，R1 f0/0接口关闭水平分割，看第三方下一跳

**实验二：RIPv2的验证**

RIPv2的验证有明文和MD5验证两种

R2(config)#key chain RIP_auth （本地有效）

R2(config-keychain)#key 1 （建议两端一致）(可以定义多个KEY值，按从小到大的顺序进行匹配，发送KEY值时也是发送最小的一个，还可以设定KEY值的有效时间。)

R2(config-keychain-key)#key-string cisco

R2(config-if)#ip rip authentication key-chain RIP_auth

R2(config-if)#ip rip authentication mode [md5|text]

RIP中每一个路由更新最大可包含25条路由,做了明文认证后只能包含24条，做了MD5认证后只能包含23条。

R2(config-keychain-key)#Accept-lifetime 04:00:00 jan 2006 infinite 定时接收

R2(config-keychain-key)#Send-lifetime 04:00:00 jan 2006 04:01:00 jan 2006 定时发送

R2(config-keychain-key)#Send-lifetime 04:00:00 jan 2006 duration 300 有效期300S

明文认证总结 ： 只发送key ID最小的KEY 并不需要KEY ID，接收方与KEY列表中所有KEY匹配，只有一个能匹配上则通过认证。

密文认证总结： 只发送最小的KEY ID，并且携带KEY ID，当接收时，先只匹配相同KEY ID密钥，如果不匹配，则通不过认证，但如果没有相同KEY ID ，只向下查找一次大的KEY ID密钥，如果有相同大KEY ID，但不匹配也不通过认证，如果仍然没有不是相同的KEY ID则也不通过认证。

注意点：不要在密码后面加入空格

**实验三：RIPv2的汇总**

**实验四：RIP的不等值负载均衡**

**实验五：计时器配置**

**实验六：v1/v2的兼容性**

![RIP%20Lab%20475ae22cb89342cb87e80c9f74185a57/image5.jpg](RIP%20Lab/image5.jpg)

**R1、R5运行RIPv1，R3、R4运行RIPv2**

**所以在R2上配置f0/0口收1，接1；f1/0口发1、2；f2/0口默认（收2）**

**在R4上debug ip rip**

**R5接收不到R4的lo0路由，解决办法2个：**

**（1）配置R5收发两个版本**

**（2）关闭f1/0水平分割**

**实验七：配置单播更新**

**实验八：RIP产生缺省路由**

**rip传递默认路由的5种方法**

**在一个单出口网络内启用RIP协议，在网络出口处的路由器需要向RIP域内传播一条默认路由，这样，域内的路由器就可以通过默认路由访问外部网络。通过RIP传递默认路由共有5种方法:**

**1 default-informatio**

**2 手工写一条默认路由（到NULL0） 然后重分布到RIP中**

**3 手工写一条默认路由（到NULL0） 在进程中宣告**

**4 ip default-network**

**5 在接口汇总 0.0.0.0/0 到NULL0的路由**

- *******************************************************************

**方法1**

**default-information originate**

**此外，在default-information originate可以调用一个route-map来匹配一个接口或路由，当这个路由有效的时候才会传递默认路由。**

**首先我们在R2上建立一个loopback接口，并将它宣告到RIP中，然后用ACL来匹配这个接口，建立route-map调用这个ACL，最后在default-information originate命令后调用这个route-map**

**－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－方法2 手工写一条默认路由（到NULL0） 然后重分布到RIP中**

**r2(config)#ip route 0.0.0.0 0.0.0.0 null 0 /在R2上建立一条默认路由**

**r2(config-router)#redistribute static /重分布静态路由到RIP中**

**－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－方法3 手工写一条默认路由（到NULL0） 在进程中宣告**

**r2(config)#ip route 0.0.0.0 0.0.0.0 null 0**

R1(config)#router rip

R1(config-router)#network 0.0.0.0

**－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－方法4 ip default-network**

**r2(config)#ip default-network 23.0.0.0 /建立一个缺省网络**

如写成ip default-network 12.1.1.0

会自动生成ip route 12.0.0.0 255.0.0.0 12.1.1.0

**－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－方法5 在接口汇总 0.0.0.0/0 到NULL0的路由**

**r2(config)#ip route 0.0.0.0 0.0.0.0 null 0 /先建立一条默认路由**

**interface Serial1/0**

**ip summary-address rip 0.0.0.0 0.0.0.0 /在接口上手工汇总这条默认路由**