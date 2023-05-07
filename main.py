#!flask/bin/python
from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/", methods=["GET"])
def index():
    return "It is a capital mistake to theorize before one has data. \n- Sherlock Holmes -"

@app.route("/create_merchant/", methods=["PUT"])
def create_merchant():
    body = request.get_json(force=True)
    return "create a merchant"

@app.route("/update_merchant/", methods=["POST"])
def update_merchant():
    body = request.get_json(force=True)
    print(body)
    return "update a merchant"

@app.route("/delete_merchant/", methods=["DELETE"])
def delete_merchant():
    body = request.get_json(force=True)
    return "delete a merchant"

@app.route("/get_merchant/", methods=["GET"])
def get_merchant():
    #body = request.get_json(force=True)
    return "get a merchant"

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=8080)
