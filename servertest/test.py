# coding=utf-8
#定时发帖
import NewQuestion, SendEmail, os
from apscheduler.schedulers.blocking import BlockingScheduler
# 表格名
excel_name = 'reptile_data.xls'
# 表格中的sheet名
sheet_name = 'baidu_zhidao'
# 定义邮件相关

# 定时方法
def tick_send_post():
    # os.system('python login_test.py')
    wenwen_post = NewQuestion.NewQuestion(0, False)
    # 获取表格中的最后一行内容并删除
    www_string = wenwen_post.get_excel_data(sheet_name, excel_name)
    wenwen_post.send_post_by_custom(www_string)
    # 发送邮件
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
        'MailTitle': '您的帖子(%s)已经发送成功' % www_string,
        'Body': '帖子的内容是'
    }
    print('*****')
    print(www_string)
    send_email = SendEmail.SendEmail(sender_msg, getter_msg, email_msg)
    if __name__ == '__main__':
        send_email.send_email()

    # print(www_string)
# 定义发帖时间点
question_scheduler = BlockingScheduler()
question_scheduler.add_job(tick_send_post, 'cron', second='0', minute='10', hour='10', day='*', month='*', year='*')
question_scheduler.add_job(tick_send_post, 'cron', second='0', minute='10', hour='12', day='*', month='*', year='*')
question_scheduler.add_job(tick_send_post, 'cron', second='0', minute='10', hour='14', day='*', month='*', year='*')
question_scheduler.add_job(tick_send_post, 'cron', second='0', minute='10', hour='16', day='*', month='*', year='*')
question_scheduler.start()




# os.system('python reptile.py')
