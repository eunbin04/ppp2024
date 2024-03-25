eat_fruits=["딸기", "사과"]
eat_grams=[50, 150]

cal={"한라봉":0.5, "딸기":0.34, "바나나":0.77, "사과":0.57}


total_cal=0
idx=0
for eat_fruit in eat_fruits:
    for fruit in cal:
        if eat_fruit == fruit:
            total_cal += cal[fruit] * eat_grams[idx]
    idx+=1

print(f"총 칼로리는 {total_cal}입니다.")

#에러
