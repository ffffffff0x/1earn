
#coding=utf-8
#-------------------------------------------------------------------------------
# Name:        PortScan
# Purpose:     scan open port in ip
# Python3.4
#-------------------------------------------------------------------------------

print ('''

   _____                                  ____                   __ 
  / ___/  _____  ____ _   ____           / __ \  ____    _____  / /_
  \__ \  / ___/ / __ `/  / __ \         / /_/ / / __ \  / ___/ / __/
 ___/ / / /__  / /_/ /  / / / /        / ____/ / /_/ / / /    / /_  
/____/  \___/  \__,_/  /_/ /_/        /_/      \____/ /_/     \__/  

                          Python3.4                     

''')

import socket
def main():
    ip_start=input('Please Start IP:(default:127.0.0.1)')
    if ip_start=='':
        ip_start='127.0.0.1'
        ip_end='127.0.0.1'
    else:
        ip_end=input('Please End IP:')
        if ip_end=='':
            ip_end=ip_start
        
    s=input('Please Input Port Start:(default All PORT:)')
    if s=='':
        portList=[21, 22, 23, 25, 80, 135, 137, 139, 445, 1433, 1502, 3306, 3389, 8080, 9015]   #常用端口
        #portList =range(1,65534) 所有端口
    else:
        startport=int(s)
        s=input('Please Input End PORT:(default:65535)')
        if s=='':
            endport=65535
        else:
            endport=int(s)
        portList=[i for i in range(startport,endport+1)]


    while 1:
        #ip_start<ip_end
        x1=ip_start.rfind('.');                      
        x2=ip_end.rfind('.')
        if int(ip_start[x1+1:])>int(ip_end[x2+1:]):
            break;
        
        #开始扫描端口
        for port in portList:
            print('Now Scaning %s:%d' %(ip_start,port))
            try:
                sk = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                sk.settimeout(10)
                sk.connect((ip_start,port))
                sk.settimeout(None)
                print('Server %s Port %d Open OK!\n' % (ip_start,port))
                sk.close()

                #结果保存在文件中
                f=open("IP_Port_%s.txt" % ip_start ,'a')
                f.write(ip_start+':'+str(port)+'\n')
                f.close()               
            except Exception:
                print('Server %s Port %d Close!\n' % (ip_start,port))
            
        #更新ip_start
        i=ip_start.rfind('.')
        x=int(ip_start[i+1:])+1
        ip_start=ip_start[:i+1]+str(x)
        
    print('Scan comple, Save In IP_Port.txt')

if __name__ == '__main__':
    main()
