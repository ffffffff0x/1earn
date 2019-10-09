# Nginx

---

**安装**
- **源代码编译安装**

  自己下载好包 https://nginx.org/en/download.html，传到服务器上，这里以1.14.2 举例

  ```bash
  tar -zxvf nginx-1.14.2.tar.gz
  cd nginx-1.14.2/
  ./configure
  make
  make install
  cd /usr/local/nginx/sbin
  ./nginx
  ```

  注:源代码安装你的默认目录在 /usr/local/nginx 下,配置文件在 conf/ 中，不要搞错了

```bash
firewall-cmd --permanent --zone=public --add-service=http
firewall-cmd --reload
```

**反向代理**

反向代理（Reverse Proxy）方式是指以代理服务器来接受 internet 上的连接请求，然后将请求转发给内部网络上的服务器，并将从服务器上得到的结果返回给 internet 上请求连接的客户端，此时代理服务器对外就表现为一个反向代理服务器。

```vim
cd /usr/local/nginx/conf
vim nginx.conf


server {
    #侦听的80端口
    listen       80;
    server_name  localhost;

    location / {

        proxy_pass   http://127.0.0.1:81;    #在这里设置一个代理
        #以下是一些反向代理的配置可删除
        proxy_redirect             off;
        #后端的Web服务器可以通过X-Forwarded-For获取用户真实IP
        proxy_set_header           Host $host;
        proxy_set_header           X-Real-IP $remote_addr;
        proxy_set_header           X-Forwarded-For $proxy_add_x_forwarded_for;
        client_max_body_size       10m; #允许客户端请求的最大单文件字节数
        client_body_buffer_size    128k; #缓冲区代理缓冲用户端请求的最大字节数
        proxy_connect_timeout      300; #nginx跟后端服务器连接超时时间(代理连接超时)
        proxy_send_timeout         300; #后端服务器数据回传时间(代理发送超时)
        proxy_read_timeout         300; #连接成功后，后端服务器响应时间(代理接收超时)
        proxy_buffer_size          4k; #设置代理服务器（nginx）保存用户头信息的缓冲区大小
        proxy_buffers              4 32k; #proxy_buffers缓冲区，网页平均在32k以下的话，这样设置
        proxy_busy_buffers_size    64k; #高负荷下缓冲大小（proxy_buffers*2）
        proxy_temp_file_write_size 64k; #设定缓存文件夹大小，大于这个值，将从upstream服务器传
    }
}
```

