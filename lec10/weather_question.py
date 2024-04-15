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

def count_rainday(rainfall):
    return sum([1 if x >= 5 else 0 for x in rainfall])

def longest_rainday(rainfall):
    rain_event=[]
    prev_rain_count=0
    for rain in rainfall:
        if rain ==0:
            if prev_rain_count>0:
                rain_event.append(prev_rain_count)
            prev_rain_count=0
        else:
            prev_rain_count+=1
    return max(rain_event)

def max_rainfall_event(rainfall):
    rain_event=[]
    prev_rain_count=0
    prev_rain=0
    for rain in rainfall:
        if rain ==0:
            if prev_rain_count>0:
                rain_event.append(prev_rain)
            prev_rain_count=0
            prev_rain=0
        else:
            prev_rain_count+=1
            prev_rain+=rain
    return max(rain_event)

def top_rank(values, limit):
    #return sorted(values, reverse=True)[:limit]
    return sorted(values)[-limit:][::-1]

def main():
    weather_filename="lec10/weather(146)_2022-2022.csv"
    rainfall=read_col(weather_filename, "rainfall")
    tmax=read_col(weather_filename, "tmax")

    print(f"최장연속 강우일수는 {longest_rainday(rainfall):.1f}일입니다.")
    print(f"최대 강우량은 {max_rainfall_event(rainfall):.1f}mm입니다.")
    print(f"가장 더운날 top3는 {top_rank(tmax,3)}일입니다.")
