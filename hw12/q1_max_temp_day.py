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
    for td in temp_diff:
        if max_diff_temp<td:
            max_diff_temp=td
            max_idx=i
        i+=1

    print(f"날짜: {years[max_idx]}/{months[max_idx]}/{days[max_idx]} 최대일교차: {max(temp_diff):.1f}℃")

if __name__=="__main__":
    main()