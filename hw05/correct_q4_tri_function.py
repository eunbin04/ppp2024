print("각   라디안     sin       cos       tan")

angle=100

import math
for i in range(angle):
    if (i)%15==0:
        print(f"{i}   {math.radians(i):.4f}    {math.sin(math.radians(i)):.4f}    {math.cos(math.radians(i)):.4f}    {math.tan(math.radians(i)):.4f}")