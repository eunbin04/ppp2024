def f2c(temp_f):
    return (temp_f-32)*5/9

def main():
    temp_f=100
    print("{}F=>{}C".format(temp_f,f2c(temp_f)))

if __name__=="__main__":
    main()