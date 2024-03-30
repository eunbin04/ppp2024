def average(list):
    return sum(list)/len(list)

def main():
    x=[1,3,5,7,9,11,13]
    print(f"평균은 {average(x)}입니다.")

if __name__=="__main__":
    main()