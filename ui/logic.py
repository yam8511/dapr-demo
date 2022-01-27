"""
邏輯層 - Logic Layer
負責呼叫API，或處理邏輯的程序寫這一層

ps. API = Web Service
"""

import json
from dapr.clients import DaprClient

app_id = "app-1"


def count():
    with DaprClient() as d:
        res = d.invoke_method(app_id, "count", "")
        return res.json()


def sum(a, b):
    with DaprClient() as d:
        req = json.dumps(
            {
                "A": a,
                "B": b,
            }
        )
        res = d.invoke_method(app_id, "sum", req)
        return res.json()


def upload(f):
    with DaprClient() as d:
        res = d.invoke_method(app_id, "uplaod", f)
        return res.data
