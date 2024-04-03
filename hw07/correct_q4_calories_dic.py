def total_calorie(fruits, fruits_calorie_dic):
    total=0
    for fruit_name in fruits:
        total+=fruits[fruit_name]*fruits_calorie_dic[fruit_name]/100
    return total

def main():
    fruits={"딸기":300, "한라봉":150}
    fruits_calorie_dic={"한라봉":0.5, "딸기":0.34, "바나나":0.77}
    print(f"총 섭취한 칼로리량은 {total_calorie(fruits, fruits_calorie_dic):.2f}㎉입니다.")

if __name__=="__main__":
    main()