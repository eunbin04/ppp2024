from weather_read_col import read_col, read_col_int

def main():
    filename="hw12/weather(146)_2001-2022.csv"
    tmax=read_col(filename, "tmax")
    tmin=read_col(filename, "tmin")
    years=read_col_int(filename, "year")
    months=read_col_int(filename, "month")
    days=read_col_int(filename, "day")

    temp_diff=[]
    for tx, tn in zip(tmax, tmin):
        temp_diff.append(tx-tn)

    max_idx=0
    max_diff_temp=0
    i=0
    last_year=0

    for i in range(len(temp_diff)):
        if years[i]!=last_year:
            last_year=years[i]
            max_diff_temp=temp_diff[i]
            max_idx=i
            print(f"날짜: {years[max_idx]}/{months[max_idx]}/{days[max_idx]} 최대일교차: {max_diff_temp:.1f}℃")
        i+=1
            
if __name__=="__main__":
    main()