def text2list(input_text):
    tokens = input_text.strip().split()
    results = []
    for token in tokens:
        results.append(token)
    return results

def count(nums):
    natural_nums=0
    i=0
    while i<len(nums):
        try:
            for lines in nums[i]:
                num=int(lines)
                if num>0:
                    natural_nums+=1
                    break
        except ValueError:
            pass
        i+=1
    return natural_nums
        
def average(nums):
    sum_nums=0
    natural_nums=0
    i=0
    while i<len(nums):
        try:
            num=int(nums[i])
            if num>0:
                sum_nums+=num
                natural_nums+=1
        except ValueError:
            pass
        i+=1
    if natural_nums==0:
        return 0
    else:
        return sum_nums/natural_nums

def main():
    input_list=[]
    while True:
        input_text=input("X=")
        if input_text=='-1':
            break
        nums=text2list(input_text)
        input_list.extend(nums)

    print(f"입력된 값은 {input_list}입니다. 총 {count(input_list)}개의 자연수가 입력되었고, 평균은 {average(input_list):.1f}입니다.")

if __name__=="__main__":
    main()
