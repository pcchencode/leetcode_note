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