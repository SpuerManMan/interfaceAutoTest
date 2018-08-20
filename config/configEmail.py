#coding=utf-8

from readConfig import ReadConfig as RC
from log import *
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib
import threading
import os
import zipfile

class Email:

    sender = RC.get_Email('sender')
    receiver = RC.get_Email('receiver')
    smtpserver = RC.get_Email('smtpserver')
    username = RC.get_Email('username')
    password = RC.get_Email('password')
    emflag = RC.get_Email('emflag')
    subject = '[AutomationTest]接口自动化测试报告通知'


    def __init__(self):
        self.logpath = MyLog.get_log()
        self.log = MyLog.get_log()
        self.logger = self.log.get_logger()
        self.message=MIMEMultipart()
        self.retult_path = self.logpath.get_result_path()
        self.zip_file=os.path.join(readConfig.proDir,'testFile','test.zip')
    # 设置邮件标题
    def set_header(self):
        self.message['subject']=self.subject
        self.message['From']=self.sender
        self.message['To']=self.receiver

    #设置邮件发送内容
    def set_content(self):
        try:
            with open(os.path.join(readConfig.proDir,'testFile','mail.txt'))as f:
                content=f.read()
        except Exception as ex:
            self.logger.info(str(ex))
        finally:
            f.close()
            content_plain=MIMEText(content,'html','utf-8')
            self.message.attach(content_plain)
    def set_file(self):
         with zipfile.ZipFile(self.zip_file,'w',zipfile.ZIP_DEFLATED)as zipf:
             if os.path.isdir(self.retult_path):
                for file in os.listdir(self.retult_path):
                    zipf.write(os.path.join(self.retult_path,file),'/report/' + os.path.basename(file))
             zipf.close()
         att2=MIMEText(open(self.zip_file,'rb').read(),'base64','utf-8')
         att2["Content-Type"] = 'application/octet-stream'
         att2["Content-Disposition"] = 'attachment; filename="test.zip"'
         self.message.attach(att2)

    def send_Email(self):
        try:

            self.logger.info('设置邮件主题!')
            self.set_header()
            self.logger.info('读取邮件内容！')
            self.set_content()
            self.logger.info('压缩附件！')
            self.set_file()
            self.logger.info('连接邮箱......')
            stmp=smtplib.SMTP_SSL(self.smtpserver,465)
            self.logger.info('进行邮件登录.....')
            stmp.login(self.username,self.password)
            self.logger.info('开始发送邮件！')
            stmp.sendmail(self.sender,self.receiver,self.message.as_string())
            stmp.quit()
            self.logger.info('邮件发送成功！')
        except Exception as ex:
            self.logger.info(str(ex))
            raise ('邮件发送失败！')


class MyEmail:
    email=None
    mutx=threading.Lock()

    def __init__(self):
        pass
    @staticmethod
    def get_email():

        if MyEmail.email is None:
            MyEmail.mutx.acquire()
            try:
                MyEmail.email=Email()
            except Exception as ex:
                print(str(ex))
            finally:
              MyEmail.mutx.release()
        return MyEmail.email

if __name__=='__main__':
    myEmail=MyEmail.get_email()
    myEmail.send_Email()