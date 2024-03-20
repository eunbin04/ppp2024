total1=1+2+3+4+5+6+7+8+9+10

total2=0
total2=total2+1
total2=total2+2
total2=total2+3
total2=total2+4
total2=total2+5
total2=total2+6
total2=total2+7
total2=total2+8
total2=total2+9
total2=total2+10

total=0
for i in range(10):
    #total=total+(i+1)
    total+=(i+1)
print(f"1부터 10까지 합은 {total1}입니다.")
print(f"1부터 10까지 합은 {total2}입니다.")
print(f"1부터 10까지 합은 {total}입니다.")