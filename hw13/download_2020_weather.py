import os
import requests

url=" https://api.taegon.kr/stations/146/?sy=2020&ey=2020&format=csv"

filename="./hw13/weather_146_2020-2020.csv"

if not os.path.exists(filename):
    with open(filename,"w") as f:
        res =requests.get(url)
        f.write(res.text)


from hw10_weather_file import read_tavg, average, read_rainfall, count_rainday

def main():
    tavg=read_tavg("hw13/weather_146_2020-2020.csv")
    rainfall=read_rainfall("hw13/weather_146_2020-2020.csv")
    print(f"연 평균 기온은 {average(tavg):.2f}℃ 입니다.")
    print(f"5mm이상 강우일수는 {len(count_rainday(rainfall))}일 입니다.")
    print(f"총 강우량은 {sum(rainfall):.1f}mm입니다.")


    filename="./hw13/hw_result_2020_weather"
    with open(filename,"w")as fout:
        fout.write('연 평균 기온은 13.99℃ 입니다. 5mm이상 강우일수는 57일 입니다. 총 강우량은 1780.8mm입니다.')
    

if __name__=="__main__":
    main()