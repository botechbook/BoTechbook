# 基于802.1x的动态VLAN

基于802.1x的动态VLAN

2011年8月2日

21:53

基于802.1x的动态VLAN

IEEE 802.1x名为基于端口的访问控制协议（Port based network access control protocol），它源于IEEE 802.11无线以太网（EAPOW）。该协议的认证体系结构中采用了“可控端口”和“不可控端口”的逻辑功能，从而可以实现认证与业务的分离，保证了网络传输的效率。用户通过认证后，业务流和认证流分开，对后续的数据包处理没有特殊要求。 本节讲述如何在Catalyst系列交换机上使用802.1x实现动态VLAN技术，拓扑图如下

![%E5%9F%BA%E4%BA%8E802%201x%E7%9A%84%E5%8A%A8%E6%80%81VLAN%20c82709aef14641e4b71399111dbb2125/image1.png](基于802%201x的动态VLAN/image1.png)

第一步，在交换机上启动AAA，配置认证和授权

switch(config)# aaa new-mode

switch(config)# aaa authentication dot1x default group radius

switch(config)# aaa authorization network default group radius //配置认证和授权方法

第二步，配置AAA服务器参数。

switch(config)# radius-server host 10.10.20.60 key cisco

switch(config)# radius-server vsa send //由于需要做动态VLAN分配，因此必须让交换机识别radius服务器发送的VSA值

第三步，启动802.1x。

switch(config)# dot1x system-auth-control //全局开启802.1x

switch(config)# interface range fa0/1 – 20

switch(config-if-range)# switchport mode access

switch(config-if-range)# spanning-tree portfast

switch(config-if-range)# dot1x port-control auto //在端口上开启802.1x

第四步，配置Radius服务器。

1、在ACS导航条中点击“Network Configuration”将交换机添加为AAA client，认证协议使用“Radius（IETF）”，如下图所示：

![%E5%9F%BA%E4%BA%8E802%201x%E7%9A%84%E5%8A%A8%E6%80%81VLAN%20c82709aef14641e4b71399111dbb2125/image2.png](基于802%201x的动态VLAN/image2.png)

2、在ACS导航条中点击“Interface Configuration”，点击“Radius（IETF）”进入以下界面

![%E5%9F%BA%E4%BA%8E802%201x%E7%9A%84%E5%8A%A8%E6%80%81VLAN%20c82709aef14641e4b71399111dbb2125/image3.png](基于802%201x的动态VLAN/image3.png)

选中“[064] Tunnel-Type”、“[065] Tunnel-Medium-Type”、“[081] Tunnel-Private-Group-ID”复选框，点击“submit”。

3、在ACS导航条中点击“User Setup”添加用户并且分配到相应的组中。

4、在ACS导航条中点击“Group Setup”编辑组设置，将“[064] Tunnel-Type”标签1的值设置为“VLAN”，将“[065] Tunnel-Medium-Type” 标签1的值设置为“802”，将“[081] Tunnel-Private-Group-ID” 标签1的值设置为该组用户所对应的VLAN ID。如下图所示：

![%E5%9F%BA%E4%BA%8E802%201x%E7%9A%84%E5%8A%A8%E6%80%81VLAN%20c82709aef14641e4b71399111dbb2125/image4.png](基于802%201x的动态VLAN/image4.png)