import os
import queue

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# 使用dfs搜尋，只要沒碰到leaf就+1; 只要碰到leaf就扣1，並且將當時走道的depth輸入一個list
c1l = None
c1r = None
c2l = TreeNode(15)
c2r = TreeNode(7)
c1 = TreeNode(val=9, left=c1l, right=c1r)
c2 = TreeNode(val=20, left=c2l, right=c2r)
r1 = TreeNode(val=3, left=c1, right=c2)

c1l = TreeNode(4)
c1r = None
c2l = None
c2r = TreeNode(5)
c1 = TreeNode(val=3, left=c1l, right=c1r)
c2 = TreeNode(val=2, left=c2l, right=c2r)
r2 = TreeNode(val=1, left=c1, right=c2)

c1l = TreeNode(4)
c1r = TreeNode(5)
c2l = None
c2r = None
c1 = TreeNode(val=3, left=c1l, right=c1r)
c2 = TreeNode(val=2, left=c2l, right=c2r)
r3 = TreeNode(val=1, left=c1, right=c2)


def isleaf(r):
    if r.left:
        return False
    elif r.right:
        return False
    else:
        return True


def dfs_left(root):
    result = []
    stack = []
    depth = 1
    stack.append(root)
    while len(stack)>0:
        node = stack.pop()
        if node:
            if isleaf(node):
                return depth
            else:
                depth += 1
        else:
            return 0
        
        if type(node) is TreeNode:
            result.append(node.val)

            if node.right != None:
                stack.append(node.right)

            if node.left != None:
                stack.append(node.left)
        else:
            result.append(node)
    return depth






