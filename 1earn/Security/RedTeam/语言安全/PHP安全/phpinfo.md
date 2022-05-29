# phpinfo

---

**相关文章**
- [phpinfo 可以告诉我们什么](http://zeroyu.xyz/2018/11/13/what-phpinfo-can-tell-we/)
- [PHPINFO 中的重要信息](https://www.k0rz3n.com/2019/02/12/PHPINFO%20%E4%B8%AD%E7%9A%84%E9%87%8D%E8%A6%81%E4%BF%A1%E6%81%AF/)
- [amazing phpinfo() ](https://skysec.top/2018/04/04/amazing-phpinfo/)
- [phpinfo 中值得注意的信息](https://seaii-blog.com/index.php/2017/10/25/73.html)
- [php中函数禁用绕过的原理与利用](https://mp.weixin.qq.com/s/_L379eq0kufu3CCHN1DdkA)

**相关工具**
- [proudwind/phpinfo_scanner](https://github.com/proudwind/phpinfo_scanner) - 抓取 phpinfo 重要信息 - 我这里运行报错,解决方法是把15行的3个 nth-child 改为 nth-of-type

---

## 版本号

最直观的就是php版本号（虽然版本号有时候会在响应头中出现）

找相应版本存在的漏洞

---

## DOCUMENT_ROOT

取得网站当前路径

---

## disable_functions

disable_functions 顾名思义函数禁用

如一些ctf题会把disable设置的极其恶心，这里要使用一些 bypass 的技巧

---

## open_basedir

该配置限制了当前 php 程序所能访问到的路径

---

## opcache

如果使用了opcache，那么可能达成getshell，但需要存在文件上传的点
- https://www.cnblogs.com/xhds/p/13239331.html

---

## allow_url_include

文件包含相关

---

## allow_url_fopen

文件包含相关

---

## short_open_tag

短标签

---

## Server API

是否可用 PHP-FPM 绕过 disable_function
