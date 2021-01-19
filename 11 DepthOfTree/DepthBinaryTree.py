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

c1l = None
c1r = None
c2l = None
c2r = TreeNode(val=4, left=None, right=5)
c1 = None
c2 = TreeNode(val=3, left=c2l, right=c2r)
r4 = TreeNode(val=2, left=c1, right=c2)




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
            if not isleaf(node):
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

def bfs_1leaf(root):
    result = []
    q = queue.Queue()
    q.put(root)
    while q.qsize()>0:
        node = q.get()
        if type(node) is TreeNode:
            result.append(node.val)
            if not isleaf(node):
                if node.left != None:
                    q.put(node.left)
                else:
                    q.put("NONE")
                if node.right != None:
                    q.put(node.right)
                else:
                    q.put("NONE")
            else:
                break
        else:
            result.append(node)
    return result

# print(bfs_tra(r1)); print(bfs_1leaf(r1))
# print(bfs_tra(r2)); print(bfs_1leaf(r2))
# print(bfs_tra(r3)); print(bfs_1leaf(r3))

# def depth(root):
#     bfs = bfs_tra(root)
#     first_leaf = bfs_1leaf(root)
#     print(bfs)
#     print(first_leaf)
#     i = 1
#     n = 1
#     h = 1
#     while True:
#         if len(bfs[0:i]) < len(first_leaf):
#             # print(i)
#             i = i + n*2
#             n = n*2
#             h += 1
#         else:
#             # print(i)
#             break
#     print(h)
#     return h

# depth(r4)


# n = 1
# i = 1
# while n < 10 :
#   print(i)
#   i = i + n*2
#   n = n*2


def solution(root):
    if root is None:
        return 0
    if root.right is None and root.left is None:
        return 1

    if root.left is None:
        return solution(root.right)+1

    if root.right is None:
        return solution(root.left)+1

    return min(solution(root.left), solution(root.right))+1

def solution(root):
    if root is None:
        return 0
    
    if root.right is None and root.left is None:
        return 1
    elif root.left is None:
        return solution(root.right)+1
    elif root.right is None:
        return solution(root.left)+1
    # 如果左右都有subtree，這時該往哪裡鑽？
    # Ans: 兩邊都鑽，但是 return 的值要取一個 min 後，才+1
    else:
        return min(solution(root.left), solution(root.right)) + 1

print(solution(r3))







