# Ubuntu tftpd

Ubuntu tftpd

Thursday, August 6, 2020

10:45 AM

apt install tftp-hpa tftpd-hpa -y
sed -i 's/TFTP_OPTIONS="--secure"/TFTP_OPTIONS="-l -s -c"/' /etc/default/tftpd-hpa
chmod 777 /var/lib/tftpboot