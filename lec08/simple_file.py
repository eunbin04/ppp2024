def read_file(filename):
    with open(filename) as f:
        text=f.readline().strip()
        return text

def main():
    nums=read_file("lec08/number1.txt")
    print("주어진 리스트는", nums)

if __name__=="__main__":
    main()