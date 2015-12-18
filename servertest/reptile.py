# coding=utf-8
# 爬虫测试,爬取百度知道的内容
import urllib2, re, StaticVar, xlrd, sys
from xlutils.copy import copy
reload(sys)
sys.setdefaultencoding("utf-8")
STATICVAR = StaticVar.StaticVar()
request = urllib2.Request('http://zhidao.baidu.com/list?cid=106')
response = urllib2.urlopen(request)
response_string = response.read().decode('gbk')
pattern = re.compile('<div class="question-title-section">\n<div class="question-title">\n<a href=.*? class="title-link" target="_blank">\n(.*?)\n</a>\n</div>\n<div class="question-tags">\n<span class="tag-logo">\n</span>', re.S)
items = re.findall(pattern, response_string)
# 打开存放爬取数据的表格
data_xls = xlrd.open_workbook('reptile_data.xls')
wb = copy(data_xls)

# 判断是否存在百度知道的表格
all_sheet_names = data_xls.sheet_names()
need_sheet_name = 'baidu_zhidao'
judge_sheet_exits = STATICVAR.is_sheet_exist(need_sheet_name,all_sheet_names)
if judge_sheet_exits['IsExist']:
#     存在此sheet
    zhidao_sheet = wb.get_sheet(judge_sheet_exits['ExistInIndex'])
else:
    #不存在此sheet需要新建一个
    wb.add_sheet(need_sheet_name, cell_overwrite_ok=True)
    zhidao_sheet = wb.get_sheet(len(all_sheet_names))

wb.save('reptile_data.xls')
data_xls = xlrd.open_workbook('reptile_data.xls')
# 获得当前表格中一共有多少行数据
currentlen = len(data_xls.sheet_by_name('baidu_zhidao').col_values(0))

i = currentlen
for item in items:
    zhidao_sheet.write(i, 0, item)
    i += 1
wb.save('reptile_data.xls')


