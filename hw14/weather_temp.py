import sys
if "./" not in sys.path:
    sys.path.append("./")

from lec13 import hw_submission

def download(filename, url):
    import os
    import requests

    if not os.path.exists(filename):
        with open(filename,"w") as f:
            res =requests.get(url)
            f.write(res.text)

from lec11.weather_q78 import read_col, read_col_int

def main():
    URL="https://data.kma.go.kr/stcs/grnd/downloadGrndTaList.do?fileType=csv&pgmNo=70&menuNo=432&serviceSe=F00101&stdrMg=99999&startDt=19040101&endDt=20240422&taElement=MIN&taElement=AVG&taElement=MAX&stnGroupSns=&selectType=1&mddlClssCd=SFC01&dataFormCd=F00501&dataTypeCd=standard&startDay=19040101&startYear=1904&endDay=20240422&endYear=2024&startMonth=01&endMonth=12&sesnCd=0&txtStnNm=%EC%A0%84%EC%A3%BC&stnId=146&areaId=&gFontSize="
    filename="./hw14/jeonju_all.csv"
    download(filename, URL)

    tmax=read_col(filename, "Col 5")
    tmin=read_col(filename, "Col 4")
    tmax_date=read_col_int(filename, "Col 1")
    tdiff_max_date=read_col_int(filename, "Col 1")

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

    #tmax, tmax_date=38,"2021-08-12"
    #tdiff_max, tdiff_max_date=28.5, "1989-01-09"
    #hw_submission.submit("박은빈", tmax, tmax_date, tdiff_max, tdiff_max_date)
    tdiff_max=max(temp_diff)
    print(f"{max(tmax):.2f}℃ , {tmax_date[max_idx]} {tdiff_max:.2f}℃ , {tdiff_max_date[max_idx]}")

if __name__=="__main__":
    main()