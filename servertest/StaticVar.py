# coding=utf-8
import time, RequestThread, SuperDict
class StaticVar:
    # 压力测试的总次数
    TEST_COUNT = 10
    # 压力测试的地址
    SERVER_NAME = "http://120.55.126.201/rest/v1.0/"
    # VSOME = '?type=android&vname=1.8.25(106)-debug&vcode=108025'
    VNAME = '2.0.7(127)-debug'
    VCODE = '200007'
    TYPE = 'android'

    # 拼写url
    def spell_url_v2(self, urlmsg_original):
        urlmsg = SuperDict.SuperDict().put_msg(urlmsg_original)
        spell_string = self.SERVER_NAME + urlmsg.get_msg('HEAD') + urlmsg.get_msg('TS') + urlmsg.get_msg('TOKEN') + urlmsg.get_msg('DIVICEID') + urlmsg.get_msg('VAR')
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
        return str(time_span)

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

    # 打印后台日志
    def print_results(self,results_dic = {}):
        results = ''
        for each_key in results_dic:
            results = results + each_key + ":" + results_dic[each_key] + "\n"
        print(results)


