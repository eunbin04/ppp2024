x1=5
y1=4
x2=1
y2=1

x1=int(input("A의 x축 좌표를 입력하시오."))
y1=int(input("A의 y축 좌표를 입력하시오."))
x2=int(input("B의 x축 좌표를 입력하시오."))
y2=int(input("B의 y축 좌표를 입력하시오."))

import math
distance=(math.sqrt((x1-x2)**2+(y1-y2)**2))
print("두 지점 A, B 사이의 거리=>{}".format(distance))