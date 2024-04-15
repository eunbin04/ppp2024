def read_col(filename, col_name):
    dataset=[]
    with open(filename) as f:
        lines=f.readlines()
        header=[x.strip() for x in lines[0].split(",")]
        print(header)
        col_idx=header.index(col_name)
        print(col_name, col_idx)
        #col_name은 아래에서 숫자(4) 대신 tavg로 나타내기 위함
        for line in lines[1:]:
            tokens=line.split(",")
            dataset.append(float(tokens[col_idx]))
    return dataset

def count_rainday(rainfall):
    #방법1
    rain_day=0
    for rain in rainfall:
        if rain>=5:
            rain_day+=1
    return rain_day

    #방법2-비가 온 날은 1, 안 온 날은 0
    #return sum([1 if x >= 5 else 0 for x in rainfall])


def main():
    weather_filename="lec10/weather(146)_2022-2022.csv"
    tavg=read_col(weather_filename, "tavg")
    rainfall=read_col(weather_filename, "rainfall")

    print(f"연 평균 기온은 {sum(tavg)/len(tavg):.2f}C입니다.")
    print(f"5mm 이상 강우일수는 {count_rainday(rainfall)}일입니다.")
    print(f"총 강수량은 {sum(rainfall):.1f}mm입니다.")