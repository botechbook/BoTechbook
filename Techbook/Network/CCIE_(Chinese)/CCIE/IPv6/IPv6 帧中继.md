# IPv6 帧中继

帧中继

2011年6月27日

17:24

![IPv6%20%E5%B8%A7%E4%B8%AD%E7%BB%A7%2085bc5734cf754b23ae84dcca1605e7ad/image1.png](IPv6%20帧中继/image1.png)

R1#sh run

Building configuration...

Current configuration : 1036 bytes

!

version 12.4

service timestamps debug datetime msec

service timestamps log datetime msec

no service password-encryption

!

hostname R1

!

boot-start-marker

boot-end-marker

!

!

no aaa new-model

memory-size iomem 5

!

!

ip cef

no ip domain lookup

!

!

!

!

!

interface FastEthernet0/0

no ip address

shutdown

duplex auto

speed auto

!

interface Serial1/0

no ip address

shutdown

serial restart-delay 0

no fair-queue

!

interface Serial1/1

no ip address

encapsulation frame-relay

ipv6 address 2001:1:1:11::1/64

serial restart-delay 0

clock rate 64000

frame-relay map ipv6 2001:1:1:11::2 102 broadcast

frame-relay map ipv6 2001:1:1:11::3 103 broadcast

no frame-relay inverse-arp

!

interface Serial1/2

no ip address

shutdown

serial restart-delay 0

!

interface Serial1/3

no ip address

shutdown

serial restart-delay 0

!

ip http server

no ip http secure-server

!

!

!

!

!

!

control-plane

!

!

!

!

!

!

line con 0

exec-timeout 0 0

logging synchronous

line aux 0

line vty 0 4

!

!

end

==========================================

R2#sh run

Building configuration...

Current configuration : 1036 bytes

!

version 12.4

service timestamps debug datetime msec

service timestamps log datetime msec

no service password-encryption

!

hostname R2

!

boot-start-marker

boot-end-marker

!

!

no aaa new-model

memory-size iomem 5

!

!

ip cef

no ip domain lookup

!

!

!

!

!

!

!

interface FastEthernet0/0

no ip address

shutdown

duplex auto

speed auto

!

interface Serial1/0

no ip address

shutdown

serial restart-delay 0

no fair-queue

!

interface Serial1/1

no ip address

encapsulation frame-relay

ipv6 address 2001:1:1:11::2/64

serial restart-delay 0

clock rate 64000

frame-relay map ipv6 2001:1:1:11::1 201 broadcast

frame-relay map ipv6 2001:1:1:11::3 201 broadcast

no frame-relay inverse-arp

!

interface Serial1/2

no ip address

shutdown

serial restart-delay 0

!

interface Serial1/3

no ip address

shutdown

serial restart-delay 0

!

ip http server

no ip http secure-server

!

!

!

!

!

!

control-plane

!

!

!

!

!

line con 0

exec-timeout 0 0

logging synchronous

line aux 0

line vty 0 4

!

!

end

================================

R3#sh run

Building configuration...

Current configuration : 1021 bytes

!

version 12.4

service timestamps debug datetime msec

service timestamps log datetime msec

no service password-encryption

!

hostname R3

!

boot-start-marker

boot-end-marker

!

!

no aaa new-model

memory-size iomem 5

!

!

ip cef

no ip domain lookup

!

!

!

!

!

!

!

interface FastEthernet0/0

no ip address

shutdown

duplex auto

speed auto

!

interface Serial1/0

no ip address

shutdown

serial restart-delay 0

!

interface Serial1/1

no ip address

encapsulation frame-relay

ipv6 address 2001:1:1:11::3/64

serial restart-delay 0

clock rate 64000

frame-relay map ipv6 2001:1:1:11::1 301 broadcast

frame-relay map ipv6 2001:1:1:11::2 301 broadcast

no frame-relay inverse-arp

!

interface Serial1/2

no ip address

shutdown

serial restart-delay 0

!

interface Serial1/3

no ip address

shutdown

serial restart-delay 0

!

ip http server

no ip http secure-server

!

!

!

!

control-plane

!

!

!

line con 0

exec-timeout 0 0

logging synchronous

line aux 0

line vty 0 4

!

!

end