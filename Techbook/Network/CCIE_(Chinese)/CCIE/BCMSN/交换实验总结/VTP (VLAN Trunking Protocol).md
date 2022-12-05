# VTP (VLAN Trunking Protocol)

VTP (VLAN Trunking Protocol)

2011年7月7日

14:23

> 在一个拥有多台交换机的交换网络中，通常会在多台交换机上配置相同的VLAN，并且也会对多个接口做相同的配置。
> 
> 
> 对于需要对多个接口做相同的配置，通过快速接口配置，能够轻松实现，提高工作效率。而对于在多台交换机上做相同的VLAN配置，则通过VTP来实现。
> 
> VTP为了在多台交换机上配置相同的VLAN，通过将一台交换机的VLAN向其它交换机传播的方法来完成，其它交换机在接收到VLAN信息后，然后更新自己的VLAN数据库，以达到同步。
> 
> 要将自己的VLAN信息发送到网络中，交换机上必须配置Trunk，IEEE 802.1Q和ISL都支持，通过Trunk相连的交换机便能收到对方发来的VLAN信息。
> 
> VTP通过域来管理网络中的交换机，任何交换机发出的VLAN信息只能在一个域内传播，只有相同域的交换机才能接收此VLAN信息，并且根据接收到的VLAN信息更新自己的VLAN数据库。交换机是否在同一个域，是通过域名来分辨的，比如域名ccie与域名ccie属于同一个域，而域名ccie与域名cisco就属于不同的域。默认交换机的域名为空，但是最重点的，需要大家牢记的是，如果自己的域名为空，则表示与任何非空域名相同，也就是说如果对方有域名，而自己却没有域名，则自己和对方属于相同的域。
> 
> 在VTP中，交换机分三种模式：Server、Client、Transparent，他们的功能分别如下：
> 
> **Server：**
> 
> 可以创建，更改和删除VLAN，可以更改任何VTP参数，可以将自己的VLAN信息向网络中发送，并且也会根据收到的VLAN信息来选择是否同步自己的VLAN数据库。
> 
> **Client：**
> 
> 不能创建，更改和删除VLAN，但是可以更改部分VTP参数，也可以将自己的VLAN信息向网络中发送，并且也会根据收到的VLAN信息来选择是否同步自己的VLAN数据库。
> 
> **Transparent：**
> 
> 可以创建，更改和删除VLAN，可以更改任何VTP参数，不会将自己的VLAN信息向网络中发送，但是会转发接收到其它交换机发来的VLAN信息，并且不会根据收到的VLAN信息来同步自己的VLAN数据库。
> 
> 从上可以看出，Server与Client的唯一区别在于，Server可以随意修改自己的VLAN信息和VTP参数，而Client则不能，除此之外，其它完全相同。
> 
> Server与Transparent的区别在于, Transparent不会将自己的VLAN信息发送到网络中，并且也不会向别人同步自己的VLAN数据库。
> 
> 所以最终的结论是，如果希望从网络中接收VLAN信息来同步自己的VLAN数据库，配置成Server与Client都可以实现，要将自己的VLAN信息发送到网络中，Server与Client也都能实现。如果要具有修改VLAN数据库的权限，只有Server与Transparent能做到，Client是不能自己更改VLAN数据库的。
> 
> Server与Client发出的VLAN信息，都有一个configuration revision号码，每修改一次VLAN信息，configuration revision号则加1，如果做相同操作，configuration revision号是不会有变化的。configuration revision号越高（数字越大），则说明VLAN信息越新。
> 
> Server与Client从网络中接收到VLAN信息后，是否根据此信息同步自己的VLAN数据库，则要将自己的VLAN信息与接收到的作对比，如果接收到的VLAN信息的configuration revision号比自己的大，则将自己的VLAN数据库与接收到的进行同步，如果configuration revision号比自己的小或者相等，则放弃同步。域中总是先使用configuration revision号码最高的VLAN信息
> 
> 默认情况下，交换机的域名为空，无论是Server还是Client，在空域名的情况下，是不会将自己的VLAN信息往外发的，但是在域名为空的情况下，无论收到任何VLAN信息，只要configuration revision号比自己的大，就会同步自己的VLAN数据库，并且添加上相同的域名。域名在配置之后，只能更改，但不能删除。如果网络中全是Client，可想而知就不要配置域名了。
> 
> 在谈及VTP，不得不详细解释VLAN，交换机所支持的VLAN数为1-4094，VLAN 1-1005称为Normal VLAN，VLAN 1006 – 4094称为Extended VLAN。Normal VLAN（1-1005）是保存在VLAN数据库中的，也就是vlan.dat，而Extended VLAN(1006-4094)是保存在startup-config中的。Normal VLAN（1-1005）可以随意配置，而Extended VLAN(1006-4094)只能在VTP模式为Transparent时才能配置。所以，VTP只能将Normal VLAN（1-1005）在网络中更新。当同时配置了1-1005的VLAN和1006-4096的VLAN，在删除vlan.dat后，1-1005的VLAN会被删除，但1006-4096的VLAN还在，如果删除了startup-config，那么则会删除1006-4096的VLAN，但不会影响1-1005的VLAN。
> 
> VTP现有两个版本，ver 1和ver 2，默认为ver 1，因为Transparent会转发接收到其它交换机发来的VLAN信息，但是当自己的VTP版本为ver 1时，只有自己接收到的VLAN信息的域名和VTP版本与自己的相同，才会转发，但如果自己为ver 2，则无论收到任何VLAN信息都会转发。
> 
> 如果域中一台交换机开了VTP ver 2，则应该全部都要打开，但是只有Server和Transparent才能更改VTP版本，而Client会根据收到的VLAN信息同步自己的VTP版本。
> 
> 交换机还可以为VTP配置密码，当配置密码后，即使VTP域名相同，如果密码不同，也不能根据接收到的VLAN信息更新自己的VLAN数据库。要确认VTP密码是否相同，双方的MD5 digest值必须相同。
> 
> **附:**在交换机最新的IOS版本中,如果3560的 12.2(52)SE ,已经加入对VTP version 3的支持,最大的特点就是,可以在VTP信息中传递Extended VLAN(1006-4094),但改为Ver 3之后,不能再切换到Ver 1和Ver 2.
> 
> **重点说明：**
> 
> ★ 交换机的配置信息保存在nvram存储器的startup-config文件中。
> 
> ★ 而Flash中的文件config.text与nvram存储器的startup-config文件完全相同，删除任何一个，即同时删除两个。（注：此规则不完全适用于高端交换机）
> 
> ★交换机的Normal VLAN（1-1005）是保存在文件vlan.dat中，而Extended VLAN(1006-4094)是保存在nvram存储器的文件startup-config中。
> 
> ★ VTP信息全部保存在vlan.dat中。
> 
> ★ 当VTP模式为Transparent时，所有VLAN信息和VTP信息除了保存在vlan.dat中之外，还会保存在nvram存储器的startup-config中。
> 
> ★ 当VTP模式为Server和Client时，所有VLAN信息和VTP信息只保存在vlan.dat中，不会保存在nvram存储器的startup-config中，所以show running-config时，也是看不到VLAN信息的。
> 
> ★ 域名为空的交换机是不会发送任何VTP信息的。
> 
> ★ 将模式改为Transparent，可以清除所有VTP信息。
> 
> **VTP Pruning**
> 

