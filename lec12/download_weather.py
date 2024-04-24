import os
import requests

url="https://api.taegon.kr/stations/146/?sy=2022&ey=2022&format=csv"

filename="./lec12/weather_146_2022.csv"

if not os.path.exists(filename):
    with open(filename,"w") as f:
        res =requests.get(url)
        f.write(res.text)