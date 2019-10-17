import sys
import json
import requests

from django import conf


def sendmessage(message):
    url = conf.settings.DINGDING_WEBHOOK_PATH
    HEADERS = {
        "Content-Type": "application/json ;charset=utf-8 "
    }
    message = message
    String_textMsg = {
        "msgtype": "text",
        "text": {"content": message},
         "at": {
            "isAtAll": 1                                         #如果需要@所有人，这些写1
        }
    }
    String_textMsg = json.dumps(String_textMsg)
    res = requests.post(url, data=String_textMsg, headers=HEADERS)
    print(res.text)

