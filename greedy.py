def jump(nums):
    result = 0
    while len(nums) > 1:
        goal = len(nums)-1
        # print("goal", goal)
        for i in range(0, len(nums)-1):
            step = goal - i
            if nums[i] >= step:
                result += 1
                nums = nums[0:i+1]
                print(nums)
                break
    return result

print(jump([2,3,0,1,4]))