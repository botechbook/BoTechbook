# Iptables NAT配置

Iptables NAT配置

Monday, January 22, 2018

3:48 PM

iptables -t nat -A POSTROUTING -s 172.16.93.0/24  -j SNAT --to-source 10.0.0.1

Pasted from <[http://blog.51cto.com/lustlost/943110](http://blog.51cto.com/lustlost/943110)>