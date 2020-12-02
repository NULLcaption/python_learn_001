# 钉钉机器人定时发送任务
import json
import requests
import time
import sched
import threading

# 初始化sched模块的scheduler类
# 第一个参数是一个可以返回时间戳的函数，第二个参数可以在定时未到达之前阻塞。
schedule = sched.scheduler(time.time, time.sleep)


def toMassage():
    url = 'https://oapi.dingtalk.com/robot/send?access_token' \
          '=9f9034185c4d74ea9af1e036a327d0b20ce68e6e325721255f7d35d5709266e7 '
    HEADERS = {
        "Content-Type": "application/json ;charset=utf-8 "
    }
    String_textMsg = {
        "msgtype": "text",
        "text": {"content": '测试成功！'},
        "at": {
            "atMobiles": [
                "18868345795",
                "18657273958"
            ],
            "isAtAll": False}
    }
    String_textMsg = json.dumps(String_textMsg)
    res = requests.post(url, data=String_textMsg, headers=HEADERS)
    print(res.text)
    timer = threading.Timer(5, toMassage)
    timer.start()


# 运行程序
if __name__ == "__main__":
    timer = threading.Timer(5, toMassage)
    timer.start()
