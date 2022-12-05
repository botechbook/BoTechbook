# Freeradius

Freeradius

2014年10月24日

15:31

1. apt-get install freeradius # install freeradius

2. #vim /etc/freeradius/clients.conf

添加

client 0.0.0.0/0 {

secret = fortinet

shortname = MyNasClient

nastype = Ubuntu-IPv4

}

client ::/0 {

secret = fortinet

shortname = MyNasClient

nastype = Ubuntu-IPv6

}

3. #vim /etc/freeradius/users, then add:

user10 Cleartext-Password:=pass10

Reply-Message=10.0.10.15

#After this, authentication response will take "10.0.10.15"

4. vim /etc/freeradius/acct_users

Add this:

DEFAULT

Reply-Message=10.0.10.15