![VTP%20(VLAN%20Trunking%20Protocol)%20f524e437fec34446839824b2dced8242/image1.png](VTP%20(VLAN%20Trunking%20Protocol)/image1.png)

如上图所示，当交换机SW1收到broadcast, multicast以及unknown unicast后，会在所有Trunk上进行广播发送，最终结果造成SW2会转发给SW3，也会转发给SW4，而只有SW4上接有终端，也就是说只有SW4需要接收这些广播，对于SW3，转发这些广播是毫无意义的，因为自己没有连接终端。

对于上述情况，当一台交换机在某VLAN进入广播发送数据时，流量应该只被发送到在此VLAN连接了终端的交换机，而对于没有连接终端的交换机，很明显，是没有必须接收这样的广播了。**为了节省带宽，提高网络性能**，VTP Pruning限制交换机只将广播发送到连接了终端的交换机。如果上图中开启了VTP Pruning，则SW1发出的广播只会被发送到SW2，再转发到SW4，而不会转发到SW3。

在Trunk上，只有某VLAN允许被剪除，那么在此VLAN的广播才不会发到没有连接终端的交换机，如果不允许剪除，则广播照常。**允许被剪除的VLAN范围是2-1001，而VLAN1和1002-1005以及1006-4094是不能被剪除的，开启VTP Pruning后，默认VLAN2-1001被剪除，但剪除的VLAN号可以在Trunk上随意定义。**

**VTP模式为Transparent时，是不支持VTP Pruning的，**但无论支持VTP Ver 1还是 Ver 2都支持VTP Pruning。

![VTP%20(VLAN%20Trunking%20Protocol)%20f524e437fec34446839824b2dced8242/image2.png](VTP%20(VLAN%20Trunking%20Protocol)/image2.png)

**说明：**以上图为例，配置VTP。第一部分为验证交换机文件系统，第二部分为验证VTP。

**第一部分 （验证交换机文件系统）**

**1.在SW1上配置VTP**

**（1）创建vlan 2000，vlan 3000**

sw1(config)#vlan 2000

sw1(config-vlan)#exit

% Failed to create VLANs 2000

Extended VLAN(s) not allowed in current VTP mode.

%Failed to commit extended VLAN(s) changes.

sw1(config)#

**说明：**因为交换机默认为Server模式，所以不能创建Extended VLAN(1006-4094)。

**（2）在VTPTransparent下创建vlan 2000，vlan 3000**

sw1(config)#vtp domain ccie

sw1(config)#vtp mo transparent

Setting device to VTP TRANSPARENT mode.

sw1(config)#vlan 2000

sw1(config-vlan)#exit

sw1(config)#vlan 3000

sw1(config-vlan)#exit

sw1(config)#

**说明：**Vlan 2000在transparent模式下创建成功。

**(3)查看VLAN**

sw1#sh vlan

VLAN Name                             Status    Ports

- --- -------------------------------- --------- -------------------------------

