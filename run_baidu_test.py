from HTMLTestRunner import HTMLTestRunner
from email.mime.text import MIMEText
from email.header import Header
import smtplib
import unittest
import time
import os,sys
import win32api

def send_mail(file_new):
    f=open(file_new,'rb')
    mail_body=f.read()
    f.close()

    msg=MIMEText(mail_body,'html','utf-8')
    msg['Subject']=Header("百度自动化测试报告_Qingbo",'utf-8')

    smtp=smtplib.SMTP()
    smtp.connect("smtp.163.com")
    smtp.login("tianliang657@163.com","Password")
    smtp.sendmail("tianliang657@163.com","tianliang657@163.com",msg.as_string())
    smtp.quit()
    print("email has send out !")

def new_report(testreport):
    lists=os.listdir(testreport)
    lists.sort(key=lambda fn:os.path.getmtime(testreport + "\\" + fn))
    file_new=os.path.join(testreport,lists[-1])
    print(file_new)
    return file_new

if __name__=="__main__":
    now=time.strftime("%Y-%m-%d %H_%M_%S")
    #filename='./Baidu_test/report/' + now + 'result.html'
    filename='./Baidu_test/report/result.html'
    fp=open(filename,'wb')
    runner=HTMLTestRunner(stream=fp,title='百度测试_Qingbo',
                          description='环境：XOS 浏览器：chrome')
    discover=unittest.defaultTestLoader.discover('./Baidu_test/test_case',
                                                 pattern='*_sta.py')
    runner.run(discover)
    fp.close()
    #file_path=new_report('./Baidu_test/report/')
    #send_mail(file_path)
    exit()
    win32api.keybd_event(13,0,0,0)
    win32api.keybd_event(13,0,KEYEVENT_KEYUP,0)
