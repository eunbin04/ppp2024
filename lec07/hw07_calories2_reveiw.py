def total_calorie(fruits_eat, fruits_cal_dic):
    total=0
    for fruit_name, fruit_gram in fruits_eat.items():
        total+=fruit_gram*fruits_cal_dic[fruit_name]/100
    return total

def main():
    fruits_mon={"딸기":300, "한라봉":150}
    fruits_calorie_dic={"한라봉":50, "딸기":34, "바나나":77}
    print(total_calorie(fruits_mon, fruits_calorie_dic))

    fruits_wed={"딸기":200, "바나나":300}
    print(total_calorie(fruits_wed, fruits_calorie_dic))

if __name__=="__main__":
    main()