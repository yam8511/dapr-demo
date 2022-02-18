import http.client
import json

# API Host
api_host = "127.0.0.1"
# API Port
api_port = 3500
# API HTTPS
api_https = False


def api_conn(host=api_host, port=api_port, https=api_https):
    # 建立連線
    if https:
        conn = http.client.HTTPSConnection(api_host, api_port)
    else:
        conn = http.client.HTTPConnection(api_host, api_port)
    return conn


def curl(body, url="/", method="POST", headers={}, conn=None):
    auto_close = False
    if conn is None:
        auto_close = True
        conn = api_conn()
    conn.request(method, url, body, headers)
    res = conn.getresponse()
    res.data = res.read()

    if auto_close:
        conn.close()

    return res


def curl_json(body, url="/", method="POST", headers={}, conn=None):
    body = json.dumps(body)
    if headers is None:
        headers = {}
    headers.setdefault("Content-Type", "application/json")
    return curl(body, url, method, headers, conn)


def curl_dapr(app_id, method, body):
    return curl(body, url="/" + method, headers={"dapr-app-id": app_id})
