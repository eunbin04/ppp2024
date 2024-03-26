def total(n):
    total=0
    for i in range(n):
        total=total+(i+1)
    return total

def main():
    n=int(input("숫자를 입력하시오:"))
    print(f"1부터 {n}까지 합은 {total(n)}입니다.")

if __name__=="__main__":
    main()