1    default                          active    Fa0/1, Fa0/2, Fa0/3, Fa0/4

Fa0/5, Fa0/6, Fa0/7, Fa0/8

Fa0/9, Fa0/10, Fa0/11, Fa0/12

Fa0/13, Fa0/14, Fa0/15, Fa0/16

Fa0/17, Fa0/18, Fa0/23, Fa0/24

Gi0/1, Gi0/2

1002 fddi-default                     act/unsup

1003 token-ring-default               act/unsup

1004 fddinet-default                  act/unsup

1005 trnet-default                    act/unsup

2000 VLAN2000                         active

3000 VLAN3000                         active

（输出被省略）

sw1#

**说明：**Vlan 2000在transparent模式下创建成功。

**（4）在SW1上创建VLAN 2-5，以及VLAN 3000**

sw1(config)#vlan 2

sw1(config-vlan)#exit

sw1(config)#vlan 3

sw1(config-vlan)#exit

sw1(config)#vlan 4

sw1(config-vlan)#exit

sw1(config)#vlan 5

sw1(config-vlan)#exit

**(5)保存并查看**

保存：

sw1#wr

Building configuration...

[OK]

sw1#

**查看VLAN：**

sw1#sh vlan

VLAN Name                             Status    Ports

- --- -------------------------------- --------- -------------------------------

1    default                          active    Fa0/1, Fa0/2, Fa0/3, Fa0/4

Fa0/5, Fa0/6, Fa0/7, Fa0/8

Fa0/9, Fa0/10, Fa0/11, Fa0/12

Fa0/13, Fa0/14, Fa0/15, Fa0/16

Fa0/17, Fa0/18, Fa0/19, Fa0/20

Fa0/21, Fa0/22, Fa0/23, Fa0/24

Gi0/1, Gi0/2

2    VLAN0002                         active

3    VLAN0003                         active

4    VLAN0004                         active

5    VLAN0005                         active

1002 fddi-default                     act/unsup

1003 token-ring-default               act/unsup

1004 fddinet-default                  act/unsup

1005 trnet-default                    act/unsup

2000 VLAN2000                         active

3000 VLAN3000                         active

（输出被省略）

sw1#

**查看VTP：**

sw1#sh vtp sta

VTP Version                     : 2

Configuration Revision          : 0

Maximum VLANs supported locally : 1005

Number of existing VLANs        : 9

VTP Operating Mode              : Transparent

VTP Domain Name                 : ccie

VTP Pruning Mode                : Disabled

VTP V2 Mode                     : Disabled

VTP Traps Generation            : Disabled

MD5 digest                      : 0x63 0xE7 0xF7 0x4B 0xFD 0xED 0x17 0xAA

Configuration last modified by 0.0.0.0 at 3-1-93 00:02:01

sw1#

**说明：**VLAN创建成功，VTP也修改成功。

**（6）查看文件系统**

sw1#dir flash:

Directory of flash:/

2  -rwx     7457899   Mar 1 1993 06:35:16 +00:00  c3550-ipservicesk9-mz.122-35.SE3.bin

3  -rwx         796   Mar 1 1993 00:02:44 +00:00  vlan.dat

4  -rwx           0   Mar 1 1993 05:57:14 +00:00  env_vars

5  -rwx          24   Mar 1 1993 05:57:14 +00:00  system_env_vars

6  -rwx        2416   Mar 1 1993 00:03:10 +00:00  config.text

7  -rwx          24   Mar 1 1993 00:03:10 +00:00  private-config.text

15998976 bytes total (8535040 bytes free)

sw1#dir nv

sw1#dir nvram:

Directory of nvram:/

380  -rw-        2416                    <no date>  startup-config

381  ----          24                    <no date>  private-config

393216 bytes total (390724 bytes free)

sw1#

**说明：**存在VLAN信息和VTP信息的vlan.dat已经生成；nvram中的startup-config也已经生成，相应的config.text也已经生成。

**（7）共享文件系统**

sw1(config)#int vlan 1

sw1(config-if)#ip add 1.1.1.1 255.255.255.0

sw1(config)#tftp-server flash:vlan.dat

sw1(config)#tftp-server flash:config.text

sw1(config)#tftp-server nvram:startup-config

**说明：**交换机已经将vlan.dat，config.text，startup-config通过TFTP在网络中共享。

**2.通过SW2验证SW1的vlan.dat**

**（1）查看当前VTP和VLAN**

sw2#sh vtp status

VTP Version                     : 2

Configuration Revision          : 0

Maximum VLANs supported locally : 1005

Number of existing VLANs        : 5

VTP Operating Mode              : Server

VTP Domain Name                 :

VTP Pruning Mode                : Disabled

VTP V2 Mode                     : Disabled

VTP Traps Generation            : Disabled

MD5 digest                      : 0x57 0xCD 0x40 0x65 0x63 0x59 0x47 0xBD

Configuration last modified by 0.0.0.0 at 0-0-00 00:00:00

Local updater ID is 1.1.1.2 on interface Vl1 (lowest numbered VLAN interface found)

sw2#

sw2#sh vlan

VLAN Name                             Status    Ports

