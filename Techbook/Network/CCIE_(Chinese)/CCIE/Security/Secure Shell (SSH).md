# Secure Shell (SSH)

Secure Shell (SSH)

2011年7月7日

16:01

**概述**

> 在对设备进行远程连接的方法中，最常用的是telnet，而所有通过telnet会话传递的数据都是以明文（非加密）方式传递的，当这些数据被截取之后，很轻松就能读取原文意思，为了安全性，有一种在telnet会话之上的连接方法，将数据进行加密后传输，这就是Secure Shell (SSH)。
> 
> 
> SSH共有两个版本，ver 1 和ver 2，Cisco设备在没有指定版本的情况下，默认就是指ver 1。要支持SSH，设备必须拥有支持IPSec (DES or 3DES) 加密的IOS，从12.1(1)T或之后都是可以的。除此之外，必须为设备配置主机名和域名，否则会报错。最关键的是必须配置RSA key，配置之后，SSH就自动打开了，否则不能开启。删除RSA使用命令crypto key zeroize rsa，如果密码被删除，则表示SSH被禁用。
> 
> 在Cisco设备上配置SSH，SSH分为server和client两种，server就是提供SSH登陆的设备，而client就是发起SSH会话的设备，而Cisco设备无法单独开启client，client在配置server功能后自动开启，并且自身是不需要任何命令打开的，也没有特定命令能够打开client。当SSH会话没有数据传递时，默认超时是120秒，即使是手工配置也不能超过这个值。并且SSH的最大连接数量就是VTY所允许的数量。
> 

SSH版本2的 RSA至少是768位。

**配置**

![Secure%20Shell%20(SSH)%202d563edaaf8c46da98f717b111b3c1a7/image1.png](Secure%20Shell%20(SSH)/image1.png)

**1.配置双方主机名和域名**

**注：**server和client之间的域名是可以不一样的。

**（1）配置R1的主机名和域名**

router (config)#hostname r1

r1(config)#ip domain-name cisco.com

**（2）配置R2的主机名和域名**

router (config)#hostname r2

r2(config)#ip domain-name cisco.com

> 
> 

**2.配置双方的RSA key**

**注：**双方的RSA key位数必须一致。

**(1)配置R1的RSA key**

r1(config)#crypto key generate rsa

The name for the keys will be: r1.cisco.com

Choose the size of the key modulus in the range of 360 to 2048 for your

General Purpose Keys. Choosing a key modulus greater than 512 may take

a few minutes.

How many bits in the modulus [512]: 1024

% Generating 1024 bit RSA keys ...[OK]

r1(config)#

**(2)配置R2的RSA key**

r2(config)#crypto key generate rsa

The name for the keys will be: r2.cisco.com

Choose the size of the key modulus in the range of 360 to 2048 for your

General Purpose Keys. Choosing a key modulus greater than 512 may take

a few minutes.

How many bits in the modulus [512]: 1024

% Generating 1024 bit RSA keys, keys will be non-exportable...[OK]

- Mar 1 05:24:34.940: %SSH-5-ENABLED: SSH 1.99 has been enabled

r2(config)#

**3.创建用户名和密码，client通过此用户名和密码登陆**

r1(config)#username ccie password cisco

**4.在VTY下开启认证，并指定SSH可以登陆**

r1(config)#line vty 0 181

r1(config-line)#login local

r1(config-line)#transport input ssh telnet

**5.测试SSH登陆**

r2#ssh -l ccie 10.1.1.1

Password:

r1>

**说明：**可以成功登陆

**6.查看SSH版本：**

r1#sh ip ssh

SSH Enabled - version 1.5

Authentication timeout: 120 secs; Authentication retries: 3

r1#

r2#sh ip ssh

SSH Enabled - version 1.99

Authentication timeout: 120 secs; Authentication retries: 3

r2#

**说明：**所有在2.0以下，都算是版本1。

**7.将SSH启用版本2**

**（1）修改SSH为版本2**

r2(config)#ip ssh version 2

**（2）查看版本：**

r2#sh ip ssh

SSH Enabled - version 2.0

Authentication timeout: 120 secs; Authentication retries: 3

r2#

**说明：**已经改为版本2。

注：版本1和版本2是可以互相登陆的。

**8.指定源地址**

**说明：**当使用telnet登陆远程时，可以指定源IP地址，在使用SSH时，需要在配置中修改源IP地址。

r2(config)#ip ssh source-interface Loopback0

**说明：**已将SSH的源IP地址改为Loopback0的地址。

**9同时开启两个SSH版本**

R1 (config)# no ip ssh version

**说明：**加了此命令，表示SSH两个版本同时开启。

ip domain-name cisco.com

crypto key generate rsa

transport input ssh telnet

ssh -l ccie 10.1.1.1