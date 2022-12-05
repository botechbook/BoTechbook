# Conda

## Create env

```bash
# --no-default-packages means not installing python packages from default env
conda create --name myenv python --no-default-packages

# or
# Specify the python version
conda create --name myenv python=3.10

# or
# In this way, it doesn't even install python into the environment (inherit base env)
conda create --name myenv --no-default-packages
```

## List envs

```bash
conda env list

#or 

conda info --env
```

## Activate & Deactivate env

```bash
# activate the env myenv
conda activate myenv

# in env myenv
conda deactivate
```

## Remove envs

```bash
# must deactivate the env first
conda env remove -n myenv
```

## Check packages of the env

```bash
# check packages installed into the env
# if the -n arg is not specified, it'll check the "base" env
conda list -n mydev 
```

## Install Python packages into the env

- Using pip command to install Python package (recommended)

```bash
# activate the env
conda activate myenv

# install the desired packages using pip command
pip install requests

(myenv) bofei@bofei-mac bin % conda list -n myenv
# packages in environment at /Users/bofei/miniconda3/envs/myenv:
#
# Name                    Version                   Build  Channel
bzip2                     1.0.8                h1de35cc_0  
charset-normalizer        2.1.1                    pypi_0    pypi
idna                      3.3                      pypi_0    pypi
requests                  2.28.1                   pypi_0    pypi
urllib3                   1.26.12                  pypi_0    pypi

(myenv) bofei@bofei-mac bin %       
(myenv) bofei@bofei-mac bin % conda env export -n myenv
name: myenv
channels:
  - defaults
dependencies:
  - bzip2=1.0.8=h1de35cc_0
  - pip:
    - charset-normalizer==2.1.1
    - idna==3.3
    - requests==2.28.1
    - urllib3==1.26.12
prefix: /Users/bofei/miniconda3/envs/myenv
```

- Using conda command to install Python package

```bash
# use conda command install the python package directly
conda install -n myenv requests

(base) bofei@bofei-mac fakehome % conda list -n myenv
# packages in environment at /Users/bofei/miniconda3/envs/myenv:
#
# Name                    Version                   Build  Channel
brotlipy                  0.7.0           py310hca72f7f_1002  
bzip2                     1.0.8                h1de35cc_0  
ca-certificates           2022.07.19           hecd8cb5_0  
certifi                   2022.6.15       py310hecd8cb5_0  
cffi                      1.15.1          py310hc55c11b_0  
charset-normalizer        2.0.4              pyhd3eb1b0_0  
cryptography              37.0.1          py310hf6deb26_0  
idna                      3.3                pyhd3eb1b0_0  
libcxx                    14.0.6               h9765a3e_0  
libffi                    3.3                  hb1e8313_2  
ncurses                   6.3                  hca72f7f_3  
openssl                   1.1.1q               hca72f7f_0  
pip                       22.1.2          py310hecd8cb5_0  
pycparser                 2.21               pyhd3eb1b0_0  
pyopenssl                 22.0.0             pyhd3eb1b0_0  
pysocks                   1.7.1           py310hecd8cb5_0  
python                    3.10.4               hdfd78df_0  
readline                  8.1.2                hca72f7f_1  
**requests                  2.28.1          py310hecd8cb5_0**  
setuptools                63.4.1          py310hecd8cb5_0  
sqlite                    3.39.2               h707629a_0  
tk                        8.6.12               h5d9f67b_0  
tzdata                    2022a                hda174b7_0  
urllib3                   1.26.11         py310hecd8cb5_0  
wheel                     0.37.1             pyhd3eb1b0_0  
xz                        5.2.5                hca72f7f_1  
zlib                      1.2.12               h4dc903c_3

(base) bofei@bofei-mac fakehome % conda env export -n myenv
name: myenv
channels:
  - defaults
dependencies:
  - brotlipy=0.7.0=py310hca72f7f_1002
  - bzip2=1.0.8=h1de35cc_0
  - ca-certificates=2022.07.19=hecd8cb5_0
  - certifi=2022.6.15=py310hecd8cb5_0
  - cffi=1.15.1=py310hc55c11b_0
  - charset-normalizer=2.0.4=pyhd3eb1b0_0
  - cryptography=37.0.1=py310hf6deb26_0
  - idna=3.3=pyhd3eb1b0_0
  - libcxx=14.0.6=h9765a3e_0
  - libffi=3.3=hb1e8313_2
  - ncurses=6.3=hca72f7f_3
  - openssl=1.1.1q=hca72f7f_0
  - pip=22.1.2=py310hecd8cb5_0
  - pycparser=2.21=pyhd3eb1b0_0
  - pyopenssl=22.0.0=pyhd3eb1b0_0
  - pysocks=1.7.1=py310hecd8cb5_0
  - python=3.10.4=hdfd78df_0
  - readline=8.1.2=hca72f7f_1
  - requests=2.28.1=py310hecd8cb5_0
  - setuptools=63.4.1=py310hecd8cb5_0
  - sqlite=3.39.2=h707629a_0
  - tk=8.6.12=h5d9f67b_0
  - tzdata=2022a=hda174b7_0
  - urllib3=1.26.11=py310hecd8cb5_0
  - wheel=0.37.1=pyhd3eb1b0_0
  - xz=5.2.5=hca72f7f_1
  - zlib=1.2.12=h4dc903c_3
prefix: /Users/bofei/miniconda3/envs/myenv
```

## Install other packages into the env

> Find a desired package on website:
> [anaconda](https://anaconda.org/)
> 

```bash
# -c is to specify channel which is like library source
conda install -c conda-forge terraform -n myenv
conda install -c conda-forge awscli -n myenv

# search the other available version of the package
conda search -c conda-forge terraform
```

## Set environment variables to the env

```bash
conda env config vars set HOME=/Users/bofei/fakehome -n myenv
conda env config vars set AWS_ACCESS_KEY_ID=AKIAIOSFODNN7EXAMPLE -n myenv
conda env config vars set AWS_SECRET_ACCESS_KEY=wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY -n myenv
conda env config vars set AWS_DEFAULT_REGION=us-east-1 -n myenv


newHome="/Users/bofei/fakehome"
homeDirs=".ssh .conda .config .gitconfig .git-credentials" 
for i in $homeDirs; do cp -rf ~/$i $newHome ; done
```

## Save env

```bash
conda env export -t myenv | grep -v "^prefix: " > environment.yml

# exclude the build info of the dependencies
conda env export -t myenv --no-builds | grep -v "^prefix: " > environment.yml
```

## Create env from an env YAML file

```bash
# You probably need to modify the environment.yml for name, prefix, vars
conda env create -f environment.yml
```