- --- -------------------------------- --------- -------------------------------

1    default                          active    Fa0/1, Fa0/2, Fa0/3, Fa0/4

Fa0/5, Fa0/6, Fa0/7, Fa0/8

Fa0/9, Fa0/10, Fa0/11, Fa0/12

Fa0/13, Fa0/14, Fa0/15, Fa0/16

Fa0/17, Fa0/18, Fa0/19, Fa0/20

Fa0/21, Fa0/22, Fa0/24, Gi0/1

Gi0/2

1002 fddi-default                     act/unsup

1003 token-ring-default               act/unsup

1004 fddinet-default                  act/unsup

1005 trnet-default                    act/unsup

（输出被省略）

sw2#

**说明：**SW2的VLAN和VTP为默认配置。

**（2）复制SW1的vlan.dat**

sw2(config)#int vlan 1

sw2(config-if)#ip add 1.1.1.2 255.255.255.0

sw2#copy tftp: flash:

Address or name of remote host []? 1.1.1.1

Source filename []? vlan.dat

Destination filename [vlan.dat]?

Accessing tftp://1.1.1.1/vlan.dat...

Loading vlan.dat from 1.1.1.1 (via Vlan1): !

[OK - 796 bytes]

796 bytes copied in 0.032 secs (24875 bytes/sec)

sw2#

**说明：**SW1的vlan.dat已经被SW2复制，接下来可以验证vlan.dat中的内容。

**（3）查看SW2复制的SW1的vlan.dat**

sw2#dir flash:

Directory of flash:/

2  -rwx     7457899   Mar 1 1993 06:33:13 +00:00  c3550-ipservicesk9-mz.122-35.SE3.bin

3  -rwx         796   Mar 1 1993 00:10:41 +00:00  vlan.dat

4  drwx           0   Mar 1 1993 02:51:43 +00:00  test

7  -rwx           0   Mar 1 1993 01:52:09 +00:00  system_env_vars

8  -rwx           0   Mar 1 1993 01:52:09 +00:00  env_vars

15998976 bytes total (8538624 bytes free)

sw2#

**说明：**可以看到vlan.dat与SW1的vlan.dat相同。

**(4)在SW2上使用SW1的vlan.dat**

**说明：**因为SW1的vlan.dat已经复制到SW2的flash中，所以重启SW2后，便可读取其中的内容。

重启SW2后，查看VLAN信息和VTP信息：

**查看VLAN信息：**

Sw2#sh vlan

VLAN Name                             Status    Ports

- --- -------------------------------- --------- -------------------------------

1    default                          active    Fa0/1, Fa0/2, Fa0/3, Fa0/4

Fa0/5, Fa0/6, Fa0/7, Fa0/8

Fa0/9, Fa0/10, Fa0/11, Fa0/12

Fa0/13, Fa0/14, Fa0/15, Fa0/16

Fa0/17, Fa0/18, Fa0/19, Fa0/20

Fa0/21, Fa0/22, Fa0/23, Fa0/24

Gi0/1, Gi0/2

2    VLAN0002                         active

3    VLAN0003                         active

4    VLAN0004                         active

5    VLAN0005                         active

1002 fddi-default                     act/unsup

1003 token-ring-default               act/unsup

1004 fddinet-default                  act/unsup

1005 trnet-default                    act/unsup

（输出被省略）

Sw2#

**查看VTP信息：**

Sw2#sh vtp sta

VTP Version                     : 2

Configuration Revision          : 0

Maximum VLANs supported locally : 1005

Number of existing VLANs        : 9

VTP Operating Mode              : Transparent

VTP Domain Name                 : ccie

VTP Pruning Mode                : Disabled

VTP V2 Mode                     : Disabled

VTP Traps Generation            : Disabled

MD5 digest                      : 0x63 0xE7 0xF7 0x4B 0xFD 0xED 0x17 0xAA

Configuration last modified by 0.0.0.0 at 3-1-93 00:02:01

Sw2#

**说明：**可以验证，vlan.dat中只有1-1005的VLAN，并且VTP信息保存在vlan.dat中。

**3.通过SW3验证SW1的startup-config**

**（1）查看SW3当前的startup-config**

sw3#dir nvram:

Directory of nvram:/

382  -rw-           0                    <no date>  startup-config

383  ----           0                    <no date>  private-config

393216 bytes total (393164 bytes free)

sw3#

**说明：**SW3当前的startup-config为空。

**（2）复制SW1的startup-config**

sw3(config)#int vlan 1

sw3(config-if)#ip add 1.1.1.3 255.255.255.0

sw3#copy tftp: flash:

Address or name of remote host [1.1.1.1]?

Source filename [startup-config]?

Destination filename [startup-config]?

Accessing tftp://1.1.1.1/startup-config...

Loading startup-config from 1.1.1.1 (via Vlan1): !

[OK - 2416 bytes]

2416 bytes copied in 0.088 secs (27455 bytes/sec)

sw3#

**说明：**SW1的startup-config已经被SW3复制，接下来可以验证startup-config中的内容。

**（3）在SW3上导入复制的SW1的startup-config**

sw3#copy flash:startup-config running-config

Destination filename [running-config]?

