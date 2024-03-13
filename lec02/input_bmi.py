#height_cm=170
#height_cm=input("키를 입력하시오.")
#height_cm=int(height_cm)
#weight=60
#weight=input("몸무게를 입력하시오.")
#weight=int(weight)

height_cm=int(input("키를 입력하시오."))
weight=int(input("몸무게를 입력하시오."))
height_m=height_cm/100
bmi=weight/(height_m**2)
print("키가 {}cm, 몸무게가 {}kg이면, BMI는 {}입니다.".format(height_cm, weight, bmi))