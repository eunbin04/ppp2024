import os
import requests

import matplotlib.pyplot as plt
import numpy as np

url=" https://api.taegon.kr/stations/146/?sy=2023&ey=2023&format=csv"
filename="./hw18/weather_146_2023-2023.csv"
if not os.path.exists(filename):
    with open(filename,"w") as f:
        res =requests.get(url)
        f.write(res.text)


from years_temp import read_col

def read_col_int(filename, col_name):
    dataset=[]
    with open(filename) as f:
        lines=f.readlines()
        header=[x.strip() for x in lines[0].split(",")]
        col_idx=header.index(col_name)
        for line in lines[1:]:
            tokens=line.strip().split(",")
            dataset.append(int(tokens[col_idx]))
    return dataset


def main():
    tavg=read_col(filename, "tavg")
    summer_temp=[]
    winter_temp=[]

    months=read_col_int(filename, "month")
    summer_months=[]
    winter_months=[]

    for m, temp in zip(months, tavg):
        if m in [6, 7, 8]:
            summer_months.append(m)
            summer_temp.append(temp)
        elif m in [12, 1, 2]:
            winter_months.append(m)
            winter_temp.append(temp)

    summer_months=np.array(summer_months)
    summer_temp=np.array(summer_temp)
    winter_months=np.array(winter_months)
    winter_temp=np.array(winter_temp)

    plt.rcParams['font.family'] = ['NanumGothic', 'sans-serif']
    plt.rcParams['axes.unicode_minus'] = True

    plt.scatter(summer_months, summer_temp, color="r", label="여름철 온도분포")
    plt.scatter(winter_months,winter_temp, color="b", label="겨울철 온도분포")
    
    plt.ylabel("Temperature(℃)")
    plt.xlabel("Month")

    plt.title("<여름철과 겨울철의 온도분포>")
    plt.legend()
    plt.savefig("./hw18/summer_winter.png")

if __name__ == "__main__":
    main()
