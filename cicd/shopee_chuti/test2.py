

def twosum(nums, sum):
    l = len(nums)
    result = list()
    for i in range(l-1):
        for j in range(i+1, l):
            if nums[i]+nums[j] == sum:
                result.append([i,j])
    print(result)
    return result

if __name__ == "__main__":
    nums = [5,3,6,9,0,1,2]
    twosum(nums,9)
