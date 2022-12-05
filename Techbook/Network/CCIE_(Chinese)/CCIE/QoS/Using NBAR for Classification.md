# Using NBAR for Classification

Using NBAR for Classification

2011年7月7日

15:35

**NBAR：Network Based Application Recognition 基于网络的应用程序识别**

**NBAR是思科私有的**

**NBAR可以完成3项工作：**

**1.协议的发现（从4层到7层都可以识别）**

**2.流量统计**

**3.流量分类**

**由于NBAR可以发现网络中运行了哪些应用和哪些协议，并能提供数量和统计信息，所以可以使用NBAR作为一个强大易用的工具来定义网络的流量类别。**

**此外也可以在MQC中应用NBAR，以便为标记、监管和排队等机制提供数据包分类功能。**

**NBAR可以根据URL来区分HTTP流量，也可以根据MIME类型来区分HTTP流量。**

**MIME类型就是设定某种扩展名的文件用一种应用程序来打开的方式类型，当该扩展名文件被访问的时候，浏览器会自动使用指定应用程序来打开。多用于指定一些客户端自定义的文件名，以及一些媒体文件打开方式。**

**下面列出常用的文件对应的MIME类型：**

**Mime-Types(mime类型) Dateiendung(扩展名) Bedeutung**

**application/msexcel *.xls *.xla Microsoft Excel Dateien**

**application/mshelp *.hlp *.chm Microsoft Windows Hilfe Dateien**

**application/mspowerpoint *.ppt *.ppz *.pps *.pot Microsoft Powerpoint Dateien**

**application/msword *.doc *.dot Microsoft Word Dateien**

**application/octet-stream**

- **.exe exe**

**application/pdf *.pdf Adobe PDF-Dateien**

**application/post****** *.ai *.eps *.ps Adobe Post******-Dateien**

**application/rtf *.rtf Microsoft RTF-Dateien**

**application/x-httpd-php *.php *.phtml PHP-Dateien**

**application/x-java****** *.js serverseitige Java******-Dateien**

**application/x-shockwave-flash *.swf *.cab Flash Shockwave-Dateien**

**application/zip *.zip ZIP-Archivdateien**

**audio/basic *.au *.snd Sound-Dateien**

**audio/mpeg *.mp3 MPEG-Dateien**

**audio/x-midi *.mid *.midi MIDI-Dateien**

**audio/x-mpeg *.mp2 MPEG-Dateien**

**audio/x-wav *.wav Wav-Dateien**

**image/gif *.gif GIF-Dateien**

**image/jpeg *.jpeg *.jpg *.jpe JPEG-Dateien**

**image/x-windowdump *.xwd X-Windows Dump**

**text/css *.css CSS Stylesheet-Dateien**

**text/html *.htm *.html *.shtml -Dateien**

**text/java****** *.js Java******-Dateien**

**text/plain *.txt reine Textdateien**

**video/mpeg *.mpeg *.mpg *.mpe MPEG-Dateien**

**video/vnd.rn-realvideo *.rmvb realplay-Dateien**

**video/quicktime *.qt *.mov Quicktime-Dateien**

**video/vnd.vivo *viv *.vivo Vivo-Dateien**

**NBAR的一些限制：**

**1.NBAR不支持Fast EtherChannel（快速以太通道）逻辑接口**

**2.NBAR最多只能同时处理24个URL、主机或者MIME类型**

**3.NBAR只能分析数据包的前400个字节**

**4.NBAR需要CEF的支持 -----这点要切记**

**5.NBAR不支持组播包，分段包和SHTTP**

**NBAR能够识别的一些协议如下：**

![Using%20NBAR%20for%20Classification%2051c502e55c7f426382ecf87085ddbc63/image1.png](Using%20NBAR%20for%20Classification/image1.png)

**TCP和UDP静态端口协议**

**TCP和UDP状态化协议：指在发起控制会话的过程中协商数据会话的端口**

**非TCP和非UDP的协议**

**虽然NBAR只能识别部分协议，但可以通过将思科发布的新的PDLM加载到设备闪存中比在设备配置中引用该PDLM，就可以扩展NBAR所能识别的协议列表。**

**关于PDLM**

**PDLM ：Packet Description Language Modules ，包描述语言模块**

