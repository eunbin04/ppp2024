import time

def main():
    x=int(input("카운트다운할 시간을 입력하세요:"))
    count=x

    while True:
        print(f"카운트다운...{count}") 
        time.sleep(1)
        count-=1
        if count<=0:
            break

    print("Bomb!!")

if __name__=="__main__":
    main()