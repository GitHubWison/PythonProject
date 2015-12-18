# coding=utf-8
import smtplib,time
from email.mime.text import MIMEText
# 发送邮件的类
class SendEmail:
    # 发件人的信息:包含：SMTPserver，登录邮箱的用户名：UserName,登录邮箱的密码:PassWord，发件人的邮箱地址：SenderMailAdd
    sender_msg = {}
    # 收件人的信息:包含：收件人的地址：GetterMailAdd
    getter_msg = {}
    # 发送的内容:包含：邮件的标题:MailTitle,邮件的正文：Body
    email_msg = {}
    def __init__(self,sender_msg,getter_msg,email_msg):
        self.sender_msg = sender_msg
        self.getter_msg = getter_msg
        self.email_msg = email_msg

    def send_email(self):
        message = MIMEText(self.email_msg['Body'], 'text', 'utf-8')
        message['Subject'] = self.email_msg['MailTitle']
        message['From'] = self.sender_msg['SenderMailAdd']
        message['To'] = self.getter_msg['GetterMailAdd']
        msg = message.as_string()



        sm = smtplib.SMTP(self.sender_msg['SMTPserver'], timeout=20)
        sm.set_debuglevel(1)
        sm.ehlo()
        sm.starttls()
        sm.ehlo()
        sm.login(self.sender_msg['UserName'], self.sender_msg['PassWord'])

        sm.sendmail(self.sender_msg['SenderMailAdd'], self.getter_msg['GetterMailAdd'], msg)
        time.sleep(5)
        sm.quit()