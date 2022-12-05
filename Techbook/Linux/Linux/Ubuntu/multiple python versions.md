# multiple python versions

[](https://linuxconfig.org/how-to-change-from-default-to-alternative-python-version-on-debian-linux)

```bash
###########################################################################
# install python3.9
add-apt-repository ppa:deadsnakes/ppa
apt update
apt install python3.9 -y
apt install python3.9-distutils -y

###########################################################################
# python package location
# python3.9
#['', '/usr/lib/python39.zip', '/usr/lib/python3.9', '/usr/lib/python3.9/lib-dynload', '/home/jenkins/.local/lib/python3.9/site-packages', '/usr/local/lib/python3.9/dist-packages', '/usr/lib/python3/dist-packages']

# python3.6
# ['', '/usr/lib/python36.zip', '/usr/lib/python3.6', '/usr/lib/python3.6/lib-dynload', '/home/jenkins/.local/lib/python3.6/site-packages', '/usr/local/lib/python3.6/dist-packages', '/usr/lib/python3/dist-packages']

###########################################################################
# install pip3 for python3.9
curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py
python3.9 get-pip.py
# After installing python3.9 pip, the pip3 command will become python3.9 version by default
# pip3 install location is /usr/lib/python3/dist-packages by default, so the previously installed python packages
# might be conflict, resolve: 
python3.9 -m pip uninstall requests
python3.9 -m pip install requests boto3
python3.6 -m pip install requests boto3 # this will be installed to /usr/local/lib/python3.6/dist-packages

# pip install for different version python, install
python3.9 -m pip install requests boto3
python3.6 -m pip install requests boto3

###########################################################################
# the end 1 & 2 are priority, the higher number value, the higher priority
update-alternatives --install /usr/bin/python3 python3 /usr/bin/python3.9 1
update-alternatives --install /usr/bin/python3 python3 /usr/bin/python3.6 2
update-alternatives --list python3

###########################################################################
# switch python version
root@worker22:~# update-alternatives --config python3
There are 2 choices for the alternative python3 (providing /usr/bin/python3).

Selection Path Priority Status
------------------------------------------------------------
0 /usr/bin/python3.6 2 auto mode
1 /usr/bin/python3.6 2 manual mode
* 2 /usr/bin/python3.9 1 manual mode

Press <enter> to keep the current choice[*], or type selection number: 1
update-alternatives: using /usr/bin/python3.6 to provide /usr/bin/python3 (python3) in manual mode
```