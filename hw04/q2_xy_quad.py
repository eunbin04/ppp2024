x=int(input("x축 좌표를 입력하시오."))
y=int(input("y축 좌표를 입력하시오."))

import math
dist=(math.sqrt(x**2+y**2))
print("원점에서의 거리=>{:.3f}".format(dist))

if x>0 and y>0:
    print("입력한 좌표는 1사분면입니다.")
elif x<0 and y>0:
    print("입력한 좌표는 2사분면입니다.")
elif x<0 and y<0:
    print("입력한 좌표는 3사분면입니다.")
elif x>0 and y<0:
    print("입력한 좌표는 4사분면입니다.")
elif x==0 and y!=0:
    print("입력한 좌표는 y좌표축 위에 있습니다.")
elif y==0 and x!=0:
    print("입력한 좌표는 x좌표축 위에 있습니다.")
else:
    print("원점입니다.")
