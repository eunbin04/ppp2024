height_cm=int(input("키를 입력하시오."))
weight=int(input("몸무게를 입력하시오."))
height_m=height_cm/100
bmi=weight/(height_m**2)
print("키가 {}cm, 몸무게가 {}kg이면, BMI는 {:.3f}입니다.".format(height_cm, weight, bmi))

if bmi<=18.5:
    print("저체중입니다.")
elif 23<=bmi<25:
    print("비만 전단계입니다. 주의가 필요합니다.")
elif 25<=bmi<30:
    print("1단계 비만입니다.")
elif 30<=bmi<35:
    print("2단계 비만입니다.")
elif 35<=bmi:
    print("3단계 비만입니다.")
else:
    print("정상입니다.")