from flask import Flask, jsonify, request

app = Flask(__name__)

# Rooting the endpoint
@app.route("/")
def home():
    return "welcome to flask!"
# other routes

@app.route("/hello")
def hello():
    return "Hello world!"

@app.route("/about")
def about():
    return "This is a simple flask app."

# json response
@app.route("/user")
def user():
    data = {"name": "john Doe", "course": "Flask ApI Development"}
    return jsonify(data)

#request handling with query parameter
@app.route("/greet")
def greet():
    name = request.args.get("name", "Alice")
    return f"Hello, {name}!"