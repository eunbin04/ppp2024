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

def read_col(filename, col_name):
    dataset=[]
    with open(filename) as f:
        lines=f.readlines()
        header=[x.strip() for x in lines[0].split(",")]
        col_idx=header.index(col_name)
        for line in lines[1:]:
            tokens=line.split(",")
            dataset.append(float(tokens[col_idx]))
    return dataset

def main():
    tavg=read_col(filename, "tavg")
    year_tavg=np.array(tavg)

    tmax=read_col(filename, "tmax")
    year_tmax=np.array(tmax)

    tmin=read_col(filename, "tmin")
    year_tmin=np.array(tmin)
    
    plt.rcParams['font.family'] = ['NanumGothic', 'sans-serif']
    plt.rcParams['axes.unicode_minus'] = True

    plt.plot(year_tavg, color="lightblue", label="평균기온")
    plt.plot(year_tmax, color="r", label="최고온도")
    plt.plot(year_tmin, color="b", label="최저온도")
     
    plt.ylabel("Temperature(℃)")
    plt.xlabel("Year")
    plt.xlim(1980,2023)

    plt.title("<연 평균 기온>")
    plt.legend()
    plt.savefig("./hw18/years_temp.png")

if __name__ == "__main__":
    main()