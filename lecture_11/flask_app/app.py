import json
from flask import Flask, request, Response

app = Flask(__name__)

def get_data():
    with open('storage2.json', 'r') as f:
        return json.load(f)

def store_data(data):
    with open('storage2.json', 'w') as f:
        return json.dump(data, f)

@app.route('/pray-requests/', methods=['GET'])
def pray_requests():
    return Response(
        json.dumps(get_data()),
        mimetype='application/json'
    )

@app.route('/pray-requests/', methods=['POST'])
def create_pray_requests():
    data = get_data()
    latest_id = max([msg['id'] for msg in data], default=0) + 1
    data.append({
        "id": latest_id,
        "message": request.get_json()["message"]
    })
    store_data(data)
    return Response (
        json.dumps({
            "pray_id": latest_id
        }),
        mimetype='application/json',
    )

@app.route('/pray-requests/<int:pray_id>/', methods=['GET'])
def pray_requests2(pray_id):
    data = get_data()
    for i in range(len(data)):
        if data[i]["id"] == pray_id:
            return Response (
                json.dumps(data),
                mimetype='application/json',
            )
    return Response("Not found pray request", status=404)

@app.route('/pray-requests/<int:pray_id>', methods=['PUT'])
def update_pray_request(pray_id):
    data = get_data()
    for i in range(len(data)):
        if data[i]["id"] == pray_id:
            data[i]["message"] = request.get_json()["message"]
            store_data(data)
            break
    else:
        return Response("Not found pray request", status=404)
    return Response(
        json.dumps(data),
        status=200,
        mimetype='application/json')

@app.route('/pray-requests/<int:pray_id>', methods=['DELETE'])
def delete_pray_request(pray_id):
    data = get_data()
    for i in range(len(data)):
        if data[i]["id"] == pray_id:
            del data[i]
            store_data(data)
            return Response(status=204)
    return Response("Not found pray request", status=404)