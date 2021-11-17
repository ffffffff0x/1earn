# flask安全

---

## session伪造

flask-session 的三部分为 json->zlib->base64后的源字符串.时间戳.hmac签名信息

**相关文章**

- [flask session伪造admin身份](https://blog.csdn.net/since_2020/article/details/119543172)

**相关工具**

- [noraj/flask-session-cookie-manager](https://github.com/noraj/flask-session-cookie-manager)
    ```bash
    python3 flask_session_cookie_manager3.py decode -s "thisiskey" -c "eyJ1c2VybmFtZSI6eyIgYiI6IllXUnRhVzQ9In19.YWfurA.sHD-E9MuX4QZJQ4cU07WYykbJZU" # 解密
    python3 flask_session_cookie_manager3.py encode -s "thisiskey" -t "{'username': b'admin'}"  # 加密
    ```

**writeup**
- [[HCTF 2018] admin](https://darkwing.moe/2019/11/04/HCTF-2018-admin/)
- [BUUCTF N1BOOK [第一章 web入门]](https://blog.csdn.net/RABCDXB/article/details/115189884)
