# 添加aggregate口

添加aggregate口

Wednesday, June 13, 2018

10:19 AM

ip link add bond0 type bond

ip link set bond0 type bond mode 802.3ad

ip link set eth2 down

ip link set eth3 down

ip link set eth2 master bond0

ip link set eth3 master bond0

ip link set bond0 up

ip link add link bond0 name bond0.970 type vlan id 970

ip link set bond0.970 up

ip add add 10.50.70.31/24 dev bond0.970

**cat /proc/net/bonding/bond0**

===============================================================

To use VLANs over bonds and bridges, proceed as follows:

1. Add a bond device as root:
# ip link add bond0 type bond
# ip link set bond0 type bond miimon 100 mode 802.3ad
# ip link set eth1 down
# ip link set eth1 master bond0
# ip link set eth2 down
# ip link set eth2 master bond0
# ip link set bond0 up
2. Set VLAN on the bond device:
# ip link add link bond0 name bond0.2 type vlan id 2
# ip link set bond0.2 up

=========================================================================================

To use VLANs over bonds and bridges, proceed as follows:

1. Add a bond device as root:
# ip link add bond0 type bond
# ip link set bond0 type bond miimon 100 mode active-backup
# ip link set em1 down
# ip link set em1 master bond0
# ip link set em2 down
# ip link set em2 master bond0
# ip link set bond0 up
2. Set VLAN on the bond device:
# ip link add link bond0 name bond0.2 type vlan id 2
# ip link set bond0.2 up
3. Add the bridge device and attach VLAN to it:
# ip link add br0 type bridge
# ip link set bond0.2 master br0
# ip link set br0 up

Pasted from <[https://access.redhat.com/documentation/en-us/red_hat_enterprise_linux/7/html/networking_guide/sec-vlan_on_bond_and_bridge_using_ip_commands](https://access.redhat.com/documentation/en-us/red_hat_enterprise_linux/7/html/networking_guide/sec-vlan_on_bond_and_bridge_using_ip_commands)>

To create a bond device, run:

$ ip link add name bond0 type bond

Different [operation modes](https://en.wikipedia.org/wiki/Link_Aggregation_Control_Protocol#Driver_modes) can be used with both bond and team devices. However, currently only LACP mode is supported in the ASIC. To set the bond device to LACP (802.3ad) mode, run:

$ ip link set dev bond0 type bond mode 802.3ad

As with the bridge device, enslaving a port netdev to the bond device is performed using the following commands:

$ ip link set dev sw1p5 master bond0
$ ip link set dev sw1p6 master bond0
$ ip link set dev bond0 up

To remove a port netdev from a bond, run:

$ ip link set dev sw1p5 nomaster

And to delete the bond device, run:

$ ip link del dev bond0

Pasted from <[https://github.com/Mellanox/mlxsw/wiki/Link-Aggregation#bond-device-configuration](https://github.com/Mellanox/mlxsw/wiki/Link-Aggregation#bond-device-configuration)>