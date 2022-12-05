
# open welcome and help again

再次打开welcome和帮助


![open%20welcome%20and%20help%20again%2083f1b87e58f547b7b51c703d2c79803c/image1.png](RED%20editor/open%20welcome%20and%20help%20again/image1.png)

![open%20welcome%20and%20help%20again%2083f1b87e58f547b7b51c703d2c79803c/image2.png](RED%20editor/open%20welcome%20and%20help%20again/image2.png)

---
# project structure

要打开的project里面必须包含 red.xml

---
# recover RED initial


![recover%20RED%20initial%200949dc95270b4bca901d934ab6a012d1/image1.png](RED%20editor/recover%20RED%20initial/image1.png)

并且删除默认workspace下面的.metadata

还有project下面的.project文件

---
# RED ignore errors

![RED%20ignore%20errors%20756730a630364bcdb7b07e703f0e9b40/image1.png](RED%20editor/RED%20ignore%20errors/image1.png)


---
# RED introduction

RED introduction

Friday, August 2, 2019

2:47 PM

1. RIDE review:

> https://github.com/robotframework/RIDE
> 
> 
> Forked:
> 
> [https://github.com/HelioGuilherme66/RIDE](https://github.com/HelioGuilherme66/RIDE)
> 
> Advantage:
> 
> (1) Easy to use especially for starter
> 
> (2) Educate new user to get used to robot framework
> 
> (3) first impression of robot framework
> 
> RIDE disadvantage:
> 
> (1) No Python3 supported officially (Helio forked and maintained RIDE, bug fixes limited)
> 
> (2) poor performance
> 
> (3) no officially maintained (only Helio keeps contributing)
> 
1. RED review

> RED advantage:
> 
> 
> (1) Nokia official developing
> 
> (2) support all RIDE functions
> 
> (3) all python version supported
> 
> (4) continuous new features integrated (robot itself & robot framework new feature supported)
> 
> (5) syntax analysis
> 
> (6) library spec auto generated
> 
> (7) high performance
> 
> (8) developing robot case & python code in one place
> 
> (9) more advanced features (case running manager, listener server)
> 
> (10) all eclipse advantage
> 
> RED disadvantage:
> 
> (1) need time to get used to
> 
> (2) memory leak
> 
> (3) all eclipse disadvantage
> 
> Why not others:
> 
> (1) no continuous contribution
> 
> (2) no test case level control
> 
> (3) limited features supported
> 
1. Get started

> () Open RED, open the project "ADC_Test" , optional open "Libraries" as well
> 
> 
> () Open RED, then open the "ADC_Test", right click the "ADC_Test"->Robot Framework -> Robot Nature, then the red.xml file will be generated under "ADC_Test"
> 
> () Check the "Use local settings for this project"
> 
> () set the pythonpath in red.xml, like what you did in RIDE:
> 
> C:\Users\Administrator\Desktop\Current_Build\Libraries, C:\Users\Administrator\Desktop\Current_Build\ADC_Test
> 
> () Edit red.xml file, find "Variables" tab, add the variable files under ADC_Test/red_config_backup/red_robot_variables.py
> 
> () Right click "ADC_Test" -> Robot Framework -> Automatically discover and add libraries to red.xml
> 
> () Right click "ADC_Test" -> Robot Framework -> Revalidate
> 
> () go to Window->Preferences->Robot Framework->Launching->Default Launch Configurations,
> 
> ()
> 
> ()

---
# RED reload referenced libraries


![RED%20reload%20referenced%20libraries%20a701ac2aed0b47bb896aba3ea656d840/image1.png](RED%20editor/RED%20reload%20referenced%20libraries/image1.png)


---
# RIDE arguments

- -argumentfile C:\Users\Administrator\Desktop\Current_Build\argumentfile.txt -v lab:60Flab_01 -v repeat:1 -v image_server:10.106.4.200 -v testbuild:latest

---

# Robot parameter


![Robot%20parameter%20be020cdd8a2546f5800d987750228c1c/image1.png](RED%20editor/Robot%20parameter/image1.png)

---
# Robot revalidate

Ctrl + F5 or

![Robot%20revalidate%20dc8031418bc448b3bd81fc3733c597af/image1.png](RED%20editor/Robot%20revalidate/image1.png)

---
# Robot run parameter

-variable cloud_test_env:cloud_env_aws_2.yaml --loglevel DEBUG


---
# save and reset layout

保存和重置layout


![save%20and%20reset%20layout%20798c84d8ff93457a9fd6b877ee22fb68/image1.png](RED%20editor/save%20and%20reset%20layout/image1.png)

![save%20and%20reset%20layout%20798c84d8ff93457a9fd6b877ee22fb68/image2.png](RED%20editor/save%20and%20reset%20layout/image2.png)

---
# switch view


![switch%20view%20ab5d08fae1f74f39b105f7c7f0734115/image1.png](RED%20editor/switch%20view/image1.png)

---
# Test Case options

![Test%20Case%20options%20012dcb06c2e04dadbb0b326ce7ef43e1/image1.png](RED%20editor/Test%20Case%20options/image1.png)

799590

[Documentation] Summary: Verify if the hard disk failure will be detected every 1 hour and after getting failure it can trigg

... Script Writer:

[Tags] medium v4.8

---
# Workspace

Workspace

Friday, September 7, 2018

2:21 PM

每次打开RED(Eclipse)，设置的默认workspace如果不存在都会自动创建这个目录，并且下面会有一个隐藏的目录.metadata ，里面包含一些eclipse的文件

![Workspace%20ef18cfe033b24aac9a22da7caee7ae6f/image1.png](RED%20editor/Workspace/image1.png)



