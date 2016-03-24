# coding=utf-8
import StaticVar,json
# qq登录测试
STATICVAR= StaticVar.StaticVar()
# surlv2 = STATICVAR.spell_url_v2({
#     'HEAD': 'app/thirdParty/login/',
#     'VAR': '?type='+STATICVAR.TYPE+'&vname='+STATICVAR.VNAME+'&vcode='+STATICVAR.VCODE,
#     'DIVICEID': "BDDFA469774D8A467FD517CEAD8F62BE"
# })
# STATICVAR.operat_threads(STATICVAR.generate_mutible_threads(surlv2, False, {"id": "4CAFC66F62734C0DFE5F8721FFB361F8"}))
#http://t.app.66xiaoqu.com/rest/v1.0/users/appLogin/BDDFA469774D8A467FD517CEAD8F62BE?type=android&vname=2.0.2(59)&vcode=200002
# 手机登录测试
# 1.登录
surl = STATICVAR.spell_url_v2({
    'HEAD': 'users/appLogin/',
    'DIVICEID': 'BDDFA469774D8A467FD517CEAD8F62BE',
    'VAR': '?type='+STATICVAR.TYPE+'&vname='+STATICVAR.VNAME+'&vcode='+STATICVAR.VCODE
})
login_data = {"userPassword": "qqqqqq", "mobilePhone": "15995448875"}
# login_json = json.dumps(login_data)
# print(login_json)
STATICVAR.generate_thread(surl, False, login_data)

