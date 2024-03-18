import math

x1=0
y1=0
x2=3
y2=4

x1=int(input("A의 x축 좌표를 입력하시오."))
y1=int(input("A의 y축 좌표를 입력하시오."))
x2=int(input("B의 x축 좌표를 입력하시오."))
y2=int(input("B의 y축 좌표를 입력하시오."))

dist = math.sqrt((x2-x1)**2+(y2-y1)**2)

if dist>1:
    print("거리는 {}입니다.".format(dist))
else:
    print("거리가 너무 가깝습니다.")