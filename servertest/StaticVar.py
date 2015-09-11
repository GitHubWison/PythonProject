# coding=utf-8
import time, RequestThread, SuperDict
class StaticVar:
    # 压力测试的总次数
    TEST_COUNT = 10
    # 压力测试的地址
    SERVER_NAME = "http://42.62.18.90/rest/v1.0/"
    # VSOME = '?type=android&vname=1.8.25(106)-debug&vcode=108025'
    VNAME = '1.8.25(106)-debug'
    VCODE = '108025'
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
        print("totaltime== %s") % str(time_span)
        print("ok!")

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
