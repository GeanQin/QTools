from flask import Flask, request
import time
import requests

app = Flask(__name__)


@app.route("/get_time_stamp")
def get_time_stamp():
    t = time.time()
    return str(t)

@app.route("/get_weather_icon")
def get_weather_icon():
    ip = request.remote_addr
    ad_url = 'https://restapi.amap.com/v3/ip?key=e23f931ef9beee317fa5d06cbaaee882&ip=' + ip
    ad_req = requests.get(ad_url)
    ad_resp = ad_req.json()
    weather_url = 'https://restapi.amap.com/v3/weather/weatherInfo?key=e23f931ef9beee317fa5d06cbaaee882&city=' + ad_resp["adcode"]
    weather_req = requests.get(weather_url)
    weather_resp = weather_req.json()
    lives = weather_resp["lives"]
    if "雨" in lives[0]["weather"]:
        return str("rain")
    elif "雪" in lives[0]["weather"]:
        return str("rain")
    elif "晴" in lives[0]["weather"]:
        return str("sun")
    elif "少云" in lives[0]["weather"]:
        return str("sun")
    else:
        return str("cloud")