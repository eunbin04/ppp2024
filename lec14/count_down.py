import time

def main():
    #x=int(input())
    count=5

    while True:
        print(f"카운트다운...{count}", end="\r")  #end는 한줄에 표현
        time.sleep(1)
        count-=1
        if count<=0:
            break

    print()  #end를 썼을때 겹치지 않게 하려고
    print("!!Bomb!!")

if __name__=="__main__":
    main()