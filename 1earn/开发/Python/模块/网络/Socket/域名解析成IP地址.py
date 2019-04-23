import socket
import re

#将urllist.txt中的每行URL都试图解析成IP地址，保存到iplist.txt。
#socket.gethostbyname(url)方法中的url参数不能带有“http”这样的协议前缀，否则不能解析成IP地址。

def URL2IP():
   for oneurl in urllist.readlines():
	   url=re.sub('@|#|ftp://|https://|http://|moz-extension://|/', '',oneurl)
	   print(url)
	  
	  '''
       try:
           ip =socket.gethostbyname(url)
           print ip
           iplist.writelines(str(ip)+"\n")
       except:
           print "this URL 2 IP ERROR "
	'''

try:
    urllist=open("urllist.txt","r")
    iplist=open("iplist.txt","w")
    URL2IP()
    urllist.close()
    iplist.close()
    print ("complete !")
	
except:
    print ("ERROR !")

	