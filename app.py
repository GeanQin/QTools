from flask import Flask
import time

app = Flask(__name__)


@app.route("/get_time_stamp")
def get_time_stamp():
    t = time.time()
    return str(t)
