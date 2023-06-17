def findMode(nums):
    mode = []
    max_count = 0
    for i in range(0, len(nums)-1):
        dup_count = 0
        j = i+1
        if nums[j] != nums[i]:
            continue
        else:
            dup_count += 1
            if dup_count > max_count:
                max_count = dup_count
                mode.clear()
                mode.append(nums[i])
            elif dup_count == max_count:
                mode.append(nums[i])
            j+=1

    return mode

print(findMode([1,2,2,2,3,3,4,4,4]))
