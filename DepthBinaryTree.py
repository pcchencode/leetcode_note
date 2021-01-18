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
c1 = TreeNode(val=2, left=c1l, right=c1r)
c2 = TreeNode(val=3, left=c2l, right=c2r)
r2 = TreeNode(val=1, left=c1, right=c2)

c1l = TreeNode(4)
c1r = TreeNode(5)
c2l = None
c2r = None
c1 = TreeNode(val=2, left=c1l, right=c1r)
c2 = TreeNode(val=3, left=c2l, right=c2r)
r3 = TreeNode(val=1, left=c1, right=c2)


def isleaf(r):
    if r.left:
        return False
    elif r.right:
        return False
    else:
        return True


# def dfs_left(root):
#     result = []
#     stack = []
#     stack.append(root)
#     while len(stack)>0:
#         node = stack.pop()
        

#         # dfs process
#         if type(node) is TreeNode:
#             result.append(node.val)
#             if not isleaf(node):
#                 if node.right != None:
#                     stack.append(node.right)
#                 else:
#                     stack.append("NONE")
#                 if node.left != None:
#                     stack.append(node.left)
#                 else:
#                     stack.append("NONE")
#         else:
#             result.append(node)

#     return result

# 廣度優先搜尋：queue
## bfs 第一個碰到的leaf就是最淺的位置
def bfs_tra(root):
    result = []
    q = queue.Queue()
    q.put(root)
    while q.qsize()>0:
        node = q.get()
        if type(node) is TreeNode:
            result.append(node.val)
            if node.left != None:
                q.put(node.left)
            else:
                q.put("NONE")
            if node.right != None:
                q.put(node.right)
            else:
                q.put("NONE")
        else:
            result.append(node)
    return result

print(bfs_tra(r1))






