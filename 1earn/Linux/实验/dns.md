www.abc.com 解析为 192.168.192.1
192.168.192.1 解析为 www.abc.com

ftp.abc.com 解析为 192.168.192.2
192.168.192.2 解析为 ftp.abc.com

```vim
vim /etc/named.rfc1912.zones
zone "abc.com." IN {        
        type master;
        file "z";
        allow-update { none; };
};

zone "192.168.192.in-addr.arpa" IN {       
        type master;
        file "f";
        allow-update { none; };
};

```
>cd /var/named/
cp named.localhost z
cp named.loopback f

>chown named z
chown named f
	
```vim
vim /var/named/z
	$TTL 1D
	@      IN SOA  @ rname.invalid. (
                                        	0      ; serial
                                        	1D      ; refresh
                                        	1H      ; retry
                                        	1W      ; expire
                                        	3H )    ; minimum
	       	NS     @
       		A      127.0.0.1
	    	AAAA   ::1
	www    	A      192.168.192.1
	ftp    	A      192.168.192.2
	

vim /var/named/f
	$TTL 1D
	@ 		IN SOA  @ rname.invalid. (
    	                                    0 ; serial
                                        	1D ; refresh
                                        	1H ; retry
                                        	1W ; expire
                                        	3H ) ; minimum
        	NS	@
        	A 	127.0.0.1
        	AAAA	::1
        	PTR 	localhost.

	1 PTR www.abc.com.
	2 PTR ftp.abc.com.
	

systemctl restart named

```
