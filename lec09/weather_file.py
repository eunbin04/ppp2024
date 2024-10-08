def read_tmax(filename):
    #return [3.5,5,7,10]
    results=[]
    with open(filename) as f:
        lines=f.readlines()
        for line in lines[1:]:
            tokens=line.split(",")
            tmax=float(tokens[3])
            results.append(tmax)
    return results

def read_tmin(filename):
    results=[]
    with open(filename) as f:
        lines=f.readlines()
        for line in lines[1:]:
            tokens=line.split(",")
            tmin=float(tokens[5])
            results.append(tmin)
    return results

def main():
    tmax=read_tmax("lec09/weather(146)_2022-2022.csv")
    tmin=read_tmin("lec09/weather(146)_2022-2022.csv")
    print(f"연 최고 온도는 {max(tmax):.1f}입니다.")
    print(f"연 최저 온도는 {min(tmin):.1f}입니다.")
if __name__=="__main__":
    main()