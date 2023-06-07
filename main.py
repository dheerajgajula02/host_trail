from flask import Flask, json, jsonify, request

app = Flask(__name__)

@app.route("/run", methods=['GET'])
def run():
    return jsonify({
        "message":"server up and running"
    })

@app.route("/input_check", methods=['POST'])
def input_check():
    body = request.get_json(force=True)
    name = body['name']
    return jsonify({
        "message":name
    })

@app.route("/")
def home():
    return jsonify({
        "message":"this is home stoobid"
    })

if __name__=="__main__":
    app.run(debug=False, host="0.0.0.0")