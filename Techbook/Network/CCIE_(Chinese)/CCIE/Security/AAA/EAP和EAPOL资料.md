# EAP和EAPOL资料

EAP和EAPOL资料

2011年8月2日

21:51

EAP和EAPOL资料

1．EAP协议

802.1x协议在实现整个认证的过程中，其三个关键部分（客户端、认证系统、认证服务器）之间是通过不同的通信协议进行交互的，其中认证系统和认证服务器之间是EAP报文。

EAP帧结构如下表所示：

字段 字节

Code 1

Identifier 2

Length 3-4

Data 5-N

EAP帧格式中各字段含义如下：

字段 占用字节数 描述

Code 1个字节 表示EAP帧四种类型：1．Request；2．Response

3．Success；4．Failure

Identifier 1个字节 用于匹配Request和Response。Identifier的值和系统端口一起单独标识一个认证过程

Length 2个字节 表示EAP帧的总长度

Data 0或更多字节 表示EAP数据

其中Code的取值如下：

1： Request

2： Response

3： Success

4： Failure

2．EAPoL协议

802.1x协议定义了一种报文封装格式，这种报文称为EAPoL（EAP over LANs局域网上的扩展认证协议）报文，主要用于在客户端和认证系统之间传送EAP协议报文，以允许EAP协议报文在LAN上传送。

标准EAPoL帧结构如下表所示：

字段 字节

PAE Ethernet Type

1-2 、Protocol Version

3 、Packet Type

4 、Packet Body Length

5-6 、Packet Body

7-N

EAPoL帧格式中各字段含义如下：

字段 占用字节 描述

PAE Ethernet Type

2个字节 表示协议类型，802.1x分配的协议类型为888E

Protocol Version

1个字节 表示EAPOL 帧的发送方所支持的协议版本号。本规范使用值为0000 0001

Packet Type

1个字节 表示传送的帧类型，如下几种帧类型：

a) EAP-Packet. 值为 0000 0000

b）EAPOL-Start.值为0000 0001

b) EAPOL-Logoff. 值为0000 0010

Packet Body Length

2个字节 表示Packet Body的长度

Packet Body

0/多字节 如果Packet Type为EAP-Packet,取相应值。对于其他帧类型，该值为空。

EAPOL帧在二层传送时，必须要有目标MAC地址，当客户端和认证系统彼此之间不知道发送的目标时，其目标MAC地址使用由802.1x协议分配的组播地址01-80-c2-00-00-03。