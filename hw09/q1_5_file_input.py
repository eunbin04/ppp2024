def average(nums):
    return sum(nums)/len(nums)

def median(nums):
    sorted_nums=sorted(nums)
    return sorted_nums[len(nums)//2]

def read_file_multi_line(filename):
    data=[]
    with open(filename) as f:
        lines=f.readlines()
        for line in lines:
            text=line.split()
            for word in text:
                num=word.strip()
                data.append(int(num))
    return data

def main():
    nums=read_file_multi_line("hw09/numbers.txt")
    print("총 숫자의 개수는", len(nums))
    print("평균값은 {:.1f}".format(average(nums)))
    print(f"최댓값은 {max(nums)}")
    print(f"최솟값은 {min(nums)}")
    print("중앙값은 {}".format(median(nums)))

if __name__=="__main__":
    main()