#평균 온도
def read_tavg(filename):
    results=[]
    with open(filename) as f:
        lines=f.readlines()
        for line in lines[1:]:
            tokens=line.split(",")
            tavg=float(tokens[4])
            results.append(tavg)
    return results

def average(tavg):
    return sum(tavg)/len(tavg)

#강수량
def read_rainfall(filename):
    results=[]
    with open(filename) as f:
        lines=f.readlines()
        for line in lines[1:]:
            tokens=line.split(",")
            rainfall=float(tokens[9])
            results.append(rainfall)
    return results

def more(rainfall):
    list=[]
    for rain in rainfall:
        if rain>=0.5:
            list.append(rain)
    return list

#일조 시간
def read_sunshine(filename):
    results=[]
    with open(filename) as f:
        lines=f.readlines()
        for line in lines[1:]:
            tokens=line.split(",")
            sunshine=float(tokens[8])
            results.append(sunshine)
    return results

def average(sunshine):
    return sum(sunshine)/len(sunshine)

#습도
def read_humid(filename):
    results=[]
    with open(filename) as f:
        lines=f.readlines()
        for line in lines[1:]:
            tokens=line.split(",")
            humid=float(tokens[6])
            results.append(humid)
    return results


def main():
    tavg=read_tavg("hw10/weather(146)_2022-2022.csv")
    rainfall=read_rainfall("hw10/weather(146)_2022-2022.csv")
    sunshine=read_sunshine("hw10/weather(146)_2022-2022.csv")
    humid=read_humid("hw10/weather(146)_2022-2022.csv")
    print(f"연 평균 기온은 {average(tavg):.1f}℃ 입니다.")
    print(f"5mm이상 강우일수는 {len(more(rainfall))}일 입니다.")
    print(f"총 강우량은 {sum(rainfall):.1f}mm입니다.")
    print(f"연 평균 일조 시간은 {average(sunshine):.1f}시간 입니다.")
    print(f"연 최고 습도는 {max(humid):.1f}% 입니다.")

if __name__=="__main__":
    main()