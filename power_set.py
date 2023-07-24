def helper(sets, target):
    res = []
    for ele in sets:
        # print(ele, target)
        tmp = ele.copy()
        tmp.append(target)
        # print(ele)
        res.append(tmp)
    # print(sets,res)
    # res.append([target])
    # print(sets+res)
    return sets+res

# helper([[]], target=1)
# helper([[], [1]], target=2)
# helper([[], [2], [1, 2], [2]], target=3)
nums = [1,2,3,4]
res = [[]]
for t in nums:
    res = helper(res, t)
print(res)

##回溯正解
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        self.result = []
        self.path = [[]]

        def backtrack(nums):
            #終止條件
            if len(nums)==0:
                return

            for i in range(0, len(nums)):
                cand = nums[i]; remains = nums[i+1:]
                res = self.path[-1].copy(); res.append(cand)
                self.path.append(res)
                backtrack(remains)

                self.result.append(self.path[-1].copy()) #回溯時放入
                self.path = self.path[:-1]
            
        backtrack(nums)
        self.result.append([])
        return self.result