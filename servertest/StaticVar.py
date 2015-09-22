# coding=utf-8
import time, RequestThread, SuperDict, requests
class StaticVar:
    # 压力测试的总次数
    TEST_COUNT = 10
    # 压力测试的地址
    SERVER_NAME = "http://120.55.126.201/rest/v1.0/"
    # VSOME = '?type=android&vname=1.8.25(106)-debug&vcode=108025'
    VNAME = '2.0.7(127)-debug'
    VCODE = '200007'
    TYPE = 'android'
    # 日期格式
    ISOTIMEFORMAT = '%Y-%m-%d %X'
    DIRECTION_TOP = "top"
    DIRECTION_DOWN = "down"

    # 拼写url
    def spell_url_v2(self, urlmsg_original):
        urlmsg = SuperDict.SuperDict().put_msg(urlmsg_original)
        spell_string = self.SERVER_NAME + urlmsg.get_msg('HEAD') + urlmsg.get_msg('TS') + urlmsg.get_msg('TOKEN') + urlmsg.get_msg('DIVICEID') + urlmsg.get_msg('VAR') + urlmsg.get_msg('DIRECTION')
        return spell_string

    def operat_threads(self, threads):
        # 开始的时间
        start_time = time.time()
        count = 0
        while True:
            try:
                if threads[count].isAlive():
                    continue
                else:
                    count += 1
            except IndexError as ierror:
                break
        time_span = time.time()-start_time
        # print("totaltime== %s") % str(time_span)
        # print("ok!")
        return time_span

    # 生成单个的进程
    def generate_thread(self, surl, is_get=True, test_data=''):
        threads = []
        t = RequestThread.RequestThread(surl, is_get, test_data)
        threads.append(t)
        t.start()
        return threads


    # 批量生成进程
    def generate_mutible_threads(self, surl, is_get=True, test_data='', t_count=TEST_COUNT):
        i = 0
        threads = []
        while i < t_count:
            t = RequestThread.RequestThread(surl, is_get, test_data)
            threads.append(t)
            t.start()
            i += 1
        return (threads)

    #生成连续的进程批量，模拟用户连续的操作
    #surls：字典类型的数组，存放单个字典示例{'url':'www.baidu.com','is_get':True,test_data=''}
    def generate_series_threads(self, surls=[]):
        threads = []
        for each_url_dic in surls:
            urlmsg = SuperDict.SuperDict().put_msg(each_url_dic)
            # 测试的url地址
            url = urlmsg.get_msg('url')
            # 是否是get请求
            is_get = urlmsg.get_msg('is_get')
            # 如果是post请求，则需要把测试的参数传进来
            if is_get == False:
                test_data = urlmsg.get_msg('test_data')
            else:
                test_data = ''
            t = RequestThread.RequestThread(url, is_get, test_data)
            threads.append(t)
            t.start()
        return threads

    # 获得后台日志
    def print_results(self, results_dic={}):
        current_time = time.strftime(self.ISOTIMEFORMAT, time.localtime(time.time()))
        logs = open(current_time + '.txt', 'w')
        results = ''
        i = 1
        for each_key in results_dic:
            results = results + "第"+ str(i) + "轮" + ":" + str(results_dic[each_key]) + "\n"
            i = i + 1
        # results = results + "平均值：" + str(self.get_avg(results_dic)) + "\n" +
        # "峰值：" +
        results = results + "最快用时：" + str(self.get_statistics(results_dic)["TheFast"]) + "\n" +"最慢用时：" + \
                  str(self.get_statistics(results_dic)["TheLowest"]) + "\n" +"平均用时：" + \
                  str(self.get_statistics(results_dic)["TheAvg"]) + "\n"

        logs.write(results)
        # return results

    #平均值，峰值，谷值
    def get_statistics(self,data):
        sum = 0
        # 最快值
        the_fast = 0
        # 最慢值
        the_lowest = 0
        for each_data in data:
            if the_fast == 0:
                the_fast = data[each_data]
            else:
                the_fast = data[each_data] if data[each_data] < the_fast else the_fast
            if the_lowest == 0:
                the_lowest = data[each_data]
            else:
                the_lowest = data[each_data] if data[each_data] > the_lowest else the_lowest
            sum = sum + data[each_data]
        #平均值
        avg = sum/len(data)
        return ({"TheFast":the_fast, "TheLowest":the_lowest, "TheAvg":avg})

    #分页时生成批量的数据
    def get_paging_list_urls(self, url):
        nowurldic = url
        # nextTs
        nextTs = ''
        # 存储分页的url
        lists = [self.spell_url_v2(url)]
        url["DIRECTION"] = '&direction='+self.DIRECTION_DOWN
        print(lists)
        for i in range(0, 5):
            xiaoqu = requests.get(self.spell_url_v2(url))
            xiaoqu_content = xiaoqu.json()
            nextTs = str(xiaoqu_content["data"]["nextTs"]) + "/"
            # 拼接url
            nowurldic["TS"] = nextTs
            lists.append(self.spell_url_v2(nowurldic))
        return(lists)







