from flask import Flask, jsonify
import redis
import json 

app = Flask(__name__)

@app.route("/", methods=["GET"])
def hello_world():
	return "Welcome to the API"

@app.route("/<int:input>", methods=["GET"])
def multiply(input):
	answer = input * input 
	return str(answer)

if __name__ == "__main__":
	app.run(host='0.0.0.0')