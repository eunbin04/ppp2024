def largest(a, b, c):
    largest_num=a

    if a>b:
        if a>c:
            largest_num=a
        else:
            largest_num=c
    else: #a<=b
        if b>c:
            largest_num=b
        else:
            largest_num=c
    return largest_num
        
def main():
    x1=5
    x2=7
    x3=3
    largest_num=largest(x1, x2, x3)

    print(f"가장 큰 수는 {largest_num}입니다.")


if __name__=="__main__":
    main()