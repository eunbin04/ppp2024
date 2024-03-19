import math
r=int(input("원의 반지름을 입력하세요."))
area=math.pi *r**2
circum=2*r*math.pi
print("반지름이 {}인 원의 면적은 {:.2f}이고, 원의 둘레는 {:.1f}입니다.".format(r,area,circum))