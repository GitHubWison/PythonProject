# coding=utf-8
import SuperDict
# 对互助列表进行压力测试
import StaticVar
STATICVAR = StaticVar.StaticVar()
surlv2 = STATICVAR.spell_url_v2({
    'HEAD': 'Questions/getAllCommunityQuestionListNew/',
    'TS': '0/',
    'TOKEN': '5555c4f3698692b75bc1da01/',
    'DIVICEID': 'BDDFA469774D8A467FD517CEAD8F62BE',
    'VAR': '?range=around&type='+STATICVAR.TYPE+'&vname='+STATICVAR.VNAME+'&sortrule=release&cacheGroupKey=question_list0releasefalsetrue&vcode='+STATICVAR.VCODE
})
STATICVAR.operat_threads(STATICVAR.generate_mutible_threads(surlv2, True, '', 1))
