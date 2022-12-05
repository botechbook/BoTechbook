# 设置nameserver

设置nameserver

2014年10月24日

16:04

vim /etc/resolv.conf #设置nameserver地址：

nameserver 202.106.0.20

设置查找DNS的顺序

vim /etc/nsswitch.conf #这个文件里面有个选项是调节查DNS顺序的

hosts: files dns #就是这句，files指的是先查/etc/hosts文件的内容，dns是指后查dns_server的内容