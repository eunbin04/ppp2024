n=3
for i in range(n):
    star=i+1
    print("*"*star)

#공백도 출력이 됨, 뒤집기
for i in range(n):
    num_star=i+1
    num_space=n-num_star
    print(" "*num_space+"*"*num_star)

for i in range(n):
    for j in range(i+1):
        print("*", end="")
    print()

#이렇게도 할 수 있다.
for i in range(n):
    print(' '*(n-i-1) + "*"*((i+1)*2-1))
