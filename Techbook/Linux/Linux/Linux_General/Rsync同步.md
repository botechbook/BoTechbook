# Rsync 同步

Rsync 同步

Tuesday, January 21, 2020

2:59 PM

apt install rsync

apt install sshpass

sshpass -p fortinet rsync -avz --delete -e "ssh -o StrictHostKeyChecking=no" root@172.30.104.2:/root/deep_directory_server/db.sqlite3 /home/bofei/dev/fadc_autotest/dist/deep_directory_server/db_backup/

You have to login the remote machine one time manually to confirm the session, don't forget to remove the ~/.ssh/known_host once the remote machine reinstalls the OS

sshpass -p remote_password rsync -avz --delete -e ssh remote_user@remote_host:/remote/dir /local/dir

=======================================

配置rsync+ssh+密码登录

[Leave a reply](https://www.coder4.com/archives/2323#respond)

原创，转载请注明：[配置rsync+ssh+密码登录](http://www.coder4.com/archives/2323)

配置rsync+ssh+密码登录 – rsync over SSH using sshpass

rsync是Linux下非常好用的开源工具。

rsync的更新是差量的，即有变化的文件才更新，最大程度的减少了数据传输量和时间。

但是配置起来比较繁琐。即需要rsyncd和rsync共同配置。

实际上，rsync是支持ssh协议的，只要走ssh协议就可以了。走ssh协议速度稍慢一些，但是配置非常简单。

同时，ssh协议的缺点就是，密码问题不好搞定，因为需要非交互模式，我们使用sshpass来避免配置密钥免登录。

1、安装rsync和sshpass

安装rsync。

我们走的是rsync over ssh协议，因此不需要在服务器端安装rsyncd，只要服务器开了ssh就行。

yum install rsync

基于Debian的发行版一般都有sshpass，如果你的CentOS没有，直接去下载，编译一个，无依赖，非常简单.

sshpass开源项目：http://sourceforge.net/projects/sshpass/files/

yum install sshpass

2、一次更新

在rsync over ssh的基础上，我们采用sshpass解决非交互模式输入密码的问题。

传统做法是：使用密钥，但是很麻烦。

我们先得成功登录一次remotehost，之后就可以使用sshpass了。

ssh remote_user@remote_host

特别提醒：如果今后远程主机重装系统，或者换了机器，一定要删除本地~/.ssh/known_host，否则是会无法登录的。

下面测试rsync over ssh，密码登录。

sshpass -p remote_password rsync -avz --delete -e ssh remote_user@remote_host:/remote/dir /local/dir

上面的命令中:

remote_use/remote_password是远程的密码

- avz是打包传送、显示明细、压缩
- e ssh是关键，即over ssh

我们要从远程同步到本地

/remote/dir是远程服务器路径

/local/dir是本地服务器路径

原创，转载请注明：[配置rsync+ssh+密码登录](http://www.coder4.com/archives/2323)

3、加入cron job

在上一步中，我们已经完成了一步的同步，下面我们要加入cron job

不同发行版本中，cron job的用法有细微差别，下面以Turbo Linux为例，理论上它应该适用于所有同源于RHEL的发行版本。

首先，准备一下要执行的脚本，将第2步中，下述内容写入到rsync-xx，注意符合cron job的命名规则

vim rsync-xx
sshpass -p remote_password rsync -avz --delete -e ssh remote_user@remote_host:/remote/dir /local/dir

安装cron

sudo yum install vixie-cron

启动crond服务，注意添加crond到开机启动服务

sudo /etc/init.d/crond start

我们要每3分钟检查一次，如果你准备又多个同步脚本，建议采用run-parts的方案1,如果只有一两个，可以直接在crontab写,即方案2

[方案1]

使用run-parts

#创建cron.min，把要执行的N个脚本拷贝过来
sudo mkdir cron.min
cp rsync-xx ./

#更改cron table
vim /etc/crontab
*/3 * * * * root run-parts /etc/cron.min

[方案2]

直接写cron table

#假设我们的脚本位于/path/cron.min
vim /etc/crontab
*/3 * * * * /path/cron.min

如果没有问题的的话，就会每隔三分钟更新了！

From <[https://www.coder4.com/archives/2323](https://www.coder4.com/archives/2323)>