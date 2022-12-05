# nfs服务

nfs服务

Monday, April 27, 2020

9:19 AM

> Ubuntu 18.04
> 
- NFSv4 client
sudo apt-get install nfs-common
- NFSv4 server
sudo apt-get install nfs-kernel-server

> 
> 
> 
> systemctl restart nfs-kernel-server
> 
> systemctl enable nfs-kernel-server
> 
> Server:
> 
> #Edit /etc/exports
> 
> /srv/ftp/public/auto_test *(rw,fsid=0,sync,no_wdelay,insecure_locks,no_root_squash)
> 
> Client:
> 
> mount -t nfs4 172.30.104.5:/srv/ftp/public/auto_test/file_store /nfsdata/data5
> 
> ==================================================================================
> 
> /nfsdata 192.168.100.101(rw,fsid=0,sync,no_wdelay,insecure_locks,no_root_squash)
> 
> [https://www.cnblogs.com/Dy1an/p/10536093.html](https://www.cnblogs.com/Dy1an/p/10536093.html)
>