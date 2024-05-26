import random

def gugudan():
    a=random.randint(1, 9)
    b=random.randint(1, 9)
    return a,b,a*b

def main():
    how_many=int(input("몇 문제를 출제할까요?"))

    correct_answer=0
    for i in range(how_many):
        a,b,hidden_answer=gugudan()
        showen_answer=int(input(f"{i+1}:{a}x{b}="))
        if showen_answer==hidden_answer:
            print("축하합니다! 정답입니다.")
            correct_answer+=1
        else:
            print(f"틀렸습니다. 정답은 {hidden_answer}입니다.")
    print(f"점수는 {correct_answer}/{how_many}입니다.")

if __name__=="__main__":
    main()