def is_leap_year(year):
    if year%4==0:
        if year%100==0:
            return False
        else:
            return True
    elif year%4!=0:
        return False
        
def main():
    year=int(input("연도를 입력하시오:"))

    print(f"{year}년은 {is_leap_year(year)}입니다.")


if __name__=="__main__":
    main()