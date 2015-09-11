# coding=utf-8
class SuperDict(dict):
    def get_msg(self, msg_head):
        try:
            msg_data = self[msg_head]
            return msg_data
        except KeyError as keyerror:
            return ''

    # 将dict的信息做处理
    def put_msg(self, dic_msg):
        for each_key in dic_msg:
            self[each_key] = dic_msg[each_key]
        return self

