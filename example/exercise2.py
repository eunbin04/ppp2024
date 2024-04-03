def read_file_multi_line(filename):
    data=[]
    with open(filename) as f:
        lines=f.readlines()
        for line in lines:
            text=line.strip()
            data.append(int(text))
    return data

def main():
    nums=read_file_multi_line("lec08/number2.txt")
    print("주어진 리스트는", nums)

if __name__=="__main__":
    main()