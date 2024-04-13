def total_calorie(fruits_eat, fruits_cal_dic):
    total = 0
    for fruit_name in fruits_eat:
        total += fruits_eat[fruit_name] * fruits_cal_dic[fruit_name] / 100
    return total

def read_cal_db(filename):
    database={}
    with open(filename, encoding="utf-8-sig") as f:
        lines=f.readlines()
        for line in lines[1:]:
            tokens=line.split(",")
            fruit_name=tokens[0]
            fruit_cal=int(tokens[1])
            database[fruit_name]=fruit_cal
    return database

def main():
    fruits_calorie_dic=read_cal_db("hw10/my_fruit_calorie.csv")
    fruits_eaten = {"딸기": 300, "고구마": 150}
    print(f"섭취한 총 칼로리양은 {total_calorie(fruits_eaten, fruits_calorie_dic)}㎉입니다.")

if __name__ == "__main__":
    main()