from collections import deque
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []

n1 = Node(val=1)
n2 = Node(val=2)
n3 = Node(val=3)
n4 = Node(val=4)
n5 = Node(val=5)
n6 = Node(val=6)
n1.neighbors = [n2, n3]
n2.neighbors = [n1, n4]
n3.neighbors = [n1, n5]
n4.neighbors = [n2, n6]
n5.neighbors = [n3, n6]
n6.neighbors = [n4, n5]

def dfs(node, visit_set):
    #終止條件
    if node in visit_set:
        return

    visit_set.add(node)
    print(node.val) #走訪
    for neib in node.neighbors:
        dfs(neib, visit_set)
dfs(n1, set())
print("===========")

def bfs(node, visit_set):
    q = deque([node])
    while q:
        nod = q.pop()
        if nod in visit_set:
            continue
        else:
            visit_set.add(nod)
        print(nod.val)
        for neib in nod.neighbors:
            q.appendleft(neib)
bfs(n1, set())

