def text2list(input_text):
    tokens=input_text.split(" ")
    results=[]
    for token in tokens:
        results.append(int(token))
    return results

def average(nums):
    return sum(nums)/len(nums)

def median(nums):
    sorted_nums=sorted(nums)
    return sorted_nums[len(nums)//2]

def main():
    input_text="5 10 3 4 7"
    nums=text2list(input_text)
    print("주어진 리스트는", nums)
    print("평균값은 {:.1f}".format(average(nums)))
    print("중앙값은 {}".format(median(nums)))
    print(f"최댓값은 {max(nums)}")
    print(f"최솟값은 {min(nums)}")
    print(f"리스트의 마지막 값은 {nums[-1]}")

if __name__=="__main__":
    main()