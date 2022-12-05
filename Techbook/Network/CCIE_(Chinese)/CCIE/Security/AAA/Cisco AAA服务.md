# Cisco AAA服务

Cisco AAA服务

2011年8月2日

21:43

Cisco AAA服务

本章介绍Cisco Secure ACS产品以及Cisco路由器和防火墙中的AAA服务，主要包含以下几个部分：

1、Cisco Secure ACS产品介绍

2、Cisco Secure ACS安装以及基本配置

3、AAA概述

4、配置AAA认证

5、配置AAA授权

6、配置AAA审计

7、AAA高级配置及应用

Cisco Secure ACS产品介绍

Cisco Secure ACS是一个用来控制对网络的访问的网络安全软件，它可以对用户进行认证、授权和审计。

Cisco Secure ACS分为Cisco Secure ACS for windows和Cisco Secure ACS for Unix两个版本，下表是两个版本所支持的操作系统：

![Cisco%20AAA%E6%9C%8D%E5%8A%A1%2034799a0b0abe4d16ad9539029c8efd6c/image1.png](Cisco%20AAA服务/image1.png)

Cisco Secure ACS管理起来十分简单，用户可以使用web浏览器完成对它的所有管理，本章只介绍Cisco Secure ACS for windows version 3.3的管理。

Cisco Secure ACS安装及基本配置

Cisco Secure ACS安装很简单，本节讲述Cisco Secure ACS for windows的安装流程、注意事项以及ACS的基本配置。

Cisco Secure ACS for windows的安装过程如下：

步骤1、检查并调整计算机硬件配置，使其满足以下要求： Pentium Ⅲ 550MHz以上 256M内存 250M以上的剩余硬盘空间

步骤2、检查windows配置，安装Java run time（JRE）。（JRE的最新版本可以去[www.sun.com](http://www.sun.com/)上下载）

步骤3、检查服务器到Cisco设备的网络连接。

步骤4、插入Cisco Secure ACS for windows 光盘，点击“Install”开始安装，然后按照windows的提示一步步地完成安装。