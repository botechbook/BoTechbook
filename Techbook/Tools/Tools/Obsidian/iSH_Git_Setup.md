
# iSH Git setup

## iOS git client setup
- Install iSH onto iOS
- In iSH
   -
	 ```bash
	 apk update
	 apk add git  # install git client
	 cd ~
	 mkdir obsidian
	 mount -t ios . obsidian
	 ```

   - A file picker will show up
   - Choose the folder with your local vault (Choose the folder Obsidian, all the vaults are under this folder)
   - Setup git credential
   
	```shell
	git config --global user.name bofortitude
	
	git config --global user.email bofortitude@gmail.com
	
	git config --global credential.helper store
	
	cat ~/.gitconfig
	
	touch ~/.git-credentials
	chmod 600 ~/.git-credentials
	
	echo "https://bofortitude%40gmail.com:xxxxxxx@github.com" >> ~/.git-credentials
	
	cd ~/obsidian/mahalanobixvault
	git pull
	```

---
## Clone git repo into obsidian

```shell
cd obsidian
rm -rf .obsidian
git clone https://github.com/bofortitude/mahalanobixvault.git

git config --global --add safe.directory /root/obsidian/mahalanobixvault # trust the directory, otherwise it will be blocked.
```

---
## git discard local changes

```shell
git reset --hard
git clean -fxd
```

