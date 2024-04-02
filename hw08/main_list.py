def text2list(input_text):
    tokens=input_text.split(" ")
    results=[]
    for token in tokens:
        results.append(int(token))
    return results

def average(nums):
    return sum(nums)/len(nums)

def median(nums):
    n=0
    if sorted(nums)[n]==sorted(nums)[-(n+1)]:
        return sorted(nums)[n]
    else:
        return sorted(nums)[round(len(nums)/2)]

def main():
    input_text="5 10 3 4 7"
    nums=text2list(input_text)
    print("주어진 리스트는", nums)
    print("평균값은 {:.1f}".format(average(nums)))
    print("중앙값은 {}".format(median(nums)))
    print(f"최댓값은 {max(nums)}")
    print(f"최솟값은 {min(nums)}")

if __name__=="__main__":
    main()