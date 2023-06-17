def findMode(nums):
    mode = []
    max_count = 0
    for i in range(0, len(nums)-1):
        dup_count = 0
        j = i+1
        while j < len(nums):
            if nums[j] != nums[i]:
                break
            else:
                dup_count += 1
                if dup_count > max_count:
                    max_count = dup_count
                    mode.clear()
                    mode.append(nums[i])
                elif dup_count == max_count:
                    mode.append(nums[i])
                j+=1
    if len(mode)==0:
        return nums

    return mode

print(findMode([1,2,2,2,3,3,4,4,4]))
print(findMode([1,2,2,4,5,5]))
print(findMode([1,2,2,4,5,5,5,5,5,6]))
print(findMode([1,2,3,4,5,6]))
print(findMode([1,1,1]))
