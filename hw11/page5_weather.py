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

def read_col_int(filename, col_name):
    dataset=[]
    with open(filename) as f:
        lines=f.readlines()
        header=[x.strip() for x in lines[0].split(",")]
        col_idx=header.index(col_name)
        for line in lines[1:]:
            tokens=line.split(",")
            dataset.append(int(tokens[col_idx]))
    return dataset

def sumifs(rainfall, months, conditions):
    total=0
    for i in range(len(rainfall)):
        rain=rainfall[i]
        month=months[i]
        if month in conditions:
            total += rain
    return total

def get_data_ifs(values, conditions, criteria):
    dataset=[]
    for rain,year in zip(values, conditions):
        if year == criteria:
            dataset.append(rain)
    return dataset

def main():
    weather_filename="lec10/weather(146)_2022-2022.csv"
    rainfall=read_col(weather_filename, "rainfall")
    months=read_col_int(weather_filename, "month")
    print(f"여름철(6월-8월) 강수량은 {sumifs(rainfall, months, [6,7,8]):.1f}mm입니다.")

    weather_filename="lec10/weather(146)_2001-2022.csv"
    rainfall_all=read_col(weather_filename, "rainfall")
    year_all=read_col_int(weather_filename, "year")
    rainfall_2021=get_data_ifs(rainfall_all, year_all, 2021)
    rainfall_2022=get_data_ifs(rainfall_all, year_all, 2022)
    all_rainfall=rainfall_2022+rainfall_2021
    print(f"2021년과 2022년의 총 강수량은 {sum(all_rainfall):.1f}mm입니다.")


if __name__ == "__main__":
    main()