Failed to generate persistent self-signed certificate.

Secure server will use temporary self-signed certificate.

2416 bytes copied in 0.416 secs (5808 bytes/sec)

sw1#

**说明：**因为使用了SW1的startup-config，所以主机名也变成了SW1。

**（4）查看VLAN与VTP信息**

**查看VLAN信息：**

sw1#sh vlan

VLAN Name                             Status    Ports

- --- -------------------------------- --------- -------------------------------

1    default                          active    Fa0/1, Fa0/2, Fa0/3, Fa0/4

Fa0/5, Fa0/6, Fa0/7, Fa0/8

Fa0/9, Fa0/10, Fa0/11, Fa0/12

Fa0/13, Fa0/14, Fa0/15, Fa0/16

Fa0/17, Fa0/18, Fa0/19, Fa0/20

Fa0/21, Fa0/22, Fa0/23, Fa0/24

Gi0/1, Gi0/2

2    VLAN0002                         active

3    VLAN0003                         active

4    VLAN0004                         active

5    VLAN0005                         active

1002 fddi-default                     act/unsup

1003 token-ring-default               act/unsup

1004 fddinet-default                  act/unsup

1005 trnet-default                    act/unsup

2000 VLAN2000                         active

3000 VLAN3000                         active

（输出被省略）

sw1#

**查看VTP：**

sw1#sh vtp status

VTP Version                     : 2

Configuration Revision          : 0

Maximum VLANs supported locally : 1005

Number of existing VLANs        : 9

VTP Operating Mode              : Transparent

VTP Domain Name                 : ccie

VTP Pruning Mode                : Disabled

VTP V2 Mode                     : Disabled

VTP Traps Generation            : Disabled

MD5 digest                      : 0x63 0xE7 0xF7 0x4B 0xFD 0xED 0x17 0xAA

Configuration last modified by 0.0.0.0 at 0-0-00 00:00:00

sw1#

**说明：**SW3上除了拥有VLAN 1-1005外，1006-4094的VLAN也存在，说明在Transparent模式下，VLAN信息不仅保存在vlan.dat中，还保存在startup-config中，并且VTP也成功保存在startup-config中。

**4.通过SW4验证SW1的config.text**

**（1）从SW4复制SW1的config.text**

sw4(config)#int vlan 1

sw4(config-if)#ip address 1.1.1.4 255.255.255.0

sw4#copy tftp: flash:

Address or name of remote host []? 1.1.1.1

Source filename []? config.text

Destination filename [config.text]?

Accessing tftp://1.1.1.1/config.text...

Loading config.text from 1.1.1.1 (via Vlan1): !

[OK - 2416 bytes]

2416 bytes copied in 0.052 secs (46462 bytes/sec)

sw4#

**说明：** SW1的vlan.dat已经被SW4复制，接下来可以验证config.text中的内容。

**（2）SW4上使用SW1的config.text**

**说明：**因为SW4上没有保存配置文件，但拥有了SW1的config.text，所以重启后，就会读取config.text的配置，重启后，SW1的config.text内容就被验证

重启SW4，查看结果：

**查看VLAN：**

sw1#sh vlan

VLAN Name                             Status    Ports

- --- -------------------------------- --------- -------------------------------

1    default                          active    Fa0/1, Fa0/2, Fa0/3, Fa0/4

Fa0/5, Fa0/6, Fa0/7, Fa0/8

Fa0/9, Fa0/10, Fa0/11, Fa0/12

Fa0/13, Fa0/14, Fa0/15, Fa0/16

Fa0/17, Fa0/18, Fa0/19, Fa0/20

Fa0/21, Fa0/22, Fa0/23, Fa0/24

Gi0/1, Gi0/2

2    VLAN0002                         active

3    VLAN0003                         active

4    VLAN0004                         active

5    VLAN0005                         active

1002 fddi-default                     act/unsup

1003 token-ring-default               act/unsup

1004 fddinet-default                  act/unsup

1005 trnet-default                    act/unsup

2000 VLAN2000                         active

3000 VLAN3000                         active

（输出被省略）

sw1#

**查看VTP：**

sw1#sh vtp status

VTP Version                     : 2

Configuration Revision          : 0

Maximum VLANs supported locally : 1005

Number of existing VLANs        : 9

VTP Operating Mode              : Transparent

VTP Domain Name                 : ccie

VTP Pruning Mode                : Disabled

VTP V2 Mode                     : Disabled

VTP Traps Generation            : Disabled

MD5 digest                      : 0x63 0xE7 0xF7 0x4B 0xFD 0xED 0x17 0xAA

Configuration last modified by 0.0.0.0 at 0-0-00 00:00:00

sw1#

**说明：**因为使用了SW1的config.text，所以主机名也变成了SW1。并且VLAN与VTP与SW1完全相同，说明config.text与startup-config完全相同。

**5.在SW1上验证VLAN存放位置**

**（1）在SW1上删除startup-config**

**说明：**由于删除vlan.dat是没有用的，因为Transparent会将所有VLAN，如VLAN 1006-4094存放在startup-config中，即使删了vlan.dat，所有内容还存在，所以直接删除startup-config来测试：

