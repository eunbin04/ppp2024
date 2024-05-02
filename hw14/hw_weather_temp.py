import sys
import os
import requests
if "./" not in sys.path:
    sys.path.append("./")
from lec13 import hw_submission

def download(filename, url):
    if not os.path.exists(filename):
        with open(filename,"w") as f:
            res =requests.get(url)
            f.write(res.text.replace("\r", ""))


from weather_read import read_col, read_col_str

def main():
    URL="https://data.kma.go.kr/stcs/grnd/downloadGrndTaList.do?fileType=csv&pgmNo=70&menuNo=432&serviceSe=F00101&stdrMg=99999&startDt=19040101&endDt=20240422&taElement=MIN&taElement=AVG&taElement=MAX&stnGroupSns=&selectType=1&mddlClssCd=SFC01&dataFormCd=F00501&dataTypeCd=standard&startDay=19040101&startYear=1904&endDay=20240422&endYear=2024&startMonth=01&endMonth=12&sesnCd=0&txtStnNm=%EC%A0%84%EC%A3%BC&stnId=146&areaId=&gFontSize="
    filename="./hw14/jeonju_all.csv"
    download(filename, URL)
    
    tmax=read_col(filename, "최고기온(℃)")
    tmin=read_col(filename, "최저기온(℃)")
    date=read_col_str(filename, "날짜")

    #tmax
    max_temp=0
    j=0
    for tx in tmax:
        if tx == "":
            tx = 0
        if max_temp<tx:
            max_temp=tx
            #tmax_date
            max_temp_idx=j
        j+=1

    #temp_diff
    temp_diff=[]
    for tx, tn in zip(tmax, tmin):
        if tx == "" or tn == "":
            temp_diff.append(0)
        else:
            temp_diff.append(tx-tn)
    max_idx=0

    #max_diff_temp
    max_diff_temp=0
    i=0
    for td in temp_diff:
        if max_diff_temp<td:
            max_diff_temp=td
            #tdiff_max_date
            max_idx=i
        i+=1
    tdiff_max=max(temp_diff)
    
    
    print("박은빈", max_temp, date[max_temp_idx], tdiff_max, date[max_idx])
    hw_submission.submit("박은빈", max_temp, date[max_temp_idx], tdiff_max, date[max_idx])


if __name__=="__main__":
    main()