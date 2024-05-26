import random

def main():
    while True:
        for hidden_answer in range(10):
            a=random.randint(1, 9)
            b=random.randint(1, 9)
            hidden_answer=a * b
        
        showen_answer=input(f"{a}x{b}=")

        if showen_answer==hidden_answer:
            print("축하합니다! 정답입니다.")
        else:
            print(f"틀렸습니다. 정답은 {hidden_answer}입니다.")

if __name__=="__main__":
    main()