hanlabog=100
strawberry=100
banana=100
mango=100

hanlabog=int(input("한라봉의 섭취량을 입력하시오."))
strawberry=int(input("딸기의 섭취량을 입력하시오."))
banana=int(input("바나나의 섭취량을 입력하시오."))
mango=int(input("망고의 섭취량을 입력하시오."))
hanlabog_calorie=(50/100*hanlabog)
strawberry_calorie=(34/100*strawberry)
banana_calorie=(77/100*banana)
mango_calorie=(61/100*mango)
print("한라봉의 칼로리는 {}㎉, 딸기의 칼로리는 {}㎉, 바나나의 칼로리는 {}㎉, 망고의 칼로리는 {}㎉ 입니다.".format(hanlabog_calorie, strawberry_calorie, banana_calorie, mango_calorie))