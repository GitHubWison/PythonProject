import SuperDict,RequestThread
# stu = SuperDict.SuperDict()
# studic = {'StudentName': 'stu_name', 'StudentBirth': 'stu_birthday', 'Student3Score': 'stu_3score'}
# # stu['StudentName'] = 'stu_name'
# stu.put_msg(studic)
#
# print(stu.get_msg('StudentName'))

# for each_item in stu:
#     print(each_item)
threads = ['1', 'bird']
thr = RequestThread.RequestThread()
# print(type(threads))
if isinstance(threads, list):
    print('OK')
else:
    print('bad')


