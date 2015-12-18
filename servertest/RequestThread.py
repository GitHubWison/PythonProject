# coding=utf-8
import threading, requests, json
import urllib
import urllib2
# 定义线程
class RequestThread(threading.Thread):
    urla = ''
    is_get_true = True
    test_request_data = ''
    def __init__(self, url, is_get=True, test_req_data=''):
        threading.Thread.__init__(self)
        self.urla = url
        self.is_get_true = is_get
        self.test_request_data = test_req_data

    def run(self):
        print("=====the response message===="+str(self.test_performace()))


    def test_performace(self):
        try:
            if self.is_get_true:
                # 是get请求
                xiaoqu = requests.get(self.urla)
                if xiaoqu.status_code != 200:
                    print("wrong var")
                else:
                    return ('SUCCESS')
            else:
                headers = {"Content-type": "application/json"}
                json_string = json.dumps(self.test_request_data)
                print(str(json_string))
                req = urllib2.Request(self.urla, json_string, headers)
                res_data = urllib2.urlopen(req)
                res = res_data.read()
                return(res)
        except EOFError as eof:
            print(str(eof.message))