sw1#erase nvram:

Erasing the nvram filesystem will remove all configuration files! Continue? [confirm]

[OK]

Erase of nvram: complete

sw1#

sw1#dir nvram:

Directory of nvram:/

382  -rw-           0                    <no date>  startup-config

383  ----           0                    <no date>  private-config

393216 bytes total (393164 bytes free)

sw

**说明：**startup-config已经为空，因为已被删除。

**（2）重启SW1后查看结果：**

**查看VLAN：**

Switch#sh vlan

VLAN Name                             Status    Ports

- --- -------------------------------- --------- -------------------------------

1    default                          active    Fa0/1, Fa0/2, Fa0/3, Fa0/4

Fa0/5, Fa0/6, Fa0/7, Fa0/8

Fa0/9, Fa0/10, Fa0/11, Fa0/12

Fa0/13, Fa0/14, Fa0/15, Fa0/16

Fa0/17, Fa0/18, Fa0/19, Fa0/20

Fa0/21, Fa0/22, Fa0/23, Fa0/24

Gi0/1, Gi0/2

2    VLAN0002                         active

3    VLAN0003                         active

4    VLAN0004                         active

5    VLAN0005                         active

1002 fddi-default                     act/unsup

1003 token-ring-default               act/unsup

1004 fddinet-default                  act/unsup

1005 trnet-default                    act/unsup

（输出被省略）

Switch#

**查看VTP：**

Switch#sh vtp status

VTP Version                     : 2

Configuration Revision          : 0

Maximum VLANs supported locally : 1005

Number of existing VLANs        : 9

VTP Operating Mode              : Transparent

VTP Domain Name                 : ccie

VTP Pruning Mode                : Disabled

VTP V2 Mode                     : Disabled

VTP Traps Generation            : Disabled

MD5 digest                      : 0x63 0xE7 0xF7 0x4B 0xFD 0xED 0x17 0xAA

Configuration last modified by 0.0.0.0 at 3-1-93 00:02:01

Switch#

**说明：**因为VTP信息和VLAN 1-1005存放在vlan.dat中，所以删除了startup-config,只是删除了VLAN 1006-4094，而VTP信息和VLAN 1-1005仍旧存在。

**第二部分（验证VTP）**

![VTP%20(VLAN%20Trunking%20Protocol)%20f524e437fec34446839824b2dced8242/image2.png](VTP%20(VLAN%20Trunking%20Protocol)/image2.png)

**说明：**还是以上图为例，验证VTP

**1.关闭交换机上所有端口**

**（1）在所有交换机上关闭所有端口**

int range f0/1 - 24

shutdown

**2.查看默认VTP**

**（1）所有交换机上，默认VTP如下：**

switch#sh vtp status

VTP Version                     : 2

Configuration Revision          : 0

Maximum VLANs supported locally : 1005

Number of existing VLANs        : 5

VTP Operating Mode              : Server

VTP Domain Name                 :

VTP Pruning Mode                : Disabled

VTP V2 Mode                     : Disabled

VTP Traps Generation            : Disabled

MD5 digest                      : 0x57 0xCD 0x40 0x65 0x63 0x59 0x47 0xBD

Configuration last modified by 0.0.0.0 at 0-0-00 00:00:00

Local updater ID is 0.0.0.0 (no valid interface found)

switch#

**说明：**默认VTP域名为空，且默认模式为Server。

**3.配置SW1的VTP**

**（1）在SW1上配置VLAN**

sw1(config)#vlan 3

sw1(config-vlan)#exi

sw1(config)#vlan 5

sw1(config-vlan)#exi

sw1(config)#vlan 7

sw1(config-vlan)#exi

sw1(config)#vlan 9

sw1(config-vlan)#exit

sw1(config)#vtp domain ccie

**说明：**SW1上的VLAN为3 5 7 9 ，全部是奇数，VTP域名为ccie。

**（2）查看SW1的VTP信息**

sw1#sh vtp status

VTP Version                     : 2

Configuration Revision          : 4

Maximum VLANs supported locally : 1005

Number of existing VLANs        : 9

VTP Operating Mode              : Server

VTP Domain Name                 : ccie

VTP Pruning Mode                : Disabled

VTP V2 Mode                     : Disabled

VTP Traps Generation            : Disabled

MD5 digest                      : 0x4C 0x22 0xDD 0xCA 0x61 0xA4 0x7C 0x65

Configuration last modified by 0.0.0.0 at 3-1-93 00:04:19

Local updater ID is 0.0.0.0 (no valid interface found)

sw1#

**说明：**现在SW1的VTP模式为Server，域名为ccie，Configuration Revision为 4。

**（3）查看SW1的VLAN信息**

sw1#sh vlan

VLAN Name                             Status    Ports

- --- -------------------------------- --------- -------------------------------

1    default                          active    Fa0/1, Fa0/2, Fa0/3, Fa0/4

Fa0/5, Fa0/6, Fa0/7, Fa0/8

Fa0/9, Fa0/10, Fa0/11, Fa0/12

Fa0/13, Fa0/14, Fa0/15, Fa0/16

Fa0/17, Fa0/18, Fa0/19, Fa0/20

