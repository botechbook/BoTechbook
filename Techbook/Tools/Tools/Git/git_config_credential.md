---

mindmap-plugin: basic

---

# git config & credential

## Overview
![](git_config_credential/fortiweb_cloud_training-git-credential.drawio_(1).png)

## Git config
- config priority: `local config > global config > system config`
- **local config(project level)**: in git project .git/config
	```bash
	# This is a project level config which is in repo/.git/config
	cd myrepo # go to repo directory
	git config user.email bofei@fortinet.com # change a config
	git config user.email # check this field from local config
	```
- **global config**: `$HOME/.gitconfig` or `$HOME/.config/git/config`
	```bash
	git config --global user.name "Mona Lisa"
	# global level config file is at ~/.gitconfig
    git config --list --global # check all the configs in global level
	```
- **system config**: `/etc/gitconfig`


## Set username & email
```bash
# To configure it in project level:
# cd to git project dir, perform the following without --global
git config --global user.name "Bo Fei"
git config --global user.email "bofei@fortinet.com"
```

## Git HTTPS credential
- `url = https://` in `[remote origin]` section of `config` file
- Set HTTPS credential helper to store
	```bash
	# This is to set the credential helper to "store" in project level
	git config --global credential.helper store # only work for HTTPS URL
	git pull # CLI will ask your password
	```

- `credential.helper` types
	- `sotre`: plain text type, easy to setup, not secure
	- `manager`
- `store` type credential file: `~/.git-credentials`
- Full example
	```bash
	git config --global user.name bofei
	git config --global user.email bofei@fortinet.com
	
	git config --global credential.helper store
	
	cat ~/.gitconfig
	
	touch ~/.git-credentials
	chmod 600 ~/.git-credentials
	
	echo "https://bofei%40fortinet.com:xxxxxxx@gitlab.com" >> ~/.git-credentials
	
	cd ~/code/gitproject
	git pull
	```

## Git SSH credential settings
- `url = git@` in `[remote origin]` section of `config` file
- `~/ssh/config` should be `chmod 600`
	```bash
	chmod ~/ssh/config
	```
- Option 1 (easiest way): `~/.ssh/config`
	```
	Host github.com
	User git
	Hostname github.com
	IdentityFile ~/.ssh/id_rsa
	```
- Option 2: `ssh-agent`
	```
	$ ssh-agent sh -c 'ssh-add ~/.ssh/id_rsa; git fetch user@host'
	
	```
- Option 3: `GIT_SSH_COMMAND`      
	```
	$ GIT_SSH_COMMAND='ssh -i ~/.ssh/id_rsa -o UserKnownHostsFile=/dev/null -o StrictHostKeyChecking=no' \
	git clone user@host
	
	```
- Option 4: `GIT_SSH`
	```
	$ echo 'ssh -i ~/.ssh/id_rsa -o UserKnownHostsFile=/dev/null -o StrictHostKeyChecking=no $*' > ssh
	$ chmod +x ssh
	$ GIT_TRACE=1 GIT_SSH='./ssh' git clone user@host
	
	```
