def average(nums):
    #방법1 return sum(nums)/len(nums)
    #방법2
    total=0
    count=0
    for num in nums:
        total+=num
        count+=1
    return total/count

def main():
    nums=[3,5,10,15,7]
    print(f"주어진 리스트의 평균은 {average(nums):.1f}입니다.")

if __name__=="__main__":
    main()