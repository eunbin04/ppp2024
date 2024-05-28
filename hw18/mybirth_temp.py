import os
import requests

import matplotlib.pyplot as plt
import numpy as np

url=" https://api.taegon.kr/stations/146/?sy=1980&ey=2023&format=csv"

filename="./hw18/weather_146_1980-2023.csv"

if not os.path.exists(filename):
    with open(filename,"w") as f:
        res =requests.get(url)
        f.write(res.text)

from summer_winter import read_col, read_col_int

def main():
    tavg=read_col(filename, "tavg")
    year_tavg=np.array(tavg)
    date_temp=[]

    years=read_col_int(filename, "year")
    months=read_col_int(filename, "month")
    days=read_col_int(filename, "day")
    date=[]

    for m, d in zip(months, days):
        if m in [8]:
            if d in [24]:
                date.append(years)
                date_temp.append(tavg)
        else:
            pass

    plt.rcParams['font.family'] = ['NanumGothic', 'sans-serif']
    plt.rcParams['axes.unicode_minus'] = False

    plt.plot(year_tavg, color="g", label="평균기온", marker='o')
     
    plt.ylabel("Temperature(℃)")
    plt.xlabel("Year")
    plt.xlim(2000,2023)
    plt.ylim(20,30)

    plt.legend()
    plt.title("<내 생일날(8/24)의 기온>")
    plt.savefig("./hw18/mybirth_temp.png")

if __name__ == "__main__":
    main()