def total_cal(eat_gram):
    eat_gram={"hanlabog", "strawberry", "banana", "mango", "grape"}
    fruit={"hanlabog", "strawberry", "banana", "mango", "grape"}
    calories={"hanlabog":0.5, "strawberry":0.34, "banana":0.77, "mango":0.61, "grape":0.6}
    
    for fruit in calories:
        total_cal = total_cal+calories[fruit] * [eat_gram]

def main():
    hanlabog=int(input("한라봉의 섭취량을 입력하시오."))
    strawberry=int(input("딸기의 섭취량을 입력하시오."))
    banana=int(input("바나나의 섭취량을 입력하시오."))
    mango=int(input("망고의 섭취량을 입력하시오."))
    grape=int(input("포도의 섭취량을 입력하시오."))
    print(f"총 칼로리는 {total_cal}입니다.")

if __name__=="__main__":
    main()