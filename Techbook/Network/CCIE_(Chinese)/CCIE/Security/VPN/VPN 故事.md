# VPN 故事

VPN

2011年8月2日

21:55

> 小故事
> 
> 
> 1、我们还没有参加CCNP的考试
> 
> 2、现在我们实验室有这么一套包过的题库
> 
> 3、如果我能拿到这套题库肯定能过
> 
> 4、但是，我现在已经在外地了，不在实验室，咋办呢？
> 
> 5、怎样才能把这个题库顺利的交到我的手上呢？
> 
> 6、而且我会怀疑有人窃取我的版本
> 
> 7、我也怕这个题库被别人拿到，我就不好办了
> 
> 安全的含义
> 
> 1、我需要确保这个版本是来自我们实验室的
> 
> 2、我能确保这个版本在传输的过程中，没有被修改过
> 
> 3、我也要确保，没有别人看过这个版本，因为这个版本是为我专门定做的
> 
> 4、我们实验室也不能事后否认曾经发给我这么一个版本
> 
> <安全的含义>
> 
- 保证来源性 <===对源进行认证
- 保证完整性 <===在传输过程中,不允许对数据包进行修改
- 保证私密性 <===对数据包进行加密,又称为:数据的机密性.
- 不可否认性 <===不允许发送方抵赖,说自己没有传过

