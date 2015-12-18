# coding=utf-8

import xlrd, sys, xlwt, NewQuestion, urllib2, re, StaticVar, urllib
from xlutils.copy import copy
STATICVAR = StaticVar.StaticVar()
reload(sys)
sys.setdefaultencoding("utf-8")
# from qiniu import Auth
# from qiniu import put_file
#
# import qiniu.config
#
# access_key = 'F-xDLc0uFKh7F1oNwmS_9oL3_2QALN3nKMiJyRGV'
# secret_key = 'axK2jtKGjnvoP74qPLNUjmoTC9wO0-wbKbyqvbLR'
# bucket_name = 'python-test-space'
#
# q = Auth(access_key, secret_key)
#
# mime_type = "application/octet-stream"
# params = {'x:a': 'a'}
# localfile = '/Users/xuxuqiwei/Documents/python/img/tu.png'
#
# key = 'big'
# token = q.upload_token(bucket_name, key)
#
# progress_handler = lambda progress, total: progress
# ret, info = put_file(token, key, localfile, params, mime_type, progress_handler=progress_handler)
# print(info)
# assert ret['key'] == key

# from apscheduler.schedulers.blocking import BlockingScheduler
# from datetime import datetime
# import  time,os
# def tick():
#     print('Tick!The time is:%s' % datetime.now())
#     # print('dd')
#
# scheduler = BlockingScheduler()
# scheduler.add_job(tick, 'cron', second='0', minute='38', hour='12', day='*', month='*', year='*')
# print('Press Ctrl+{0} to exit'.format('Break' if os.name == 'nt' else 'C'))
# try:
#     scheduler.start()
# except (KeyboardInterrupt, SystemExit):
#     scheduler.shutdown()



# table = data.sheets()[0]
# cols = table.col_values(0)
#
# print(cols[len(cols) - 1])
# print(len(cols))

# 写入空值
# f = xlwt.Workbook()
# sheet1 = f.add_sheet(u'sheet1',cell_overwrite_ok=True)
# sheet1.write(len(cols) - 1, 0, '123')
# f.save('autotest-post.xls')

# 获取表格的总行数
# data = xlrd.open_workbook('autotest-post.xls')
# table1 = data.sheets()[1].col_values(0)
# print(len(table1))
# wb = copy(data)
# ws = wb.get_sheet(1)
# ws.write(len(table1) - 1, 0, '')
# wb.save('autotest-post.xls')
#
#
# data = xlrd.open_workbook('autotest-post.xls')
# table1 = data.sheets()[1].col_values(0)
# print(len(table1))

# question = NewQuestion.NewQuestion(1)
# question.send_post_from_excel()

# 获得笑话集锦
request = urllib2.Request('http://www.jokeji.cn/jokehtml/ym/2015112502030477.htm')
response = urllib2.urlopen(request)
response_string = response.read().decode('gbk')
pattern = re.compile('<P>(.*?)</P>', re.S)
items = re.findall(pattern,response_string)
data = xlrd.open_workbook('autotest-post.xls')
wb = copy(data)
# laugh_words_sheet = ''
# 首先列出所有的表格名称
all_sheet_names = data.sheet_names()
#然后比较是否存在需要的sheet
need_sheet_name = 'laugh_words5'
judge_sheet_exist = STATICVAR.is_sheet_exist(need_sheet_name,all_sheet_names)
if judge_sheet_exist['IsExist']:
    #存在此sheet,需要获取sheet
    laugh_worlds_sheet = wb.get_sheet(judge_sheet_exist['ExistInIndex'])
else:
    #不存在此sheet需要新建一个
    wb.add_sheet(need_sheet_name, cell_overwrite_ok=True)
    laugh_worlds_sheet = wb.get_sheet(len(all_sheet_names))
i = 0
for item in items:
    laugh_worlds_sheet.write(i, 0, item)
    i += 1
wb.save('autotest-post.xls')






# 新建一个表格
# try:
#     laugh_words_sheet = data.sheet_by_name('laugh_words5')
# #     如果有这样的sheet则获取
# except Exception, e:
#     wb.add_sheet('laugh_words5', cell_overwrite_ok=True)
#     laugh_words_sheet = wb.get_sheet(4)
#     print('notpass')
#     i = 0
# for item in items:
#     # 写入到sheet中
#     laugh_words_sheet.write(i, 0, item)
#     i = i + 1
#     print(i)
#     # print(item)
# wb.save('autotest-post.xls')

# 在已有的excel中新建sheet
# data = xlrd.open_workbook('autotest-post.xls')
# wb = copy(data)
# try:
#     data.sheet_by_name('sheet3')
# except Exception, e:
#     print(e)
#     wb.add_sheet('sheet3', cell_overwrite_ok=True)
# sheet2 = wb.get_sheet(3)
# sheet2.write(0, 0, 'some text')
# wb.save('autotest-post.xls')
