"""
邏輯層 - Logic Layer
負責呼叫API，或處理邏輯的程序寫這一層

ps. API = Web Service
"""

import json
from curl import curl_dapr


app_id = "app-1"


def count():
    res = curl_dapr(app_id, "count", "")
    print(res.headers)
    return json.loads(res.data)
    # with DaprClient() as d:
    #     res = d.invoke_method(app_id, "count", "", http_verb="POST")
    #     return res.json()


def sum(a, b):
    req = json.dumps(
        {
            "A": a,
            "B": b,
        }
    )

    res = curl_dapr(app_id, "sum", req)
    return json.loads(res.data)
    # with DaprClient() as d:
    #     res = d.invoke_method(app_id, "sum", req, http_verb="POST")
    #     return res.json()


def inference(img):
    res = curl_dapr(app_id, "inference", img)
    return res.data
    # with DaprClient() as d:
    #     res = d.invoke_method(app_id, "inference", img, http_verb="POST")
    #     return res.data
