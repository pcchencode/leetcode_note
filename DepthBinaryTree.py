import os
# import queue

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# 使用dfs搜尋，只要沒碰到leaf就+1; 只要碰到leaf就歸0