# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isValid(self, node, min_i, max_i):
        # if node:
        #     print(node.val, min_i, max_i)
        # else:
        #     print(None, min_i, max_i)
        if not node:
            return True
        # print(node.val, min_i, max_i)
        # if node.val <= min_i or node.val >= max_i:
        #     return False
        if min_i and node.val <= min_i:
            return False
        if max_i and node.val >= max_i:
            return False
        
        # print(self.isValid(node.left, min_i=min_i, max_i=node.val))
        # print(self.isValid(node.right, min_i=node.val, max_i=max_i))
        return self.isValid(node.left, min_i=min_i, max_i=node.val) and self.isValid(node.right, min_i=node.val, max_i=max_i)

    def isValidBST(self, root):
        return self.isValid(root, float('-inf'), float('-inf'))
        # return self.isValid(root, None, None)

# class Solution:
#     def isValidBST(self, root: TreeNode) -> bool:
#         def check(root, l, r):
#             if root == None:
#                 return True
#             val = root.val
#             if val <= l or val >= r:
#                 return False
#             return check(root.left, l, val) and check(root.right, val, r)
#         return check(root, float('-inf'), float('inf'))

s = Solution()
r = TreeNode(0)
r.right = TreeNode(-1)
# print(s.isValid(TreeNode(-8), 0, None))

print(s.isValidBST(r))