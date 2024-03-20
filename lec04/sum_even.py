n=250
total=0
for i in range(n):
    if (i+1)%2==0:
        total=total+(i+1)

print(f"1부터 {n}까지 합은 {total:,}입니다.")