Fa0/21, Fa0/22, Fa0/23, Fa0/24

Gi0/1, Gi0/2

3    VLAN0003                         active

5    VLAN0005                         active

7    VLAN0007                         active

9    VLAN0009                         active

1002 fddi-default                     act/unsup

1003 token-ring-default               act/unsup

1004 fddinet-default                  act/unsup

1005 trnet-default                    act/unsup

（输出被省略）

sw1#

**说明：**SW1上的VLAN为1 3 5 7 9，全部奇数。

**4.配置SW2的VTP**

**（1）在SW2上配置VLAN**

sw2(config)#vlan 2

sw2(config-vlan)#exi

sw2(config)#vlan 4

sw2(config-vlan)#exi

sw2(config)#vlan 6

sw2(config-vlan)#exi

sw2(config)#vlan 8

sw2(config-vlan)#exi

sw2(config)#vlan 10

sw2(config-vlan)#exi

sw2(config)#vlan 12

sw2(config-vlan)#exit

sw2(config)#vtp domain ccie

sw2(config)#vtp mode client

**说明：**SW2上的VLAN为2 4 6 8  10  12 ，全部是偶数，VTP域名为ccie，并且模式为Client。

**（2）查看SW2的VTP信息**

查看VTPsw2#sh vtp status

VTP Version                     : 2

Configuration Revision          : 6

Maximum VLANs supported locally : 1005

Number of existing VLANs        : 11

VTP Operating Mode              : Client

VTP Domain Name                 : ccie

VTP Pruning Mode                : Disabled

VTP V2 Mode                     : Disabled

VTP Traps Generation            : Disabled

MD5 digest                      : 0x5E 0x0C 0x19 0x2B 0xC3 0x13 0x05 0x4F

Configuration last modified by 0.0.0.0 at 3-1-93 00:05:49

sw2#

**说明：**现在SW2的VTP模式为Client，域名为ccie，Configuration Revision为 6。

**（3）查看SW2的VLAN信息**

sw2#sh vlan

VLAN Name                             Status    Ports

- --- -------------------------------- --------- -------------------------------

1    default                          active    Fa0/1, Fa0/2, Fa0/3, Fa0/4

Fa0/5, Fa0/6, Fa0/7, Fa0/8

Fa0/9, Fa0/10, Fa0/11, Fa0/12

Fa0/13, Fa0/14, Fa0/15, Fa0/16

Fa0/17, Fa0/18, Fa0/19, Fa0/20

Fa0/21, Fa0/22, Fa0/23, Fa0/24

Gi0/1, Gi0/2

2    VLAN0002                         active

4    VLAN0004                         active

6    VLAN0006                         active

8    VLAN0008                         active

10   VLAN0010                         active

12   VLAN0012                         active

1002 fddi-default                     act/unsup

1003 token-ring-default               act/unsup

1004 fddinet-default                  act/unsup

1005 trnet-default                    act/unsup

（输出被省略）

sw2#

**说明：**SW2上的VLAN为2 4 6 8  10  12 ，全部是偶数。

**5.验证VTP**

**（1）开启SW1与SW2之间的Trunk链路：**

**SW1：**

sw1(config)#int ran f0/23

sw1(config-if-range)#switchport trunk encapsulation dot1q

sw1(config-if-range)#switchport mode trunk

sw1(config-if-range)#no shut

**SW2：**

sw2(config)#int f0/23

sw2(config-if)#switchport trunk encapsulation dot1q

sw2(config-if)#switchport mode trunk

sw2(config-if)#no shutdown

**说明：**SW1与SW2的Trunk已连通，VTP即将同步。

**（2）查看VTP结果**

**SW1：**

sw1#sh vtp status

VTP Version                     : 2

Configuration Revision          : 6

Maximum VLANs supported locally : 1005

Number of existing VLANs        : 11

VTP Operating Mode              : Server

VTP Domain Name                 : ccie

VTP Pruning Mode                : Disabled

VTP V2 Mode                     : Disabled

VTP Traps Generation            : Disabled

MD5 digest                      : 0x5E 0x0C 0x19 0x2B 0xC3 0x13 0x05 0x4F

Configuration last modified by 0.0.0.0 at 3-1-93 00:05:49

Local updater ID is 0.0.0.0 (no valid interface found)

sw1#

sw1#sh vlan

VLAN Name                             Status    Ports

- --- -------------------------------- --------- -------------------------------

1    default                          active    Fa0/1, Fa0/2, Fa0/3, Fa0/4

Fa0/5, Fa0/6, Fa0/7, Fa0/8

Fa0/9, Fa0/10, Fa0/11, Fa0/12

Fa0/13, Fa0/14, Fa0/15, Fa0/16

Fa0/17, Fa0/18, Fa0/19, Fa0/20

Fa0/21, Fa0/22, Fa0/24, Gi0/1

Gi0/2

2    VLAN0002                         active

4    VLAN0004                         active

6    VLAN0006                         active

8    VLAN0008                         active

10   VLAN0010                         active

12   VLAN0012                         active

1002 fddi-default                     act/unsup

1003 token-ring-default               act/unsup

1004 fddinet-default                  act/unsup

