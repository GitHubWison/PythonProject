# coding=utf-8

# 发帖专用类
import StaticVar, sys, xlrd, xlwt
from xlutils.copy import copy
class NewQuestion:
    #初始化数据
    reload(sys)
    sys.setdefaultencoding("utf-8")
    STATICVAR = StaticVar.StaticVar()
    SHEET_NAME = 'autotest-post.xls'
    surl = STATICVAR.spell_url_v2({
        'HEAD': 'Questions/newQuestion/',
        'DIVICEID': 'BDDFA469774D8A467FD517CEAD8F62BE',
        'TOKEN': '560104777b45540c15807770/',
        'VAR': '?type='+STATICVAR.TYPE+'&channelId=tecent'+'&vname='+STATICVAR.VNAME+'&vcode='+STATICVAR.VCODE
    })
    params = ''
    #选择是邻里问问还是随便说说(0是邻里问问，1是随便说说)
    post_type = 0
    #选择是否周边小区可见
    around_cansee = False
    def __init__(self, post_type='', around_cansee = True):
        self.post_type = post_type
        self.around_cansee = around_cansee

    #读出表格的数据并返回
    def get_excel_data(self, sheet_name, excel_name):
        data = xlrd.open_workbook(excel_name)
        # 取出列表
        table = data.sheet_by_name(sheet_name).col_values(0)
        # 取出列表中的最后一行
        cell_string = table[len(table) - 1]
        # 删除列表中的最后一行
        wb = copy(data)
        ws = wb.get_sheet(StaticVar.StaticVar().is_sheet_exist(sheet_name, data.sheet_names())['ExistInIndex'])
        ws.write(len(table) - 1, 0, '')
        wb.save(excel_name)
        print(cell_string)
        return cell_string

    #从excel中获得帖子内容并发帖
    def send_post_from_excel(self):
        main_body = self.get_excel_data(self.post_type)
        self.params = {
            "around": self.around_cansee,
            "md5": "5fce2ff4854193e945036021f75f0c14",
            "category": "question" if (self.post_type == 0) else "share",
            "desc": main_body
        }

        self.STATICVAR.generate_thread(self.surl, False, self.params)

    #自定义发帖内容
    def send_post_by_custom(self, custom_body):
        self.params = {
            "around": self.around_cansee,
            "md5": "5555c4f3698692b75bc1da01",
            "category": "question" if (self.post_type == 0) else "share",
            "desc": custom_body
        }
        print('surl = ' + self.surl)
        self.STATICVAR.generate_thread(self.surl, False, self.params)






