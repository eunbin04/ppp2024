hanlabog=int(input("한라봉의 섭취량을 입력하시오."))
strawberry=int(input("딸기의 섭취량을 입력하시오."))
banana=int(input("바나나의 섭취량을 입력하시오."))
mango=int(input("망고의 섭취량을 입력하시오."))
grape=int(input("포도의 섭취량을 입력하시오."))

calories={"한라봉":50, "딸기":34, "바나나":77, "망고":61, "포도":60}
total_calories=(calories["한라봉"]*hanlabog+calories["딸기"]*strawberry+calories["바나나"]*banana+calories["망고"]*mango+calories["포도"]*grape)/100

print("총 칼로리 섭취량=>{:.2f}".format(total_calories))

#밥 한 공기(140g)의 칼로리(235㎉) 기준으로 총 칼로리 섭취량 비교
rice_calories=(total_calories/235)
print("밥 {:.1f}공기정도의 양입니다.".format(rice_calories))