> 
> 
> 
> 角色
> 
> internet网 黑客 明文版本 密文版本
> 
> 对称密码学
> 
> 1、**密码学算法主要分为两个大类，对称密码学和非对称密码**学，对称密码学技术已经存在了很长的时候，最早使用对称密码技术的是埃及人
> 
> 2、我们很快就能看到，对称算法和非对称算法各有所长和弱点，所以现代密码系统都在努力做到适当的使用这两类算法以利用它们的长处，同时又避免它们各自的缺点
> 
> 对称的加密和解密案例
> 
> 文件----钥匙---密文 密文---同一把钥匙------文件
> 
> 等同于开门锁门的钥匙
> 
> 对一个文件加密密码为123456，那么解密的时候也使用123456
> 
> 感觉很完美
> 
> CCNP这个题库----密钥123456---密文----经过互联网传输给我-----我在通过123456来解密----正常的收到这个版本了
> 
> 存在的问题
> 
> 1、surpasslab怎么把123456这个密钥给我呢？
> 
> 2、也是通过互联网传输吗？
> 
> 3、要不我直接开飞机过去拿吧
> 
> 这就出现了一个密钥分发的问题
> 
> 实际情况可能更糟
> 
> 1、重复使用同一个对称密钥是不合理的
> 
> 2、 如果同学之间彼此要交换题目呢？如果是孙老要把题目交给你们每一个人肯定要使用不同的密码
> 
> 3、如果有5个人【5*（5-1）】，如果人员很多呢
> 
> 4、密钥使用一次后就要删除
> 
> 5、存在的这些缺点，密钥的分发，密钥的存储，密钥的管理以及缺乏数字签证的支持，这些都是对称密码算法的缺点
> 
> 6、所以到现在我们还没有解决这个题目传输的问题
> 
> 对称密码学总结
> 
> 1、在对称密码学中，同一个密钥既用于加密也用于解密
> 
> 2、对称加密速度快（相对的）
> 
> 3、对称加密是安全的
> 
> 4、对称加密得到的密文是紧凑的（加密前后的文件大小差不多）
> 
> 5、因为接受者需要得到对称密钥，所以对称加密容易受到中途拦截，窃听的攻击
> 
> 6、对称密码系统当中密钥的个数大约是以参与者数目的平方的速度增长，因此很难将它的使用扩大的大范围的人群中
> 
> 7、对称密码系统需要复杂的密钥管理
> 
> 8、对称密码技术不适用与数字签名和不可否认性
> 
> 算法:DES/3DES/AES/RC(2,4,5,6)
> 
> DES，3DES都是vpn用的，AES是比较新的,RC是pc用的，前三个硬件，后一个软件
> 
> 非对称密码加密
> 
> 算法：RSA
> 
> 公钥和私钥
> 
> 用公钥加密，用私钥解密；或者用私钥加密，用公钥解密
> 
> 现在再来传输版本
> 
> 明文版本---公钥----密文---internet---密文--私钥---明文
> 
> 出现的问题
> 
> 现在有个假冒的人拿着我的公钥来加密一个版本给我，所以我必须要通过某种方式来确认这个版本是来自surpasslab的
> 
> 非对称密码学的好处和缺点
> 
> 1、使用非对称密码技术时，用一个密钥加密的东西只能用另一个密钥来解密
> 
> 2、非对称加密是安全的
> 
> 3、因为不必发送密钥给接受者，所以非对称加密不必担心密钥被中途截获
> 
> 4、需要分发的密钥数目和参与者的数目一样
> 
> 5、非对称密码技术没有复杂的密钥分发问题
> 
> 6、非对称密码技术不需要事先在各参与者之间建立关系以及交换密钥
> 
> 7、非对称密码技术支持数字签名和不可否认性
> 
> 8、非对称加密速度相对较慢
> 
> 9、非对称加密会造成密文较长
> 
> 用公钥加密，用私钥解密，这种技术叫做加密
> 
> 用私钥加密，用公钥解密，这种技术叫做签名
> 
> 通过比较会发现对称密钥更适合加密大文件的东西
> 
> 理想的解决方案
> 
> 1、该解决方案必须是安全的
> 
> 2、加密的速度必须快
> 
> 3、加密得到的密文必须紧凑
> 
> 4、该解决方案必须能够适应参与者数目很多的情况
> 
> 5、该解决方案必须能够抗密钥窃听攻击
> 
> 6、该解决方案一定不能要求事先在参与者 建立某种关系
> 
> 7、该方案必须要支持数字签名和不可否认性
> 
> 现在又提出了一个更合理的方案
> 
> 明文文件--对称加密--然后把密钥用公钥加密--一块发过去
> 
> 对端收到两个东西，一个是经过对称加密的密文，一个是用公钥加密的对称密钥
> 
> 散列函数
> 
> 1、散列算法接收一大块的数据并将其压缩成最初数据的一个指纹或者摘要
> 
> 2、散列函数的输出是一个比最初数据小的值，如果你修改了最初的数据，哪怕只修改了一位，那么输出的散列值就会不同
> 
> **3、你无法反向执行散列算法来恢复出哪怕是一点最初的明文**
> 
> 4、得到摘要不会告诉你任何关于最初明文的信息
> 
> 5、创建和发现散列值为某个特定的明文，这在计算上是不可行的
> 
> MD5（128） SHA（160）
> 
> **不同输入，不同输出**
> 
> **不定长输入，定长输出**
> 
> 数字签名
> 
> 文件-----------------加密文件----
> 
> - 摘要
> - hash -
> - 私钥 -
> 
> 摘要----------------加密的摘要
> 
> 接受者收到文件之后，先把文件解密，然后再利用hash算出摘要
> 
> 再把加密过的摘要解密出来，然后对比两个摘要的大小
> 
> 验证签名过程中的逻辑推理
> 
> 1、我在目录中查找到了surpasslab的公钥
> 
> 2、我用这个公钥对加密摘要进行解密
> 
> 3、surpasslab拥有该私钥仅存的唯一拷贝
> 
> 4、因此，如果解密得到的摘要和摘要相匹配，那么这个版本就是来自surpasslab
> 
> 但是如果黑客替换了在目录中的公钥呢？
> 
> ![VPN%20%E6%95%85%E4%BA%8B%20d9e87ad760724bf3a2a3bf83c1572887/image1.png](VPN%20故事/image1.png)
> 
> 数字证书
> 
> ![VPN%20%E6%95%85%E4%BA%8B%20d9e87ad760724bf3a2a3bf83c1572887/image2.png](VPN%20故事/image2.png)
> 
> 现在不在基于一个算法进行加密，**算法是公开的，但是密钥不公开**。想一想为什么？？？
> 
> 加密的一个层次
> 
> 1、应用层加密：SQL，oracle，应用层加密的一个作用？？？QQ
> 
> 2、会话层加密：ssh //telnet呢？
> 
> 3、网络层加密：ipsec，ip包头是明文的，后面是密文，也就是说从三层 加密
> 
> 4、数据链路层加密：加密机，硬件加密。比较老的技术了，用纸袋凿孔，来表示0还是1
> 
> 5、物理层加密。 //把硬盘放在保险柜里，然后运出去
> 
> 理想的算法所要达到的要求
> 
> 1、能抵御密钥的攻击 //防止一些弱口令的出现
> 
> 2、需要变长的密钥长度
> 
> 3、雪崩效应
> 
> 4、不受进出口限制的 //必须要经过安全局审批
> 
> 最常见的技术包括块加密，流加密和消息认证
> 
> ![VPN%20%E6%95%85%E4%BA%8B%20d9e87ad760724bf3a2a3bf83c1572887/image3.png](VPN%20故事/image3.png)
> 
> ![VPN%20%E6%95%85%E4%BA%8B%20d9e87ad760724bf3a2a3bf83c1572887/image4.png](VPN%20故事/image4.png)
> 
> 对称加密
> 
> 1、加密速度快
> 
> 2、算法简单，容易硬件加速
> 
> 3、密钥管理是个很大的问题
> 
> 非对称加密算法
> 
> 1、其中最著名的是公私钥系统
> 
> 2、通常的密钥长度为512-2048比特（比不上对称算法） //路由做RSA 512，防火墙1024,2048现在还没有用
> 
> 3、RSA和椭圆曲线
> 
> 对称算法与非对称算法不能直接进行比较
> 
> 非对称 加密问题
> 
> 1、加密速度比对称算法慢
> 
> 2、硬件计算量大
> 
> 3、密钥管理方便
> 
> 4、用于小型服务（签名，密钥交换）
> 
> 常见的块加密包括DES，AES，IDEA，SAFER
> 
> 流加密包括：DES，3DES，RC4，SEAL
> 
> DES
> 
> 数据加密算法是一种**对称加密算法**，很可能是使用最广泛的密钥系统，特别是在保护金融数据的安全中，最初开发的DES是嵌入硬件中的。通常，自动取款机（Automated Teller Machine，ATM）都使用DES。它出自IBM的研究工作1975，IBM也曾对它拥有几年的专利权，但是在1983年已到期后，处于公有范围中，允许在特定条件下可以免除专利使用费而使用。1977年被美国政府正式采纳。
> 
> 加密算法很成熟（除了暴力破解，没有别的方法），但是密钥长度不够，容易被暴力破解
> 
> 加密原理
> 
> DES 使用一个 56 位的密钥以及附加的 8 位奇偶校验位，产生最大 64 位的分组大小。这是一个迭代的分组密码，使用称为 Feistel 的技术，其中将加密的文本块分成两半。使用子密钥对其中一半应用循环功能，然后将输出与另一半进行“异或”运算；接着交换这两半，这一过程会继续下去，但最后一个循环不交换。DES 使用 16 个循环，使用异或，置换，代换，移位操作四种基本运算。 数据加密算法
> 
> 加密历史和技术
> 
> 1、加密历史
> 
> 凯撒大帝密码
> 
> 风语者（原始的也许是最好的） //种族语言
> 
> **解密：最好的方法是从密钥管理和密钥分发中寻找机会点，而不是从算法本身寻找脆弱点**
> 
> 因此，一个密码系统的成功与否的关键是密钥的生成，分发，管理
> 
> 2、加密技术
> 
> 现代的基本加密技术要依赖于消息之目标接收者已知的一项秘密。通常，解密方法（亦即“算法”）是任何都知道的-就象所有人都知道怎样打开门一样。然而，真正用来解开这一秘密的“密钥（key）”却并非尽人皆知-就象钥匙一样，一扇门的钥匙并不是任何人都拿得到的，因此，关键的问题是如何保障密钥的安全
> 
> 当然，还有某些加密系统建立在一种密保的算法基础上--通常把它叫做“隐匿保密”
> 
> 不存在“绝对安全”
> 
> 加密方法的“健壮度”是由其复杂程度来决定的。例如，假设某种特定的加密系统复杂程度是2的32次方，我们便认为为了破解它，需进行2的32次方次独立运算。这个数量表面上似乎非常大，但对一部高速计算机来说，它每秒钟也许就能执行数百乃至上千次这样的解密运算，所以对这种加密系统来说，其能力尚不足以保证秘密的安全。正是考虑到这样的情况，**所以我们用“计算安全”来衡量一个现代加密系统的安全程度**
> 
> 加密基础
> 
> 公共密钥加密系统，建立在“单向函数和活门”的基础上。
> 
> “单向函数”是指一个函数很容易朝一个方向计算，但很难（甚至不可能）逆向回溯；2*3=6
> 
> “活门”是指一种可供回溯的“小道”
> 
> ![VPN%20%E6%95%85%E4%BA%8B%20d9e87ad760724bf3a2a3bf83c1572887/image5.png](VPN%20故事/image5.png)
> 
> **1、因式分解问题：z=x*y**
> 
> 一个有限的范围内，很容易计算出数字的乘积，但却很难分解出生成那个乘积的各个乘数RSA
> 
> **2、离散对数问题**：一个大质数p，以及一个底数g。已知一个特定的值y，求指数x，如下所示：g^x=y mod p
> 
> 其中，mod是“求余”的意思，模指数很容易便可计算出来，但假设若想通过一次离散对数运算恢复原来的指数，却是异常难的。
> 
> **4、单向散列函数**
> 
> 定义：散列函数采用一条长度可变的消息作为自己的输入，对其进行压缩，再 一个长度固定的摘要。**一致的输入会产生一致的输出**
> 
> 特点：collosion free，雪崩效应
> 
> 作用：身份验证，完整性校验
> 
> 具体函数：MD5（message digest 5，消息摘要5），SHA-1（secure hash |gorithm，安全散列算法），ripemd
> 
> **5、异或（XOR）函数** //经过两次异或即可还原
> 
> 0101
> 
> 0110
> 
> - ----
> 
> 0011
> 
> 对称加密算法
> 
> **对数据输入处理方式：“块”的方式，“流”的方式**
> 
> **无论块加密还是流加密，加密速度快，数据长度几乎不增加，所以特别适用于批量加密，但是密钥分发和管理困难**。
> 
> 工作模式：
> 
> 1、电子密码本（ECB）
> 
> 2、加密块连接（CBC）
> 
> IPsec适用“块”加密，CBC。
> 
> ![VPN%20%E6%95%85%E4%BA%8B%20d9e87ad760724bf3a2a3bf83c1572887/image6.png](VPN%20故事/image6.png)
> 
> 3、加密回馈模式（cipher feedback mode，CFB）
> 
> 4、输出回馈模式（output feedback mode，OFB）
> 
> 1,2是块加密的，3,4是流加密的
> 
> 非对称加密算法
> 
> 通俗的名称叫做“公共密钥算法”，其中要用到两个密钥，一个是公共的，一个是私人的，一个密钥负责加密（编码），另一个负责解密（译码），建立在单向函数基础上。
> 
> 1、RSA 目前最流行的公共密钥算法就是RSA，名字来源于它的发明者：Ron Rivest，Adi Shmir以及Leonard Adleman。RSA之所以能够保密，关键在于假如已知两个非常大的质数的乘积，那么很难解析出到底是哪两个质数相乘的结果（因数分解）。RSA的重要特点是其中一个密钥可用来加密数据，另一个密钥可用来解密。这意味着任何人都能用你的公共密钥对一条消息进行加密，而只有你才能对它进行解密。另外，你也可用自己的私人密钥对任何东西进行加密，而拿到你的公共密钥的任何人都能对其解密
> 
> **缺点：是速度非常慢，而且能处理的数据最多只能有它的密钥的模数大小**
> 
> **应用：是密钥交换和数字签名的事实标准**
> 
> **身份验证和完整性**
> 
> 为保守一个秘密，它的机密性是首先必须保证的，但假如不进行身份验证，也没有办法知道要同你分享秘密的人是不是他所声称的那个人。同时假如不能验证接收到的一条消息的完整性，也无法知道它是否确为实际发出的那条消息
> 
> 对每个数据的身份验证和完整性保证
> 
> 1、密钥化的单向散列函数
> 
> 2、数字签名（缺点是非常慢）
> 
> **对数据交换前的身份验证：数据证书+数字签名。。。。**
> 
> **数字签名特点**
> 
> 1、难以伪造：只有私人密钥的持有者才能生产签名
> 
> 2、无法抵赖：由于极难伪造，所以对于一份经过签名的文档来说，签署人很难抵赖这不是自己的“手迹”
> 
> 3、不可更改：一经签名，文档便不能修改
> 
> 4、不能转移：签名不能移走，并加入另一个不相干的文档
> 
> ![VPN%20%E6%95%85%E4%BA%8B%20d9e87ad760724bf3a2a3bf83c1572887/image7.png](VPN%20故事/image7.png)
> 
> ![VPN%20%E6%95%85%E4%BA%8B%20d9e87ad760724bf3a2a3bf83c1572887/image8.png](VPN%20故事/image8.png)
> 
> RSA签名
> 
> **单纯的数字签名不能完成身份验证，必须和数字证书相结合**
> 
> ![VPN%20%E6%95%85%E4%BA%8B%20d9e87ad760724bf3a2a3bf83c1572887/image9.png](VPN%20故事/image9.png)
> 
> DSA签名
> 
> DSA（数字签名算法）和RSA类似，即可用来加密，亦可用来签名
> 
> **数学基础：建立在“离散对数问题”的基础上**
> 
> DSA实际并不对生产的签名进行加密处理，也不对签名的验证进行解密处理（尽管它实际上有一个公共密钥和一个私人密钥），相反，私人密钥用来生成两个160位的值，该值代表着签名，而签名的验证是一种数学上的求证（用公共密钥进行），证明那两个值只能由私人密钥生成
> 
> **DSA将SHA作为一种散列函数应用于签名**
> 
> 密钥交换（1）
> 
> **DH密钥交换式**第一种公共密钥加密系统，DH密钥交换**建立在“离散对数问题”的基础上**
> 
> DH交换过程中涉及到的所有参与者首先都必须隶属于一个组，这个组定义了要使用哪个质数p，以及底数g。DH密钥交换是一个两部分的过程，在每一端（Alice和Bob）的第一部分，需要选择一个随机的私人数字（由当事人的小写字母表示），并在组内进行乘幂运算，产生一个公共值（当事人的大写字母）
> 
> ![VPN%20%E6%95%85%E4%BA%8B%20d9e87ad760724bf3a2a3bf83c1572887/image10.jpg](VPN%20故事/image10.jpg)
> 
> 开始交换自己的公共密钥，Alice讲A给Bob，Bob将B给Alice，他们再次执行乘幂运算，使用当事人的公共值作为底数，以生成共享的一个“秘密”
> 
> ![VPN%20%E6%95%85%E4%BA%8B%20d9e87ad760724bf3a2a3bf83c1572887/image11.jpg](VPN%20故事/image11.jpg)
> 
> 密钥交换（2）
> 
> DH密钥交换的一个缺点是容易受到“中间人”的攻击
> 
> 解决方法：中间人攻击并不足以证明DH的脆弱，只要Alice和Bob为自己的公共值加上了数字签名，便能有效的防范此类攻击
> 
> 完美向前保密
> 
> 短暂的一次性密钥的系统成为“完美向前保密”（PFS）
> 
> 如果加密系统中有一个密钥是所有对称密钥的衍生者，便不能认为那是一个“完美向前保密”的系统，在这种情况下，一旦破解了根密钥，便能拿到自它衍生的所有密钥，受那些密钥保护的全部数据都会曝光
> 
> 在IPsec里，PFS是通过在IPsec SA协商阶段从新进行一次DH交换来实现的
> 
> ![VPN%20%E6%95%85%E4%BA%8B%20d9e87ad760724bf3a2a3bf83c1572887/image12.png](VPN%20故事/image12.png)
> 
> ![VPN%20%E6%95%85%E4%BA%8B%20d9e87ad760724bf3a2a3bf83c1572887/image13.png](VPN%20故事/image13.png)
> 
> IPsec的基本概念
> 
> 在internet上协商出一条隧道，对数据进行加密，IPsec是一个三层的协议
> 
> **IPsec的两种模式**
> 
> 1、Transport mode（传输模式）
> 
> 加密点等于通信点，可以保留原数据包的IP头部
> 
> 2、Tunnel mode（通道模式）
> 
> 加密点不等于通信点，它需要使用一个新的IP头部
> 
> 二层VPN : ATM/Frame Relay/DDN/ISDN
> 
> 三层VPN : IPSEC/GRE/L2TP
> 
> 应用层VPN : Web VPN/SSL VPN
> 
> 两个概念
> 
> 通信点：实际通信的设备
> 
> 加密点：完成加密的设备
> 
> ![VPN%20%E6%95%85%E4%BA%8B%20d9e87ad760724bf3a2a3bf83c1572887/image14.png](VPN%20故事/image14.png)
> 
> ![VPN%20%E6%95%85%E4%BA%8B%20d9e87ad760724bf3a2a3bf83c1572887/image15.png](VPN%20故事/image15.png)
> 
> ![VPN%20%E6%95%85%E4%BA%8B%20d9e87ad760724bf3a2a3bf83c1572887/image16.png](VPN%20故事/image16.png)
> 
> ![VPN%20%E6%95%85%E4%BA%8B%20d9e87ad760724bf3a2a3bf83c1572887/image17.png](VPN%20故事/image17.png)
> 
> 怎样选取IPsec的保护模式
> 
> Tunnel mode：产生新的可路由IP头部，可解决不同私网之间跨越internet数据包的加密传送。加密点不管等不等于通信点都可以使用
> 
> Transport mode：不产生新的IP头部，要求原IP包可在internet路由，要求通信点和加密点为同一IP。
> 
> 建议：如果能用传输模式就用传输模式，想一想为什么？
> 
> ![VPN%20%E6%95%85%E4%BA%8B%20d9e87ad760724bf3a2a3bf83c1572887/image18.png](VPN%20故事/image18.png)
> 
> SA-安全联盟
> 
> “安全联盟”（IPsec术语，常常简称SA）是构成IPsec的基础。**SA是两个通信实体经协商建立起来的一种协定**。**它们决定了用来保护数据包安全的IPsec协议、转码方式、密钥以及密钥的有效存在时间等等**。任何IPsec实施方案始终会构建一个SA数据库（SADB），由他来维护IPsec协议用来保障数据包安全的SA记录
> 
> SA是单向的。如果两个主机（A和B）正在通过ESP进行安全通信，那么主机A就需要一个SA，即SA（out），用来处理外发的数据包；另外还需要有一个不同SA，即SA（in），用来处理进入的数据包。**主机A的SA(out)和主机B的SA（in）将共享相同的加密参数（比如密钥）。** //加密解密
> 
> **SA还是“与协议相关”的**。每种协议都有一个SA。如果主机A和B同时通过AH和ESP进行安全通信，那么每个主机都会针对每一种协议来构建一个独立的SA
> 
> ![VPN%20%E6%95%85%E4%BA%8B%20d9e87ad760724bf3a2a3bf83c1572887/image19.png](VPN%20故事/image19.png)
> 
> IPsec的组成部分
> 
> 1、ESP（负载安全封装）协议
> 
> 2、认证头（AH）协议
> 
> 3、internet密钥交换（IKE）协议
> 
> ESP
> 
> 封装安全有效负载,一种提供数据加密的协议,同时支持验证和防重发功能,它完整封装用户数据,可独自使用或与AH配合使用.ESP使用IP协议号50（想想协议号）进行通信.
> 
> 不对IP头部进行加密
> 
> Authentication Data(认证字段)不包含在ESP Header字段中.
> 
> ![VPN%20%E6%95%85%E4%BA%8B%20d9e87ad760724bf3a2a3bf83c1572887/image20.png](VPN%20故事/image20.png)
> 
> ![VPN%20%E6%95%85%E4%BA%8B%20d9e87ad760724bf3a2a3bf83c1572887/image21.png](VPN%20故事/image21.png)
> 
> ![VPN%20%E6%95%85%E4%BA%8B%20d9e87ad760724bf3a2a3bf83c1572887/image22.png](VPN%20故事/image22.png)
> 
> ESP头部各字段含义如下：
> 
> - **SPI字段**（Security Parameter Index(SPI)）：确定安全关联的安全参数索引,用于和IP头之前的目标地址以及协议一起标识一个安全关联。[32比特]
> - **序列号字段**（Sequence Number:）：用来提供防重放保护，跟验证报头中描述的一样。[32比特]
> - **有效载荷数据**（Payload Data）：传输层数据段（传输模式）或IP包（隧道模式），通过加密受到保护。也可在保护数据字段中包含一个加密算法可能需要用到的初始化向量（IV）。以强制实施的算法（DES-CBC）来说，IV是“受保护数据”字段中的第一个8位组。[可变]
> - **填充字段**(Padding: Extra bytes)：加密算法需要的任何填充字节。[0～9/10字节]
> - **填充长度**（Pad length）：包含填充长度字段的字节数[64 bit/块]
> - **下一报头**（Next Header）：通过标识载荷中的第一个头（如IPv6中的扩展头，或诸如TCP之类的上层协议头），决定载荷数据字段中数据的类型。
> 
> next header 取值: 1 for ICMP / 4 for IP-in-IP encapsulation / 6 for TCP / 17 for UDP
> 
> - **有效载荷数据**（Authentication Data）：长度可变的字段（应为32位字的整数倍），用于填入ICV。ICV的计算范围为ESP包中除掉验证数据字段的部分。
> 
> RFC2406对ESP头的格式、位置、验证的范围及进入和外出处理规则进行了描述。
> 
> AH-----Authentication Header(认证报头)
> 
> 验证头部,一种安全协议,只是用来验证头部和防重发.不对实际用户数据部分加密.可配合ESP使用.AH使用IP协议51进行通信.AH是为IP数据报提供无连接的完整性和数据来源验证,并提供重放(replay)攻击保护.
> 
> 使用AH时,永远不能穿越PAT设备(穿越PAT时,源IP地址会变)；做HASH验证时:不计算TTL值；
> 
> Authentication Data(认证字段)包含在AH Header字段中.
> 
> ![VPN%20%E6%95%85%E4%BA%8B%20d9e87ad760724bf3a2a3bf83c1572887/image23.png](VPN%20故事/image23.png)
> 
> AH头部各字段含义如下：
> 
> - 下一头（8比特）：标识紧跟验证头的下一个头的类型。在传输模式下，将是处于保护的上层协议的值，如UDP或TCP的协议值。在通道模式下，将是值4，表示IP－in－IP(IPv4)封装或IPv6封装的41这个值。
> - 载荷长度（8比特）：以32位字为单位的验证头的长度，再减去2。例如，缺省的验证数据字段的长度是96比特（3个32位字），加上3个字长的固定头，头部共6个字长，因此该字段的值为4。
> - 保留（16比特）：为将来使用。
> - 安全参数索引（32比特）：用于与外部IP头的目的地址一起标识一个安全关联。
> - 序号（8比特）：单增的计数器值，用于提供抗重播功能。
> - 验证数据（可变）：该字段的长度可变（但应为32位字的整数倍），包含的数据有数据包的ICV（完整性校验值）或MAC。
> 
> RFC2402对AH头的格式、位置、验证的范围及进入和外出处理规则进行了描述。
> 
> ![VPN%20%E6%95%85%E4%BA%8B%20d9e87ad760724bf3a2a3bf83c1572887/image24.png](VPN%20故事/image24.png)
> 
> ![VPN%20%E6%95%85%E4%BA%8B%20d9e87ad760724bf3a2a3bf83c1572887/image25.png](VPN%20故事/image25.png)
> 
> IKE-----Internet Key Exchange(Internet密钥交换协议)
> 
> 负责各种IPSEC选项的协商、认证通信的每一端(应用时包括公钥交换),以及管理IPSEC隧道的会话密钥.IKE使用用户数据报协议(UDP)端口500(通常用于源和目的双方)进行通信.
> 
> 一种在Internet Security Association and Key Management Protocol (ISAKMP) 框架中使用Oakley和SKEME协议组的混合协议.IKE通常用来确定一个共享的安全策略和对需要KEY 的KEY服务的验证,在IPSEC流量能通过之前,先要对router/firewall/host 这些对等体进行身份验证.**可以在双边手工输入预共享(pre-share)key或者通过CA获得KEY,通过双边协商双边获得统一IKE的SA**,建立初步的安全通道,为接下来的IPSEC作准备.
> 
> IKE的功能:
> 
> 1. Negotiating protocol parameters 协商协议参数
> 
> 2. Exchanging public keys 交换公钥
> 
> 3. Authenticating both sides 认证PEER
> 
> 4. Managing keys after the exchange 管理交换完成的KEY
> 
> IKE是一个"元"(meta)协议: "ISAKMP" = "Oakley" + "SKEME" 三个部分
> 
> 1. ISAKMP----Internet Security Association and Key Management Potocol
> 
> (Internet安全连接和密钥管理协议)
> 
> 作用:定义了一个信息交换的体系架构,包括包的格式和分组在两个Peer之间的传送方式和状态.
> 
> 2. Oakley ------ 一种KEY交换协议,它的一个基本机制就是Diffie-Hellman KEY交换算法
> 
> 作用:提供了为在2个IPSec Peer 之间达成一种相同的加密密钥,而需要的一种基于模式的机制.用户从会话中得到加密密钥.
> 
> 3. SKEME-----Security Key Exchange Mechanism(安全密钥交换机制)使用什么方式来交换密钥
> 
> 作用:提供了以认证为目的而使用公钥加密的机制,用于认证 IKE SA 的两端.
> 
> ![VPN%20%E6%95%85%E4%BA%8B%20d9e87ad760724bf3a2a3bf83c1572887/image26.png](VPN%20故事/image26.png)
> 
> 实验1：Lan-to-Lan
> 
> ![VPN%20%E6%95%85%E4%BA%8B%20d9e87ad760724bf3a2a3bf83c1572887/image27.png](VPN%20故事/image27.png)
> 
> IKE Phase I Policy:
> 
> 协商策略(策略可以建立多个,发起方会将自己的所有策略发给对方,对方会按收到的序号最小的开始匹配；双方完全匹配的策略会由对方发回到发起方,表示确认,并使用此策略):
> 
> R2(config)#crypto isakmp policy 2 <===策略号只是本地有效(建议两端相同)
> 
> R2(config-isakmp)#authentication pre-share <====认证方法(Pre-share/rsa-encr/rsa-sig)
> 
> R2(config-isakmp)#hash md5 <====对协商包进行认证
> 
> R2(config-isakmp)#encryption 3des <===对协商的数据进行"3des"加密(两端一定要相同)
> 
> R2(config-isakmp)#group 2 <===两端组号一定要相同(不同的组:加密的位数也不相同)
> 
> R2(config-isakmp)#lifetime 60 <===多少秒后,重新协商(默认为:86400 second )
> 
> R2(config)#crypto isakmp key 0 surpass address 13.1.1.3 <===使用"Pre-share"认证方式,才要输入此命令
> 
> "0":密钥将以明文方式发向"13.1.1.3"
> 
> key后面还有个"6"，表示密文。
> 
> "surpass":密码(两端一定要一样)
> 
> - --------------------------------------------
> 
> R3(config)#crypto isakmp policy 3
> 
> R3(config-isakmp)#authentication pre-share
> 
> R3(config-isakmp)#hash md5
> 
> R3(config-isakmp)#encryption 3des
> 
> R3(config-isakmp)#group 2
> 
> R3(config)#crypto isakmp key 0 surpass address 12.1.1.2
> 
> IKE Phase II Policy:
> 
> 定义转换集(本地所有的转换集要发往对方,让对方匹配自己的转换集,然后返回确认；可设置多个):
> 
> R2(config)#crypto ipsec transform-set cisco esp-des esp-sha-hmac
> 
> "cisco":transform-set的名字
> 
> "esp-des esp-sha-hmac":transform-set的加密和认证方式(选择"esp-null":不对数据加密)
> 
> R2(cfg-crypto-trans)#mode tunnel <===可选择 transport/tunnel(但Lan-to-Lan只能选择:tunnel模式)
> 
> 定义感兴趣流:
> 
> R2(config)#access-list 101 permit ip 2.2.2.0 0.0.0.255 3.3.3.0 0.0.0.255
> 
> 或者: R2(config)#ip access-list extended VPN
> 
> R2(config-ext-nacl)#permit ip 2.2.2.0 0.0.0.255 3.3.3.0 0.0.0.255
> 
> 定义MAP:
> 
> R2(config)#crypto map huawei 10 ipsec-isakmp
> 
> "huawei":定义MAP的名字
> 
> "10":序号
> 
> "ipsec-isakmp":可选择 ipsec-isakmp(自动)/ ipsec-manual(手动)
> 
> R2(config-crypto-map)#set peer 13.1.1.3 <===当满足了感兴趣流之后,和"13.1.1.3"建立peer
> 
> R2(config-crypto-map)#set transform-set cisco <===调用名字为"cisco"的transform-set
> 
> 或者: R2(config-crypto-map)#set transform-set cisco cisco2 <===后面可写多个"transform-set"
> 
> R2(config-crypto-map)#set pfs <===可选择(group1/group2/group5),默认为"group1"
> 
> R2(config-crypto-map)#match address 101 <===匹配"101"(或者是"VPN")的感兴趣流
> 
> - --------------------------------------------------
> 
> R3(config)#crypto ipsec transform-set cisco esp-des esp-sha-hmac
> 
> R3(cfg-crypto-trans)#mode tunnel
> 
> R3(config)#access-list 101 permit ip 3.3.3.0 0.0.0.255 2.2.2.0 0.0.0.255
> 
> R3(config)#crypto map huawei 10 ipsec-isakmp
> 
> R3(config-crypto-map)#set peer 12.1.1.2
> 
> R3(config-crypto-map)#set transform-set cisco
> 
> R3(config-crypto-map)#set pfs
> 
> R3(config-crypto-map)#match address 101
> 
> Apply VPN Configuration:
> 
> 在接口上调用名字为"huawei"的MAP:
> 
> R2(config)#interface e0/0
> 
> R2(config-if)#crypto map huawei
> 
> - -----------------------------------
> 
> R3(config)#interface e0/0
> 
> R3(config-if)#crypto map huawei
> 
> ip route 0.0.0.0 0.0.0.0 s1/0
> 
> 调试:
> 
> R2#debug crypto isakmp <===查看第一阶段的IKE
> 
> R2#debug crypto ipsec <===查看第二阶段的IKE
> 
> IPSEC中Lan-to-Lan的建立过程:
> 
> R2#ping 3.3.3.3 source 2.2.2.2
> 
> Type escape sequence to abort.
> 
> Sending 5, 100-byte ICMP Echos to 3.3.3.3, timeout is 2 seconds:
> 
> Packet sent with a source address of 2.2.2.2
> 
> - Mar 1 00:55:40.767: IPSEC(sa_request): ,
> 
> (key eng. msg.) OUTBOUND local= 12.1.1.2, remote= 13.1.1.3, <==由于ping包的触发,开始建立IPSEC通道
> 
> local_proxy= 2.2.2.0/255.255.255.0/0/0 (type=4),
> 
> remote_proxy= 3.3.3.0/255.255.255.0/0/0 (type=4),
> 
> protocol= ESP, transform= esp-des esp-sha-hmac (Tunnel),
> 
> lifedur= 3600s and 4608000kb,
> 
> spi= 0x5E39E570(1580852592), conn_id= 0, keysize= 0, flags= 0x400B
> 
> - Mar 1 00:55:40.767: ISAKMP: received ke message (1/1) <===IKE的第一阶段
> - Mar 1 00:55:40.771: ISAKMP (0:0): SA request profile is (NULL)
> - Mar 1 00:55:40.771: ISAKMP: local port 500, remote port 500
> - Mar 1 00:55:40.771: ISAKMP: set new node 0 to QM_IDLE
> - Mar 1 00:55:40.771: ISAKMP: Find a dup sa in the avl tree during calling isadb_insert sa = 628E53B8
> - Mar 1 00:55:40.771: ISAKMP (0:2): Can not start Aggressive mode, trying Main mode.
> - Mar 1 00:55:40.775: ISAKMP: Looking for a matching key for 13.1.1.3 in default : success
> - Mar 1 00:55:40.775: ISAKMP (0:2): found peer pre-shared key matching 13.1.1.3
> - Mar 1 00:55:40.775: ISAKMP (0:2): constructed NAT-T vendor-07 ID
> - Mar 1 00:55:40.775: ISAKMP (0:2): constructed NAT-T vendor-03 ID
> - Mar 1 00:55:40.775: ISAKMP (0:2): constructed NAT-T vendor-02 ID
> - Mar 1 00:55:40.775: ISAKMP (0:2): Input = IKE_MESG_FROM_IPSEC, IKE_SA_REQ_MM
> - Mar 1 00:55:40.775: ISAKMP (0:2): Old State = IKE_READY New State = IKE_I_MM1
> 
> IKE第一阶段的第一个包的交换
> 
> - Mar 1 00:55:40.775: ISAKMP (0:2): beginning Main Mode exchange <==开始使用Main mode
> - Mar 1 00:55:40.775: ISAKMP (0:2): sending packet to 13.1.1.3 my_port 500 peer_port 500 (I) MM_NO_STATE 发协包到对方PEER"13.1.1.3" 源端口:500 目标端口:500
> - Mar 1 00:55:40.963: ISAKMP (0:2): received packet from 13.1.1.3 dport 500 sport 500 Global (I) MM_NO_STATE
> - Mar 1 00:55:40.967: ISAKMP (0:2): Input = IKE_MESG_FROM_PEER, IKE_MM_EXCH
> - Mar 1 00:55:40.967: ISAKMP (0:2): Old State = IKE_I_MM1 New State = IKE_I_MM2
> 
> IKE第一阶段的第二个包的交换
> 
> - Mar 1 00:55:40.967: ISAKMP (0:2): processing SA payload. message ID = 0
> - Mar 1 00:55:40.967: ISAKMP (0:2): processing vendor id payload
> - M.!!!!
> 
> Success rate is 80 percent (4/5), round-trip min/avg/max = 12/12/12 ms
> 
> R2#ar 1 00:55:40.971: ISAKMP (0:2): vendor ID seems Unity/DPD but major 245 mismatch
> 
> - Mar 1 00:55:40.971: ISAKMP (0:2): vendor ID is NAT-T v7
> - Mar 1 00:55:40.971: ISAKMP: Looking for a matching key for 13.1.1.3 in default : success
> - Mar 1 00:55:40.971: ISAKMP (0:2): found peer pre-shared key matching 13.1.1.3
> - Mar 1 00:55:40.971: ISAKMP (0:2) local preshared key found
> - Mar 1 00:55:40.971: ISAKMP : Scanning profiles for xauth ...
> - Mar 1 00:55:40.971: ISAKMP (0:2): Checking ISAKMP transform 1 against priority 2 policy
> - Mar 1 00:55:40.971: ISAKMP: encryption 3DES-CBC
> - Mar 1 00:55:40.971: ISAKMP: hash MD5
> - Mar 1 00:55:40.971: ISAKMP: default group 2
> - Mar 1 00:55:40.971: ISAKMP: auth pre-share
> - Mar 1 00:55:40.971: ISAKMP: life type in seconds
> - Mar 1 00:55:40.975: ISAKMP: life duration (basic) of 60
> - Mar 1 00:55:40.975: ISAKMP (0:2): atts are acceptable. Next payload is 0 <===表示策略匹配协商完成
> - Mar 1 00:55:41.143: ISAKMP (0:2): processing vendor id payload
> - Mar 1 00:55:41.143: ISAKMP (0:2): vendor ID seems Unity/DPD but major 245 mismatch
> - Mar 1 00:55:41.143: ISAKMP (0:2): vendor ID is NAT-T v7
> - Mar 1 00:55:41.143: ISAKMP (0:2): Input = IKE_MESG_INTERNAL, IKE_PROCESS_MAIN_MODE
> - Mar 1 00:55:41.143: ISAKMP (0:2): Old State = IKE_I_MM2 New State = IKE_I_MM2
> - Mar 1 00:55:41.147: ISAKMP (0:2): sending packet to 13.1.1.3 my_port 500 peer_port 500 (I) MM_SA_SETUP
> - Mar 1 00:55:41.151: ISAKMP (0:2): Input = IKE_MESG_INTERNAL, IKE_PROCESS_COMPLETE
> - Mar 1 00:55:41.151: ISAKMP (0:2): Old State = IKE_I_MM2 New State = IKE_I_MM3
> 
> IKE第一阶段的第三个包的交换
> 
> - Mar 1 00:55:41.371: ISAKMP (0:1): purging node -1572961127
> - Mar 1 00:55:41.383: ISAKMP (0:2): received packet from 13.1.1.3 dport 500 sport 500 Global (I) MM_SA_SETUP
> - Mar 1 00:55:41.387: ISAKMP (0:2): Input = IKE_MESG_FROM_PEER, IKE_MM_EXCH
> - Mar 1 00:55:41.387: ISAKMP (0:2): Old State = IKE_I_MM3 New State = IKE_I_MM4
> 
> IKE第一阶段的第四个包的交换
> 
> - Mar 1 00:55:41.387: ISAKMP (0:2): processing KE payload. message ID = 0
> - Mar 1 00:55:41.603: ISAKMP (0:2): processing NONCE payload. message ID = 0
> - Mar 1 00:55:41.607: ISAKMP: Looking for a matching key for 13.1.1.3 in default : success
> - Mar 1 00:55:41.607: ISAKMP (0:2): found peer pre-shared key matching 13.1.1.3
> - Mar 1 00:55:41.607: ISAKMP (0:2): SKEYID state generated <===当第三、四个包完成后，就会产生SKEYID
> - Mar 1 00:55:41.607: ISAKMP (0:2): processing vendor id payload
> - Mar 1 00:55:41.607: ISAKMP (0:2): vendor ID is Unity
> - Mar 1 00:55:41.611: ISAKMP (0:2): processing vendor id payload
> - Mar 1 00:55:41.611: ISAKMP (0:2): vendor ID is DPD
> - Mar 1 00:55:41.611: ISAKMP (0:2): processing vendor id payload
> - Mar 1 00:55:41.611: ISAKMP (0:2): speaking to another IOS box!
> - Mar 1 00:55:41.611: ISAKMP (0:2): Input = IKE_MESG_INTERNAL, IKE_PROCESS_MAIN_MODE
> - Mar 1 00:55:41.611: ISAKMP (0:2): Old State = IKE_I_MM4 New State = IKE_I_MM4
> - Mar 1 00:55:41.615: ISAKMP (0:2): Send initial contact
> - Mar 1 00:55:41.615: ISAKMP (0:2): SA is doing pre-shared key authentication using id type ID_IPV4_ADDR
> - Mar 1 00:55:41.615: ISAKMP (0:2): ID payload
> 
> next-payload : 8
> 
> type : 1
> 
> address : 12.1.1.2
> 
> protocol : 17
> 
> port : 500
> 
> length : 12
> 
> - Mar 1 00:55:41.619: ISAKMP (2): Total payload length: 12
> - Mar 1 00:55:41.619: ISAKMP (0:2): sending packet to 13.1.1.3 my_port 500 peer_port 500 (I) MM_KEY_EXCH
> - Mar 1 00:55:41.623: ISAKMP (0:2): Input = IKE_MESG_INTERNAL, IKE_PROCESS_COMPLETE
> - Mar 1 00:55:41.623: ISAKMP (0:2): Old State = IKE_I_MM4 New State = IKE_I_MM5
> 
> IKE第一阶段的第五个包的交换
> 
> - Mar 1 00:55:41.643: ISAKMP (0:2): received packet from 13.1.1.3 dport 500 sport 500 Global (I) MM_KEY_EXCH
> - Mar 1 00:55:41.647: ISAKMP (0:2): processing ID payload. message ID = 0
> - Mar 1 00:55:41.647: ISAKMP (0:2): ID payload
> 
> next-payload : 8
> 
> type : 1
> 
> address : 13.1.1.3
> 
> protocol : 17
> 
> port : 500
> 
> length : 12
> 
> - Mar 1 00:55:41.647: ISAKMP (0:2): processing HASH payload. message ID = 0
> - Mar 1 00:55:41.651: ISAKMP (0:2): SA authentication status:
> 
> authenticated
> 
> - Mar 1 00:55:41.651: ISAKMP (0:2): SA has been authenticated with 13.1.1.3
> - Mar 1 00:55:41.651: ISAKMP (0:2): peer matches *none* of the profiles
> - Mar 1 00:55:41.651: ISAKMP (0:2): Input = IKE_MESG_FROM_PEER, IKE_MM_EXCH
> - Mar 1 00:55:41.651: ISAKMP (0:2): Old State = IKE_I_MM5 New State = IKE_I_MM6
> 
> IKE第一阶段的第六个包的交换
> 
> - Mar 1 00:55:41.655: ISAKMP (0:2): Input = IKE_MESG_INTERNAL, IKE_PROCESS_MAIN_MODE
> - Mar 1 00:55:41.655: ISAKMP (0:2): Old State = IKE_I_MM6 New State = IKE_I_MM6
> - Mar 1 00:55:41.659: ISAKMP (0:2): Input = IKE_MESG_INTERNAL, IKE_PROCESS_COMPLETE
> - Mar 1 00:55:41.659: ISAKMP (0:2): Old State = IKE_I_MM6 New State = IKE_P1_COMPLETE
> - Mar 1 00:55:41.659: ISAKMP (0:2): received packet from 13.1.1.3 dport 500 sport 500 Global (I) MM_KEY_EXCH
> - Mar 1 00:55:41.663: ISAKMP: set new node -1323939639 to QM_IDLE
> - Mar 1 00:55:41.663: ISAKMP (0:2): processing HASH payload. message ID = -1323939639
> - Mar 1 00:55:41.667: ISAKMP (0:2): processing DELETE payload. message ID = -1323939639
> - Mar 1 00:55:41.667: ISAKMP (0:2): peer does not do paranoid keepalives.
> - Mar 1 00:55:41.667: ISAKMP (0:2): deleting node -1323939639 error FALSE reason "informational (in) state 1"
> - Mar 1 00:55:41.667: ISAKMP (0:2): beginning Quick Mode exchange, M-ID of -426260398
> 
> IKE的第二阶段的快速模式的开始
> 
> - Mar 1 00:55:41.775: IPSEC(key_engine): got a queue event...
> - Mar 1 00:55:41.775: IPSEC(key_engine_delete_sas): rec'd delete notify from ISAKMP
> - Mar 1 00:55:41.779: ISAKMP (0:2): sending packet to 13.1.1.3 my_port 500 peer_port 500 (I) QM_IDLE
> - Mar 1 00:55:41.779: ISAKMP (0:2): Node -426260398, Input = IKE_MESG_INTERNAL, IKE_INIT_QM
> - Mar 1 00:55:41.779: ISAKMP (0:2): Old State = IKE_QM_READY New State = IKE_QM_I_QM1
> - Mar 1 00:55:41.779: ISAKMP (0:2): Input = IKE_MESG_INTERNAL, IKE_PHASE1_COMPLETE
> - Mar 1 00:55:41.783: ISAKMP (0:2): Old State = IKE_P1_COMPLETE New State = IKE_P1_COMPLETE
> - Mar 1 00:55:42.287: ISAKMP (0:2): received packet from 13.1.1.3 dport 500 sport 500 Global (I) QM_IDLE
> - Mar 1 00:55:42.295: ISAKMP (0:2): processing HASH payload. message ID = -426260398
> - Mar 1 00:55:42.295: ISAKMP (0:2): processing SA payload. message ID = -426260398
> - Mar 1 00:55:42.295: ISAKMP (0:2): Checking IPSec proposal 1
> - Mar 1 00:55:42.295: ISAKMP: transform 1, ESP_DES
> - Mar 1 00:55:42.295: ISAKMP: attributes in transform:
> - Mar 1 00:55:42.295: ISAKMP: encaps is 1 (Tunnel)
> - Mar 1 00:55:42.295: ISAKMP: SA life type in seconds
> - Mar 1 00:55:42.295: ISAKMP: SA life duration (basic) of 3600
> - Mar 1 00:55:42.295: ISAKMP: SA life type in kilobytes
> - Mar 1 00:55:42.295: ISAKMP: SA life duration (VPI) of 0x0 0x46 0x50 0x0
> - Mar 1 00:55:42.295: ISAKMP: authenticator is HMAC-SHA
> - Mar 1 00:55:42.295: ISAKMP: group is 1
> - Mar 1 00:55:42.299: ISAKMP (0:2): atts are acceptable.
> - Mar 1 00:55:42.299: IPSEC(validate_proposal_request): proposal part #1,
> 
> (key eng. msg.) INBOUND local= 12.1.1.2, remote= 13.1.1.3,
> 
> local_proxy= 2.2.2.0/255.255.255.0/0/0 (type=4),
> 
> remote_proxy= 3.3.3.0/255.255.255.0/0/0 (type=4),
> 
> protocol= ESP, transform= esp-des esp-sha-hmac (Tunnel),
> 
> lifedur= 0s and 0kb,
> 
> spi= 0x0(0), conn_id= 0, keysize= 0, flags= 0x12
> 
> - Mar 1 00:55:42.299: IPSEC(kei_proxy): head = huawei, map->ivrf = , kei->ivrf =
> - Mar 1 00:55:42.303: ISAKMP (0:2): processing NONCE payload. message ID = -426260398
> - Mar 1 00:55:42.303: ISAKMP (0:2): processing KE payload. message ID = -426260398
> - Mar 1 00:55:42.431: ISAKMP (0:2): processing ID payload. message ID = -426260398
> - Mar 1 00:55:42.431: ISAKMP (0:2): processing ID payload. message ID = -426260398
> - Mar 1 00:55:42.443: ISAKMP (0:2): Creating IPSec SAs
> - Mar 1 00:55:42.443: inbound SA from 13.1.1.3 to 12.1.1.2 (f/i) 0/ 0
> 
> (proxy 3.3.3.0 to 2.2.2.0)
> 
> - Mar 1 00:55:42.443: has spi 0x5E39E570 and conn_id 2000 and flags 13
> - Mar 1 00:55:42.443: lifetime of 3600 seconds
> - Mar 1 00:55:42.443: lifetime of 4608000 kilobytes
> - Mar 1 00:55:42.443: has client flags 0x0
> - Mar 1 00:55:42.443: outbound SA from 12.1.1.2 to 13.1.1.3 (f/i) 0/ 0 (proxy 2.2.2.0 to 3.3.3.0 )
> - Mar 1 00:55:42.443: has spi 235339588 and conn_id 2001 and flags 1B
> - Mar 1 00:55:42.443: lifetime of 3600 seconds
> - Mar 1 00:55:42.443: lifetime of 4608000 kilobytes
> - Mar 1 00:55:42.443: has client flags 0x0
> - Mar 1 00:55:42.447: ISAKMP (0:2): sending packet to 13.1.1.3 my_port 500 peer_port 500 (I) QM_IDLE
> - Mar 1 00:55:42.447: ISAKMP (0:2): deleting node -426260398 error FALSE reason ""
> - Mar 1 00:55:42.447: ISAKMP (0:2): Node -426260398, Input = IKE_MESG_FROM_PEER, IKE_QM_EXCH
> - Mar 1 00:55:42.447: ISAKMP (0:2): Old State = IKE_QM_I_QM1 New State = IKE_QM_PHASE2_COMPLETE
> - Mar 1 00:55:42.451: IPSEC(key_engine): got a queue event... 第二阶段完成后，就会建立SA
> - Mar 1 00:55:42.451: IPSEC(initialize_sas): ,
> 
> (key eng. msg.) INBOUND local= 12.1.1.2, remote= 13.1.1.3,
> 
> local_proxy= 2.2.2.0/255.255.255.0/0/0 (type=4),
> 
> remote_proxy= 3.3.3.0/255.255.255.0/0/0 (type=4),
> 
> protocol= ESP, transform= esp-des esp-sha-hmac (Tunnel),
> 
> lifedur= 3600s and 4608000kb,
> 
> spi= 0x5E39E570(1580852592), conn_id= 2000, keysize= 0, flags= 0x13 <===证明SA已经建立完成
> 
> - Mar 1 00:55:42.451: IPSEC(initialize_sas): ,
> 
> (key eng. msg.) OUTBOUND local= 12.1.1.2, remote= 13.1.1.3,
> 
> local_proxy= 2.2.2.0/255.255.255.0/0/0 (type=4),
> 
> remote_proxy= 3.3.3.0/255.255.255.0/0/0 (type=4),
> 
> protocol= ESP, transform= esp-des esp-sha-hmac (Tunnel),
> 
> lifedur= 3600s and 4608000kb,
> 
> spi= 0xE06FF44(235339588), conn_id= 2001, keysize= 0, flags= 0x1B
> 
> - Mar 1 00:55:42.455: IPSEC(kei_proxy): head = huawei, map->ivrf = , kei->ivrf =
> - Mar 1 00:55:42.455: IPSEC(crypto_ipsec_sa_find_ident_head): reconnecting with the same proxies and 13.1.1.3
> - Mar 1 00:55:42.455: IPSEC(add mtree): src 2.2.2.0, dest 3.3.3.0, dest_port 0
> - Mar 1 00:55:42.455: IPSEC(create_sa): sa created,
> 
> (sa) sa_dest= 12.1.1.2, sa_prot= 50,
> 
> sa_spi= 0x5E39E570(1580852592),
> 
> sa_trans= esp-des esp-sha-hmac , sa_conn_id= 2000
> 
> - Mar 1 00:55:42.455: IPSEC(create_sa): sa created,
> 
> (sa) sa_dest= 13.1.1.3, sa_prot= 50,
> 
> sa_spi= 0xE06FF44(235339588),
> 
> sa_trans= esp-des esp-sha-hmac , sa_conn_id= 2001
> 
> - Mar 1 00:55:51.371: ISAKMP (0:1): purging SA., sa=62E3C24C, delme=62E3C24C
> 
> 清除IPSEC中Lan-to-Lan的连接:
> 
> R2#clear crypto isakmp <===清除第一阶段的IKE
> 
> R2#clear crypto sa
> 
> R2#show crypto isakmp sa
> 
> R2#show crypto ipsec sa
> 
> interface: Ethernet0/0
> 
> Crypto map tag: huawei, local addr 12.1.1.2 <===本端的地址
> 
> protected vrf: (none)
> 
> local ident (addr/mask/prot/port): (2.2.2.0/255.255.255.0/0/0) <====本端的感兴趣流
> 
> remote ident (addr/mask/prot/port): (3.3.3.0/255.255.255.0/0/0) <====远端的感兴趣流
> 
> current_peer 13.1.1.3 port 500 <====远端的地址和端口号
> 
> PERMIT, flags={origin_is_acl,}
> 
> #pkts encaps: 3, #pkts encrypt: 3, #pkts digest: 3
> 
> #pkts decaps: 3, #pkts decrypt: 3, #pkts verify: 3
> 
> #pkts compressed: 0, #pkts decompressed: 0
> 
> #pkts not compressed: 0, #pkts compr. failed: 0
> 
> #pkts not decompressed: 0, #pkts decompress failed: 0
> 
> #send errors 0, #recv errors 0
> 
> local crypto endpt.: 12.1.1.2, remote crypto endpt.: 13.1.1.3
> 
> path mtu 1500, ip mtu 1500
> 
> current outbound spi: 0x5C587C54(1549302868)
> 
> inbound esp sas:
> 
> spi: 0xECCDDAEC(3972913900)
> 
> transform: esp-des esp-sha-hmac ,
> 
> in use settings ={Tunnel, }
> 
> conn id: 2001, flow_id: 1, crypto map: huawei
> 
> sa timing: remaining key lifetime (k/sec): (4449567/3167)
> 
> IV size: 8 bytes
> 
> replay detection support: Y
> 
> Status: ACTIVE
> 
> inbound ah sas:
> 
> inbound pcp sas:
> 
> outbound esp sas:
> 
> spi: 0x5C587C54(1549302868) <===本地"outbound"的"spi" ,就是对方"inbound"的"spi"
> 
> transform: esp-des esp-sha-hmac ,
> 
> in use settings ={Tunnel, }
> 
> conn id: 2002, flow_id: 2, crypto map: huawei
> 
> sa timing: remaining key lifetime (k/sec): (4449567/3165)
> 
> SA Lifetime: Data-based/Time-based
> 
> 假设两端时间不相同:由时间小的一端发起PING包是可通的,但由时间大的一端发起PING包是不通的.
> 
> IV size: 8 bytes
> 
> replay detection support: Y
> 
> Status: ACTIVE
> 
> outbound ah sas:
> 
> outbound pcp sas:
> 
> R2#show crypto map
> 
> Crypto Map "huawei" 10 ipsec-isakmp
> 
> Peer = 13.1.1.3
> 
> Extended IP access list VPN
> 
> access-list VPN permit ip 2.2.2.0 0.0.0.255 3.3.3.0 0.0.0.255
> 
> Current peer: 13.1.1.3
> 
> Security association lifetime: 4608000 kilobytes/3600 seconds <===两端协商时间,使用小的时间("Security association lifetime"中的"seconds")
> 
> PFS (Y/N): Y <===重新做一次Diffie-Hellman交换
> 
> 只有一端配置了PFS:
> 
> (1) 由配置了PFS的一端发起连接是可以成功的(但会显示"Attributes Not Supported",然后继续协商)
> 
> (2) 由没有配置了PFS的一端发起连接是不成功的
> 
> DH group: group1
> 
> Transform sets={
> 
> cisco,
> 
> }
> 
> Interfaces using crypto map huawei:
> 
> Ethernet0/0
> 
> 更改Security association lifetime:
> 
> R2(config)#crypto ipsec security-association lifetime seconds 600
> 
> R2(config)#crypto ipsec security-association lifetime kilobytes 10240
> 
> R2#show crypto engine connections active
> 
> ID Interface IP-Address State Algorithm Encrypt Decrypt
> 
> 1 Ethernet0/0 12.1.1.2 set HMAC_MD5+3DES_56_C 0 0
> 
> 2001 Ethernet0/0 12.1.1.2 set DES+SHA 0 99
> 
> 2002 Ethernet0/0 12.1.1.2 set DES+SHA 99 0
> 
> 实验2：Router Remote VPN ----- 只能是动态IP的一方发起连接(即,下例:"remote"方发起连接)
> 
> ![VPN%20%E6%95%85%E4%BA%8B%20d9e87ad760724bf3a2a3bf83c1572887/image28.png](VPN%20故事/image28.png)
> 
> IKE Phase I Policy:
> 
> R2(config)#crypto isakmp policy 2
> 
> R2(config-isakmp)#authentication pre-share
> 
> R2(config-isakmp)#hash md5
> 
> R2(config-isakmp)#encryption 3des
> 
> R2(config-isakmp)#group 2
> 
> R2(config)#crypto isakmp key 0 surpass address 0.0.0.0 0.0.0.0 <====由于是动态VPN,对端的地址不固定,所以写0.0.0.0
> 
> - --------------------------------------------------------
> 
> remote(config)#crypto isakmp policy 2
> 
> remote(config-isakmp)#authentication pre-share
> 
> remote(config-isakmp)#hash md5
> 
> remote(config-isakmp)#encryption 3des
> 
> remote(config-isakmp)#group 2
> 
> remote(config)#crypto isakmp key 0 surpass address 12.1.1.2
> 
> IKE Phase II Policy:
> 
> R2(config)#crypto ipsec transform-set cisco esp-des esp-sha-hmac
> 
> R2(cfg-crypto-trans)#mode tunnel
> 
> R2(config)#access-list 101 permit ip 2.2.2.0 0.0.0.255 3.3.3.0 0.0.0.255
> 
> Static Crypto Map:
> 
> R2(config)#crypto map huawei 10 ipsec-isakmp
> 
> R2(config-crypto-map)#set peer 0.0.0.0
> 
> R2(config-crypto-map)#set transform-set cisco
> 
> R2(config-crypto-map)#set pfs
> 
> R2(config-crypto-map)#match address 101
> 
> - ---------------------------------------------------------------------
> 
> remote(config)#crypto ipsec transform-set cisco esp-des esp-sha-hmac
> 
> remote(cfg-crypto-trans)#mode tunnel
> 
> Dynamic Crypto Map:
> 
> remote(config)#crypto dynamic-map dynamap 10
> 
> remote(config-crypto-map)#set transform-set cisco
> 
> remote(config-crypto-map)#set pfs
> 
> remote(config)#crypto map QQ 10 ipsec-isakmp dynamic dynamap
> 
> Apply VPN Configuration:
> 
> R2(config)#interface e0/0
> 
> R2(config-if)#crypto map huawei
> 
> - -----------------------------------
> 
> remote(config)#interface e0/0
> 
> remote(config-if)#crypto map QQ
> 
> 实验3：Lan-to-Lan (新命令)
> 
> ![VPN%20%E6%95%85%E4%BA%8B%20d9e87ad760724bf3a2a3bf83c1572887/image27.png](VPN%20故事/image27.png)
> 
> IKE Phase I Policy:
> 
> R2(config)#crypto isakmp policy 2
> 
> R2(config-isakmp)#authentication pre-share
> 
> R2(config-isakmp)#hash md5
> 
> R2(config-isakmp)#encryption 3des
> 
> R2(config-isakmp)#group 2
> 
> R2(config)#crypto keyring L2LKEY
> 
> R2(conf-keyring)#pre-shared-key address 13.1.1.3 key surpass
> 
> R2(config)#crypto isakmp profile L2L
> 
> R2(conf-isa-prof)#match identity address 13.1.1.3
> 
> R2(conf-isa-prof)#keyring L2LKEY
> 
> IPSec Phase II Policy:
> 
> R2(config)#crypto ipsec transform-set cisco esp-des esp-sha-hmac
> 
> R2(cfg-crypto-trans)#mode tunnel
> 
> R2(config)#access-list 101 permit ip 2.2.2.0 0.0.0.255 3.3.3.0 0.0.0.255
> 
> R2(config)#crypto map huawei 10 ipsec-isakmp
> 
> R2(config-crypto-map)#set peer 13.1.1.3
> 
> R2(config-crypto-map)#set transform-set cisco
> 
> R2(config-crypto-map)#set pfs
> 
> R2(config-crypto-map)#match address 101
> 
> R2(config-crypto-map)#set isakmp-profile L2L
> 
> R2(config-crypto-map)#reverse-route <===选其一:反向路由注入/静态(即:写了反向路由注入,可以不用写静态)
> 
> Apply VPN Configuration
> 
> R2(config)#interface ethernet 0/0
> 
> R2(config-if)#crypto map huawei
>