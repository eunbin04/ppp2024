def get_range_list(num):
    for i in range(num):
        print(i+1)
    
def main():
    x=int(input("숫자를 입력하시오:"))
    get_range_list(x)

if __name__=="__main__":
    main()