**PDLM是有思科发布的一系列文件，该文件中包含了NBAR用来识别协议和应用的一些规则，新的PDLM只需要加载到flash，并在设备配置中加以引用即可，不需要执行IOS升级或者重载（Reload）。**

**思科在CCO（Cisco Connection Online , 思科在线连接）上为注册用户提供了最新的PDLM（[www.cisco.com/cgi-bin/tablebuild.pl/pdlm](http://www.cisco.com/cgi-bin/tablebuild.pl/pdlm)）**

**利用PDLM可以扩展NBAR所能识别的协议列表**

**添加PDLM的命令是：**

**Router（config）# ip nbar pdlm *pdlm-name***

**pdlm-name可以有两种形式：**

**1.如果PDLM在flash中，使用flash://citrix.pdlm**

**2.如果PDLM在TFTP服务器上，使用tftp://192.168.1.3/citrix.pdlm**

**案例一：假设路由器中的NBAR不支持eDonkey，使用tftp将eDonkey.pdlm加载到路由器中**

**方法：可以使用两种方法，一种是直接将eDonkey.pdlm使用ip nbar pdlm tftp://10.1.1.3/eDonkey.pdlm加载到路由器中，一种是用copy tftp://10.1.1.3/eDonkey.pdlm flash:复制到路由器的flash中，然后使用命令ip nbar pdlm flash://eDonkey.pdlm加载到路由器中**

**补充：禁用电驴**

**关键配置：**

**ip cef**

**ip nbar pdlm flash://eDonkey.pdlm**

**class-map eDonkey**

**match protocol eDonkey**

**policy-map PM**

**class eDonkey**

**drop**

**interface s1/0**

**ip nbar protocol-discovery**

**service-policy input PM**

**注意点：**

**[www.baidu.com/admin/admin.aspx](http://www.baidu.com/admin/admin.aspx)**

**wwww.baidu.com 是host**

**admin/admin.aspx 是url**

**修改协议名所对应的端口号或者新添加一个端口号的命令是：**

**Router（config）# ip nbar port-map protocol-name [tcp|udp] port-number**

**该命令要求NBAR使用上述端口号来查找该协议或协议名。最多可以额外指定16个端口号**

**如果想查看NBAR协议与端口的对应关系，可以使用命令：show ip nbar port-map [protocol-name]**

**在接口下启用NBAR的命令是：**

**Router（config-if）# ip nbar protocol-discovery**

**要显示被发现的协议和每种被发现协议的统计信息，可以是用命令：show ip nbar protocol-discovery**

**NBAR除了可以识别和分类那些使用静态端口的协议之外，还可以识别和分类那些使用动态协商端口号的协议。**

**NBAR可以应用到MQC中，使用命令：**

**Router（config-cmap）# match protocol *protocol-name***

**其中protocol-name是协议的名字，如果想扩展NBAR所支持的协议列表，可以在设备上加载新的PDLM**

**案例二：**

**需求：对于从R1向R3方向的HTTP流量设置带宽512Kbps，并且HTTP服务器开设的端口除了80以外，有可能还会开设8080**

**拓扑图：**

![Using%20NBAR%20for%20Classification%2051c502e55c7f426382ecf87085ddbc63/image2.jpg](Using%20NBAR%20for%20Classification/image2.jpg)

**关键配置：**

**ip cef**

**class-map WWW**

**match protocol http**

**policy-map PM**

**class WWW**

**bandwidth 512**

**interface s1/1**

**ip nbar protocol-discovery**

**service-policy output PM**

**ip nbar port-map http tcp 80 8080**

**NBAR最有吸引力的一个功能就是深度包检测功能，利用NBAR的深度包检测功能可以完成一下常见任务：**

**1.基于主机名或HTTP GET,post,request请求中主机名后面的URL进行流量分类**

**命令：**

**Router（config-cmap）# match protocol http url *url-string***

**Router（config-cmap）# match protocol http host *host-name***

**2.基于MIME类型进行流量分类**

**命令：**

**Router（config-cmap）# match protocol http mime *mime-type***

**3.使用正则表达式对快速跟踪（fast-track）文件传送协议的流量进行分类**

**命令：**

**Router（config-cmap）# match protocol fasttrack file-transfer *regular-expression***

**//"regular-expression"**

**Regular expression used to identify specific FastTrack traffic. For instance, entering "cisco" as the regular expression would classify the FastTrack traffic containing the string "cisco" as matches for the traffic policy.**

**To specify that all FastTrack traffic be identified by the traffic class, use "*" as the regular expression.**

**4.基于RTP净荷类型或CODEC进行流量分类**

**命令：**

**Router（config-cmap）# match protocol rtp [audio|video|payload-type payload-type-string]**

**//实时传送协议（Real-time Transport Protocol或简写RTP，也可以写成RTTP）是一个网络传输协议，它是由IETF的多媒体传输工作小组1996年在RFC 1889中公布的。 　　RTP协议详细说明了在互联网上传递音频和视频的标准数据包格式。它一开始被设计为一个多播协议，但后来被用在很多单播应用中。RTP协议常用于流媒体系统（配合RTCP协议），视频会议和一键通（Push to Talk）系统（配合H.323或SIP），使它成为IP电话产业的技术基础。RTP协议和RTP控制协议RTCP一起使用，而且它是建立在用户数据报协议上的。**

**案例三：使用NBAR匹配HTTP主机名、URL和MIME类型**

**需求：**

**1.使用class-map A匹配主机名以cisco开头的主机的HTTP GET请求**

**2.使用class-map B匹配URL中含有“/admin/login”的HTTP请求**

**3.使用class-map C匹配HTTP中包含mp3或者mp4的请求**

**配置：**

**class-map A**

**match protocol http host cisco***

**class-map B**

**match protocol http url admin/login***

**class-map match-any C**

**match protocol http mime “*.mp3”**

**match protocol http mime “*.mp4”**

**关于正则表达式**

- **在该位置匹配零个或多个字符**

**？ 在该位置上匹配任一个字符**

**| 表示OR，匹配符号任一边的字符选项**

**（|） 匹配小括号|任一边的字符选项，如xyz.(gif|jpg)意思是匹配xyz.gif或xyz.jpg**

- [ ]  **匹配指定区间的任何字符或某个特定字符，如[0-9]表示匹配其中的一个数字**

**默认情况下，一个接口的可用带宽实际只为接口总带宽的75%， 剩下的25%保留给一些管理协议使用**

**接口下配置WFQ或者用service-policy调用一个Policy-map才能看出可用带宽Available Bandwidth**

**使用命令show interface 可以查看**

**R1(config-if)#max-reserved-bandwidth 百分比**

**这条命令可以改变可利用带宽值**

**案例四：**

**拓扑图：**

![Using%20NBAR%20for%20Classification%2051c502e55c7f426382ecf87085ddbc63/image3.jpg](Using%20NBAR%20for%20Classification/image3.jpg)

**需求：**

**对于R2，从S1/0接口进来的流量**

**如果是使用RTP协议的音频流量设置DSCP值为EF**

**如果是使用RTP协议的视频流量设置DSCP值为AF41**

**如果是使用citrix协议的流量设置DSCP值为AF31**

**从S1/1接口出去的流量**

**对于DSCP值为EF的流量优先传输，且设置带宽占总带宽的10%**

**对于DSCP值为AF41的流量设置带宽为剩余带宽的20%**

**对于DSCP值为AF31的流量设置带宽为剩余带宽的30%**

**其余流量尽量占用带宽**

**关键配置：**

**class-map RTP-VOICE-IN**

**match protocol rtp radio**

**class-map RTP-VEDIO-IN**

**match protocol rtp vedio**

**class-map CITRIX-IN**

**match protocol citrix**

**policy-map PM-MARK**

**class RTP-VOICE-IN**

**set ip dscp ef**

**class RTP-VEDIO-IN**

**set ip dscp af41**

**class CITRIX-IN**

**set ip dscp af31**

**int S1/0**

**ser in PM-MARK**

**....略**

**class-map EF**

**match dscp ef**

**class-map AF41**

**match dscp af41**

**class-map AF31**

**match dscp af31**

**policy-map PM-MARK2**

**class EF**

**bandwidth percent 10**

**class AF41**

**bandwidth remaining 20**

**class AF31**

**bandwidth remaining 30**

**class class-default**

**fair-queue 其余流量尽量占用带宽**

**int s1/1**

**ser out PM-MARK2**