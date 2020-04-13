from flask import Flask

app = Flask(__name__)

# export FLASK_APP=hello.py
# export FLASK_ENV=development  # enable debug mode
# flask run


@app.route("/")  # host on 127.0.0.1:5000
# @app.route("/hello")  # host on 127.0.0.1:5000/hello
def hello_world():
    return "Hello, Mike!"
