# NAT

NAT

2015年6月5日

14:39

SNAT命令

iptables -t nat -A POSTROUTING -s 1.1.1.1/32 -j SNAT --to-source 2.2.2.2

DNAT命令

iptables -t nat -A PREROUTING -d 202.202.202.1 -j DNAT --to-destination 192.168.0.10