1005 trnet-default                    act/unsup

（输出被省略）

sw1#

**SW2：**

sw2#sh vtp status

VTP Version                     : 2

Configuration Revision          : 6

Maximum VLANs supported locally : 1005

Number of existing VLANs        : 11

VTP Operating Mode              : Client

VTP Domain Name                 : ccie

VTP Pruning Mode                : Disabled

VTP V2 Mode                     : Disabled

VTP Traps Generation            : Disabled

MD5 digest                      : 0x5E 0x0C 0x19 0x2B 0xC3 0x13 0x05 0x4F

Configuration last modified by 0.0.0.0 at 3-1-93 00:05:49

sw2#

sw2#sh vlan

VLAN Name                             Status    Ports

- --- -------------------------------- --------- -------------------------------

1    default                          active    Fa0/1, Fa0/2, Fa0/3, Fa0/4

Fa0/5, Fa0/6, Fa0/7, Fa0/8

Fa0/9, Fa0/10, Fa0/11, Fa0/12

Fa0/13, Fa0/14, Fa0/15, Fa0/16

Fa0/17, Fa0/18, Fa0/19, Fa0/20

Fa0/21, Fa0/22, Fa0/24, Gi0/1

Gi0/2

2    VLAN0002                         active

4    VLAN0004                         active

6    VLAN0006                         active

8    VLAN0008                         active

10   VLAN0010                         active

12   VLAN0012                         active

1002 fddi-default                     act/unsup

1003 token-ring-default               act/unsup

1004 fddinet-default                  act/unsup

1005 trnet-default                    act/unsup

（输出被省略）

sw2#

**说明：**从结果中可以看出，VTP模式为Server的SW1已经将自己的VLAN信息与VTP模式为Client的SW2同步，因为SW1的Configuration Revision为4，而SW2的Configuration Revision为6，所以无论Server与Client，在收到VTP信息后，只要Configuration Revision比自己的大，则将自己的与收到的同步。

**6.验证VTP空域名**

**（1）查看SW3的VTP信息和VLAN信息**

**查看VTP信息：**

sw3#sh vtp sta

VTP Version                     : 2

Configuration Revision          : 0

Maximum VLANs supported locally : 1005

Number of existing VLANs        : 5

VTP Operating Mode              : Server

VTP Domain Name                 :

VTP Pruning Mode                : Disabled

VTP V2 Mode                     : Disabled

VTP Traps Generation            : Disabled

MD5 digest                      : 0x57 0xCD 0x40 0x65 0x63 0x59 0x47 0xBD

Configuration last modified by 0.0.0.0 at 0-0-00 00:00:00

Local updater ID is 0.0.0.0 (no valid interface found)

sw3#

**查看VLAN信息:**

sw3#sh vlan

VLAN Name                             Status    Ports

- --- -------------------------------- --------- -------------------------------

1    default                          active    Fa0/1, Fa0/2, Fa0/3, Fa0/4

Fa0/5, Fa0/6, Fa0/7, Fa0/8

Fa0/9, Fa0/10, Fa0/11, Fa0/12

Fa0/13, Fa0/14, Fa0/15, Fa0/16

Fa0/17, Fa0/18, Fa0/19, Fa0/20

Fa0/21, Fa0/22, Fa0/23, Fa0/24

Gi0/1, Gi0/2

1002 fddi-default                     act/unsup

1003 token-ring-default               act/unsup

1004 fddinet-default                  act/unsup

1005 trnet-default                    act/unsup

（输出被省略）

sw3#

**说明：**可以看到，SW3的VTP域名为空，并且没有手工配置的VLAN。

**（2）开启SW1与SW3之间的Trunk链路：**

**SW1：**

sw1(config)#int f0/19

sw1(config-if)#switchport trunk encapsulation dot1q

sw1(config-if)#switchport mode trunk

sw1(config-if)#no shutdown

**SW2：**

sw3(config)#int f0/19

sw3(config-if)#switchport trunk encapsulation dot1q

sw3(config-if)#switchport mode trunk

sw3(config-if)#no shutdown

**说明：**SW1与SW3的Trunk已连通，VTP即将同步。

**（3）查看SW3的VTP信息：**

sw3#sh vtp status

VTP Version                     : 2

Configuration Revision          : 6

Maximum VLANs supported locally : 1005

Number of existing VLANs        : 11

VTP Operating Mode              : Server

VTP Domain Name                 : ccie

VTP Pruning Mode                : Disabled

VTP V2 Mode                     : Disabled

VTP Traps Generation            : Disabled

MD5 digest                      : 0x5E 0x0C 0x19 0x2B 0xC3 0x13 0x05 0x4F

Configuration last modified by 0.0.0.0 at 3-1-93 00:05:49

Local updater ID is 0.0.0.0 (no valid interface found)

sw3#

**说明：**因为SW3的VTP域名为空，而SW1的VTP域名为ccie，在域名为空的情况下，无论收到任何VLAN信息，只要configuration revision号比自己的大，就会同步自己的VLAN数据库，并且添加上相同的域名，所以空域名的SW3在收到VTP更新之后，同步了自己的信息。所以请谨慎使用空域名交换机。