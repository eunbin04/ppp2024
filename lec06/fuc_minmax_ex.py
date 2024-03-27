def minmax(nums):
    max_num=max(nums)
    min_num=min(nums)
    return min_num, max_num

def main():
    x=[3,7,25,10,2,13]
    mn,mx=minmax(x)
    print(f"최솟값은 {mn}이고, 최댓값은 {mx}입니다.")


if __name__=="__main__":
    main()