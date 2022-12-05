# ovs agg bond 口

ovs agg bond 口

Tuesday, September 25, 2018

10:53 PM

**注意一定要允许agg的vlan的混杂模式和mac地址改变，在ovs里面的普通口也要允许混杂模式和mac地址改变, 另外如果是要agg口在ovs里面跑trunk模式，在VM的SW里面一定要用trunk**

apt-get install openvswitch-switch

#!/bin/bash

#ovs-vsctl add-br br10

#ovs-vsctl set bridge br10 stp_enable=true

#ovs-vsctl add-port br10 vlan9 tag=9 -- set interface vlan9 type=internal

ip link set br10 up

ip link add bond100 type bond

ip link set bond100 type bond mode 802.3ad

ip link set eth3 down

ip link set eth4 down

ip link set eth3 master bond100

ip link set eth4 master bond100

ip link set bond100 up

ip link add bond101 type bond

ip link set bond101 type bond mode 802.3ad

ip link set eth5 down

ip link set eth6 down

ip link set eth5 master bond101

ip link set eth6 master bond101

ip link set bond101 up

#ovs-vsctl add-port br10 bond100

#ovs-vsctl add-port br10 bond101

#ovs-vsctl add-port br10 eth2 tag=8

ip link set vlan9 up

ip add add 159.9.200.13/16 dev vlan9

=========================================

ovs-vsctl add-br br10

ovs-vsctl set bridge br10 stp_enable=true

ovs-vsctl add-port br10 vlan9 tag=9 -- set interface vlan9 type=internal

ip link set br10 up

ip link add bond20 type bond

ip link set bond20 type bond mode 802.3ad

ip link set eth3 down

ip link set eth4 down

ip link set eth3 master bond20

ip link set eth4 master bond20

ip link set bond20 up

ovs-vsctl add-port br10 bond20

ip link set vlan9 up

ip add add 159.9.200.13/16 dev vlan9