# coding=utf-8
#首页列表的相关测试
import StaticVar,time
STATICVAR = StaticVar.StaticVar()

#全部－按智能排序
all_smart = STATICVAR.spell_url_v2({
    'HEAD': 'mutualAid/all/list/',
    'TS': '0/',
    'TOKEN': '54fb62c0c9ee88e6318c7ca8/',
    'DIVICEID': 'AF64D0152793E543211D36E9D1651814',
    'VAR': '?sort=smart&range=around&type='+STATICVAR.TYPE+'&vname='+STATICVAR.VNAME+'&direction=top&cacheGroupKey=question_list0smartfalsetrue&vcode='+STATICVAR.VCODE
})
#全部－按发布时间排序
all_date = STATICVAR.spell_url_v2({
    'HEAD': 'mutualAid/all/list/',
    'TS': '0/',
    'TOKEN': '54fb62c0c9ee88e6318c7ca8/',
    'DIVICEID': 'AF64D0152793E543211D36E9D1651814',
    'VAR': '?sort=date&range=around&type='+STATICVAR.TYPE+'&vname='+STATICVAR.VNAME+'&direction=top&cacheGroupKey=question_list0datefalsetrue&vcode='+STATICVAR.VCODE
})

#全部－按智能排序&&只看本小区
all_smart_onlymy = STATICVAR.spell_url_v2({
    'HEAD': 'mutualAid/all/list/',
    'TS': '0/',
    'TOKEN': '54fb62c0c9ee88e6318c7ca8/',
    'DIVICEID': 'AF64D0152793E543211D36E9D1651814',
    'VAR': '?sort=smart&type='+STATICVAR.TYPE+'&vname='+STATICVAR.VNAME+'&direction=top&cacheGroupKey=question_list0smartfalsefalse&vcode='+STATICVAR.VCODE
})

#全部－按发布时间排序&&只看本小区
all_date_onlymy = STATICVAR.spell_url_v2({
    'HEAD': 'mutualAid/all/list/',
    'TS': '0/',
    'TOKEN': '54fb62c0c9ee88e6318c7ca8/',
    'DIVICEID': 'AF64D0152793E543211D36E9D1651814',
    'VAR': '?sort=date&type='+STATICVAR.TYPE+'&vname='+STATICVAR.VNAME+'&direction=top&cacheGroupKey=question_list0datefalsefalse&vcode='+STATICVAR.VCODE
})
# 求助－刷新
aid = STATICVAR.spell_url_v2({
    'HEAD': 'mutualAid/question/list/',
    'TS': '0/',
    'TOKEN': '54fb62c0c9ee88e6318c7ca8/',
    'DIVICEID': 'AF64D0152793E543211D36E9D1651814',
    'VAR': '?sort=date&range=around&type='+STATICVAR.TYPE+'&vname='+STATICVAR.VNAME+'&direction=top&cacheGroupKey=question_list1datefalsetrue&vcode='+STATICVAR.VCODE
})
# 求助－只看本小区
aid_myonly = STATICVAR.spell_url_v2({
    'HEAD': 'mutualAid/question/list/',
    'TS': '0/',
    'TOKEN': '54fb62c0c9ee88e6318c7ca8/',
    'DIVICEID': 'AF64D0152793E543211D36E9D1651814',
    'VAR': '?sort=date&type='+STATICVAR.TYPE+'&vname='+STATICVAR.VNAME+'&direction=top&cacheGroupKey=question_list1datefalsefalse&vcode='+STATICVAR.VCODE
})
# 求助－只看未解决
aid_unsolvedonly = STATICVAR.spell_url_v2({
    'HEAD': 'mutualAid/question/list/',
    'TS': '0/',
    'TOKEN': '54fb62c0c9ee88e6318c7ca8/',
    'DIVICEID': 'AF64D0152793E543211D36E9D1651814',
    'VAR': '?sort=date&range=around&status=unsolved&type='+STATICVAR.TYPE+'&vname='+STATICVAR.VNAME+'&direction=top&cacheGroupKey=question_list1datefalsetrue&vcode='+STATICVAR.VCODE
})
# 求助－只看本小区－只看未解决
aid_myonly_unsolvedonly = STATICVAR.spell_url_v2({
    'HEAD': 'mutualAid/question/list/',
    'TS': '0/',
    'TOKEN': '54fb62c0c9ee88e6318c7ca8/',
    'DIVICEID': 'AF64D0152793E543211D36E9D1651814',
    'VAR': '?sort=date&status=unsolved&type='+STATICVAR.TYPE+'&vname='+STATICVAR.VNAME+'&direction=top&cacheGroupKey=question_list1datefalsefalse&vcode='+STATICVAR.VCODE
})

