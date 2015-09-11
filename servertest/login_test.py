# coding=utf-8
import StaticVar
# qq登录测试
STATICVAR= StaticVar.StaticVar()
# surlv2 = STATICVAR.spell_url_v2({
#     'HEAD': 'app/thirdParty/login/',
#     'VAR': '?type='+STATICVAR.TYPE+'&vname='+STATICVAR.VNAME+'&vcode='+STATICVAR.VCODE,
#     'DIVICEID': "BDDFA469774D8A467FD517CEAD8F62BE"
# })
# STATICVAR.operat_threads(STATICVAR.generate_mutible_threads(surlv2, False, {"id": "4CAFC66F62734C0DFE5F8721FFB361F8"}))

# 手机登录测试
# 1.登录
surl = STATICVAR.spell_url_v2({
    'HEAD': 'users/appLogin/',
    'DIVICEID': 'BDDFA469774D8A467FD517CEAD8F62BE',
    'VAR': '?type='+STATICVAR.TYPE+'&vname='+STATICVAR.VNAME+'&vcode='+STATICVAR.VCODE
})

STATICVAR.generate_thread(surl, False, {"userPassword": "000000", "mobilePhone": "15995448871"})

