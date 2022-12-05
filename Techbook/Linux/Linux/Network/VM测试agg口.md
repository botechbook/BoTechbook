# VM测试agg口

VM测试agg口

Wednesday, June 13, 2018

11:44 AM

如果只是需要agg口对联，直接在agg口上面起IP地址通信的话，无论是用docker还是直接用虚拟机，只要两个口分别处于不同的vlan当中就可以通信了

如果需要在agg口之上起vlan口，那么必须要使用两个不相关的vswitch，分别在上面起trunk，然后连到两个口上，这样就可以互通了