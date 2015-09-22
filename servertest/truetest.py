# coding=utf-8
import SuperDict,RequestThread,StaticVar,time
STATICVAR = StaticVar.StaticVar()
# stu = SuperDict.SuperDict()
# studic = {'StudentName': 'stu_name', 'StudentBirth': 'stu_birthday', 'Student3Score': 'stu_3score'}
# stu.put_msg(studic)
# allstumsg = SuperDict.SuperDict()
#
# print(stu.get_msg('StudentName'))
# stu_string = 'abcdef';
# studic = {'sturand': stu_string, 'stumsg':'yes'}
# studic2 = {'sturand': stu_string, 'stumsg':'no'}
# stuarray = [studic,studic2]
# print(stuarray)
# for each_item in stu:
#     print(each_item)
# threads = ['1', 'bird']
# thr = RequestThread.RequestThread()
# # print(type(threads))
# if isinstance(threads, list):
#     print('OK')
# else:
#     print('bad')
#
# for i in range(0,10):
#     print('****'+str(i))

# StaticVar.StaticVar().print_results({"hello":"myhello","222":"22222222222","yo":"yoooooooo"})
# 创建txt文件
# f = open('f.txt','w')
# f.write("*****")
# f.close()

# ISOTIMEFORMAT = '%Y-%m-%d %X'
# print(time.strftime(ISOTIMEFORMAT, time.localtime(time.time())))

# StaticVar.StaticVar().get_avg({"one":1,"two":2,"three":3})
# stat_time = time.time()
# while (time.time() - stat_time) < 2:
#     continue
# print("SUCCESS")


#全部－按智能排序
all_smart = {
    'HEAD': 'mutualAid/all/list/',
    'TS': "0/",
    'TOKEN': '54fb62c0c9ee88e6318c7ca8/',
    'DIVICEID': 'AF64D0152793E543211D36E9D1651814',
    'VAR': '?sort=smart&range=around&type='+STATICVAR.TYPE+'&vname='+STATICVAR.VNAME+'&direction=top&cacheGroupKey=question_list0smartfalsetrue&vcode='+STATICVAR.VCODE
}
STATICVAR.get_paging_list_urls(all_smart)

# a = 1442472679343
# print(str(a) + "/")









