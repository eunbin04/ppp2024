upper_side=3
bottom_side=5
height=4

upper_side=int(input("윗변의 길이를 입력하시오."))
bottom_side=int(input("밑변의 길이를 입력하시오."))
height=int(input("높이를 입력하시오."))
area=((upper_side+bottom_side)/2*height)
print("사다리꼴의 면적={}".format(area))