# coding=utf-8
# 列表分页功能的压力测试
import StaticVar,time
import threading, requests
STATICVAR = StaticVar.StaticVar()
nextTs = 0
#全部－按智能排序
all_smart = STATICVAR.spell_url_v2({
    'HEAD': 'mutualAid/all/list/',
    'TS': '0/',
    'TOKEN': '54fb62c0c9ee88e6318c7ca8/',
    'DIVICEID': 'AF64D0152793E543211D36E9D1651814',
    'VAR': '?sort=smart&range=around&type='+STATICVAR.TYPE+'&vname='+STATICVAR.VNAME+'&direction=top&cacheGroupKey=question_list0smartfalsetrue&vcode='+STATICVAR.VCODE
})

xiaoqu = requests.get(all_smart)
xiaoqu_content = xiaoqu.json()
nextTs = xiaoqu_content["data"]["nextTs"]
print(nextTs)
print(xiaoqu_content)