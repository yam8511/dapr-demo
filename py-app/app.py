from flask import Flask, request, jsonify, Response

app = Flask("app")
count = 0


@app.post("/sum")
def sum_handler():
    print("from --->", request.remote_addr)
    req = request.json
    return jsonify(req["A"], req["B"])


@app.post("/count")
def count_handler():
    print("from --->", request.remote_addr)
    global count
    count += 1
    return jsonify(count)


@app.post("/inference")
def inference_handler():
    print("from --->", request.remote_addr)
    res = Response()
    res.set_data(request.get_data())
    return res


app.run(host="0.0.0.0", port=3002)
