def gugudan(dan):
    for i in range(9):
        print(f"{dan}*{i+1}={dan*(i+1)}")

def main():
    dan=int(input("구구단을 출력할 숫자를 입력하시오:"))
    gugudan(dan)

if __name__=="__main__":
    main()