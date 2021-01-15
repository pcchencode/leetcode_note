import os
# import queue

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# 使用dfs搜尋，只要沒碰到leaf就+1; 只要碰到leaf就歸0
c1l = TreeNode(3)
c1r = TreeNode(4)
c2l = TreeNode(4)
c2r = TreeNode(3)
c1 = TreeNode(val=2, left=c1l, right=c1r)
c2 = TreeNode(val=2, left=c2l, right=c2r)
r = TreeNode(val=1, left=c1, right=c2)