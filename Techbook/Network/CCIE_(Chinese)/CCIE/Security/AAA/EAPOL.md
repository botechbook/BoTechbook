# EAPOL

EAPOL

2011年8月2日

21:49

EAP是Extensible Authentication Protocolover的缩写，**EAPOL就是(EAP OVER LAN )基于局域网的扩展认证协议。**

EAPOL是基于802.1X网络访问认证技术发展而来的。

802.1X 的实现设计**三个部分，**请求者系统、认证系统和认证服务器系统。因此EAPOL也是。

当认证系统工作于中继方式时，认证系统与认证服务器之间也运行EAP协议，EAP帧中封装认证数据，将该协议承载在其它高层次协议中(如 RADIUS)，以便穿越复杂的网络到达认证服务器;当认证系统工作于终结方式时，认证系统终结EAPoL消息，并转换为其它认证协议(如 RADIUS)，传递用户认证信息给认证服务器系统。

认证系统每个物理端口内部包含有受控端口和非受控端口。非受控端口始终处于双向连通状态，主要用来传递EAPoL协议帧，可随时保证接收认证请求者发出的EAPoL认证报文;受控端口只有在认证通过的状态下才打开，用于传递网络资源和服务。

整个802.1X的认证过程可以描述如下

(1) 客户端向接入设备发送一-个EAPoLStart报文，开始802.1X认证接入;

(2) 接入设备向客户端发送EAP-Request/Identity报文，要求客户端将用户名送上来;

(3) 客户端回应一个EAP-Response/Identity给接入设备的请求，其中包括用户名;

(4) 接入设备将EAP-Response/Identity报文封装到RADIUS Access-Request报文中，发送给认证服务器;

(5) 认证服务器产生一个Challenge，通过接入设备将RADIUS Access-Challenge报文发送给客户端，其中包含有EAP-Request/MD5-Challenge;

(6) 接入设备通过EAP-Request/MD5-Challenge发送给客户端，要求客户端进行认证

(7) 客户端收到EAP-Request/MD5-Challenge报文后，将密码和Challenge做MD5算法后的Challenged-Pass-word，在EAP-Response/MD5-Challenge回应给接入设备

(8) 接入设备将Challenge，Challenged Password和用户名一起送到RADIUS服务器，由RADIUS服务器进行认证

(9)RADIUS服务器根据用户信息，做MD5算法，判断用户是否合法，然后回应认证成功/失败报文到接入设备。如果成功，携带协商参数，以及用户的相关业务属性给用户授权。如果认证失败，则流程到此结束;

(10) 如果认证通过，用户通过标准的DHCP协议 (可以是DHCP Relay) ，通过接入设备获取规划的IP地址;

(11) 如果认证通过，接入设备发起计费开始请求给RADIUS用户认证服务器;

(12)RADIUS用户认证服务器回应计费开始请求报文。用户上线完毕