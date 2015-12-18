# coding=utf-8
# 发邮件的
import SendEmail
ss = 'asfasd上课的罚款收到了；阿萨德'
sender_msg = {
    'SMTPserver': 'smtp.163.com',
    'UserName': '15995448871@163.com',
    'PassWord': 'nwljhxhstqinoiuw',
    'SenderMailAdd': '15995448871@163.com'
}
getter_msg = {
    'GetterMailAdd': '2876434278@qq.com'
}
email_msg = {
    'MailTitle': '标题',
    'Body': ss

}
send_email = SendEmail.SendEmail(sender_msg, getter_msg, email_msg)
send_email.send_email()