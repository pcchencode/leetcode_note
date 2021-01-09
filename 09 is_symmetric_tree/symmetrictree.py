import os
# import queue
# https://ithelp.ithome.com.tw/articles/10213280

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def dfs_right(root):
    result = []
    stack = []
    stack.append(root)
    while len(stack)>0:
        node = stack.pop()
        
        if type(node) is TreeNode:
            result.append(node.val)

            if node.left != None:
                stack.append(node.left)
            else:
                stack.append("NONE")
            if node.right != None:
                stack.append(node.right)
            else:
                stack.append("NONE")
        else:
            result.append(node)
    return result

def dfs_left(root):
    result = []
    stack = []
    stack.append(root)
    while len(stack)>0:
        node = stack.pop()
        
        if type(node) is TreeNode:
            result.append(node.val)

            if node.right != None:
                stack.append(node.right)
            else:
                stack.append("NONE")
            if node.left != None:
                stack.append(node.left)
            else:
                stack.append("NONE")
        else:
            result.append(node)
    return result

def isSymmetric(root):
    result = False
    left_tra = dfs_left(root)
    right_tra = dfs_right(root)
    if left_tra == right_tra:
        result = True
    return result


# Example from leetcode
c1l = TreeNode(3)
c1r = TreeNode(4)
c2l = TreeNode(4)
c2r = TreeNode(3)
c1 = TreeNode(val=2, left=c1l, right=c1r)
c2 = TreeNode(val=2, left=c2l, right=c2r)
r = TreeNode(val=1, left=c1, right=c2)

# recognize if the TreeNode is symmetric
print(isSymmetric(r))