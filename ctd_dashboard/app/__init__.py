from threading import Thread

from flask import Flask, render_template
from tornado.ioloop import IOLoop

from bokeh.embed import server_document
from bokeh.server.server import Server

from app.bokeh.salt_app import salt_app
from app.bokeh.nuts_app import nuts_app

# set in cmd first:
# export FLASK_ENV=development
app = Flask(__name__)


@app.route("/")
def home():
    return render_template("home.html", title="Dashboard")


@app.route("/salts", methods=["GET"])
def salts():
    script = server_document("http://0.0.0.0:5006/salt_app")
    return render_template("embed.html", script=script, template="Flask")


@app.route("/nutrients", methods=["GET"])
def nutrients():
    script = server_document("http://0.0.0.0:5006/nuts_app")
    return render_template("embed.html", script=script, template="Flask")


def bk_worker():
    server = Server(
        {"/salt_app": salt_app, "/nuts_app": nuts_app},
        io_loop=IOLoop(),
        allow_websocket_origin=["0.0.0.0:8000"],
    )
    server.start()
    server.io_loop.start()


Thread(target=bk_worker).start()
