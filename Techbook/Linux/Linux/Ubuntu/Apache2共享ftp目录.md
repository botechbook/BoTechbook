# Apache2共享ftp目录

Apache2共享ftp目录

Sunday, August 12, 2018

1:33 PM

apt install vsftpd

sed -i 's/anonymous_enable=NO/anonymous_enable=YES/' /etc/vsftpd.conf ;\

sed -i 's/#write_enable=YES/write_enable=YES/' /etc/vsftpd.conf ;\

sed -i 's/#anon_upload_enable=YES/anon_upload_enable=YES/' /etc/vsftpd.conf ;\

sed -i 's/#anon_mkdir_write_enable=YES/anon_mkdir_write_enable=YES/' /etc/vsftpd.conf ;\

echo "anon_other_write_enable=YES" >> /etc/vsftpd.conf ;\

echo "anon_umask=000" >> /etc/vsftpd.conf ;\

mkdir /srv/ftp/public ;\

chown ftp:ftp /srv/ftp/public ;\

systemctl restart vsftpd

apt install apache2

vim /etc/apache2/sites-enabled/000-default.conf

Change "DocumentRoot /var/www/html" to "DocumentRoot /srv/ftp/public"

vim /etc/apache2/apache2.conf

Add following:

<Directory /srv/ftp/public/>

Options Indexes FollowSymLinks

AllowOverride None

Require all granted

</Directory>

systemctl restart apache2