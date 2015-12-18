# coding=utf-8
import StaticVar, demjson,json,urllib,urllib2
# qq登录测试
STATICVAR= StaticVar.StaticVar()

surl = STATICVAR.spell_url_v2({
    'HEAD': 'Questions/newQuestion/',
    'DIVICEID': 'BDDFA469774D8A467FD517CEAD8F62BE',
    'TOKEN': '560104777b45540c15807770/',
    'VAR': '?type='+STATICVAR.TYPE+'&channelId=fir'+'&vname='+STATICVAR.VNAME+'&vcode='+STATICVAR.VCODE
})

#发布邻里问问／随便说说的主体内容
post_desc = STATICVAR.get_excel_data(0,0)
#1.发求助帖(跨小区)测试
questiontest = {
    "around": True,
    "md5": "5fce2ff4854193e945036021f75f0c14",
    "category": "question",
    "desc": post_desc
}


#2.发随便说说(跨小区)测试
saysaytest = {
	"around": True,
	"md5": "3203d6c8fab893148c14ce464e186d76",
	"category": "share",
	"desc": post_desc
}

print(surl)

STATICVAR.generate_thread(surl, False, questiontest)
