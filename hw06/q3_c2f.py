def c2f(temp_c):
    return temp_c*1.8+32

def main():
    temp_c=int(input("섭씨온도를 입력하시오:"))
    print("{}℃ =>{:.3f}℉".format(temp_c,c2f(temp_c)))

if __name__=="__main__":
    main()