# 推荐－刷新
share = STATICVAR.spell_url_v2({
    'HEAD': 'mutualAid/share/list/',
    'TS': '0/',
    'TOKEN': '54fb62c0c9ee88e6318c7ca8/',
    'DIVICEID': 'AF64D0152793E543211D36E9D1651814',
    'VAR': '?sort=date&range=around&type='+STATICVAR.TYPE+'&vname='+STATICVAR.VNAME+'&direction=top&cacheGroupKey=question_list2datefalsetrue&vcode='+STATICVAR.VCODE
})
# 推荐－只看本小区
share_myonly = STATICVAR.spell_url_v2({
    'HEAD': 'mutualAid/share/list/',
    'TS': '0/',
    'TOKEN': '54fb62c0c9ee88e6318c7ca8/',
    'DIVICEID': 'AF64D0152793E543211D36E9D1651814',
    'VAR': '?sort=date&type='+STATICVAR.TYPE+'&vname='+STATICVAR.VNAME+'&direction=top&cacheGroupKey=question_list2datefalsefalse&vcode='+STATICVAR.VCODE
})

# 杂谈
talk = STATICVAR.spell_url_v2({
    'HEAD': 'mutualAid/talk/list/',
    'TS': '0/',
    'TOKEN': '54fb62c0c9ee88e6318c7ca8/',
    'DIVICEID': 'AF64D0152793E543211D36E9D1651814',
    'VAR': '?sort=date&range=around&type='+STATICVAR.TYPE+'&vname='+STATICVAR.VNAME+'&direction=top&cacheGroupKey=question_list3datefalsetrue&vcode='+STATICVAR.VCODE
})
# 杂谈－只看本小区
talk_myonly = STATICVAR.spell_url_v2({
    'HEAD': 'mutualAid/talk/list/',
    'TS': '0/',
    'TOKEN': '54fb62c0c9ee88e6318c7ca8/',
    'DIVICEID': 'AF64D0152793E543211D36E9D1651814',
    'VAR': '?sort=date&type='+STATICVAR.TYPE+'&vname='+STATICVAR.VNAME+'&direction=top&cacheGroupKey=question_list3datefalsefalse&vcode='+STATICVAR.VCODE
})


#全部－按智能排序(字典版)
all_smart_dic = {
    'HEAD': 'mutualAid/all/list/',
    'TS': '0/',
    'TOKEN': '54fb62c0c9ee88e6318c7ca8/',
    'DIVICEID': 'AF64D0152793E543211D36E9D1651814',
    'VAR': '?sort=smart&range=around&type='+STATICVAR.TYPE+'&vname='+STATICVAR.VNAME+'&cacheGroupKey=question_list0smartfalsetrue&vcode='+STATICVAR.VCODE,
    'DIRECTION': '&direction='+STATICVAR.DIRECTION_TOP
}

#全部－按发布时间排序(字典版)
all_date_dic = {
    'HEAD': 'mutualAid/all/list/',
    'TS': '0/',
    'TOKEN': '54fb62c0c9ee88e6318c7ca8/',
    'DIVICEID': 'AF64D0152793E543211D36E9D1651814',
    'VAR': '?sort=date&range=around&type='+STATICVAR.TYPE+'&vname='+STATICVAR.VNAME+'&cacheGroupKey=question_list0datefalsetrue&vcode='+STATICVAR.VCODE,
    'DIRECTION': '&direction='+STATICVAR.DIRECTION_TOP
}
def geturlsdic(urls = []):
    all_surl = []
    for each_url in urls:
        urldic = {'url': each_url, 'is_get': True}
        all_surl.append(urldic)
    return all_surl




# surls = geturlsdic([all_smart, all_date, all_smart_onlymy, all_date_onlymy,aid, aid_myonly, aid_unsolvedonly, aid_myonly_unsolvedonly,share,share_myonly,talk,talk_myonly])
# print(surls)

surls = geturlsdic(STATICVAR.get_paging_list_urls(all_smart_dic))
print(surls)
# 智能排序
# surls = geturlsdic([all_smart])
# 按发布时间排序
# surls = geturlsdic([all_date])
# STATICVAR.operat_threads(STATICVAR.generate_mutible_threads(all_date, True, '', 100))
results = {}
for i in range(1, 2):
    results[str(i)] = STATICVAR.operat_threads(STATICVAR.generate_series_threads(surls))
    stat_time = time.time()
    while (time.time() - stat_time) < 0.5:
        continue
# 将结果写入txt文件中
STATICVAR.print_results(results)