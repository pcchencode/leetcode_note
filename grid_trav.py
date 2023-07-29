import os
from collections import deque


grid = [[1,2,3],[8,9,4],[7,6,5]]
# [
#     [1,2,3],
#     [8,9,4],
#     [7,6,5]
# ]
ROWS, COLS = len(grid), len(grid[0])
        
# DFS: recursion
def dfs(r, c, grid, visit_set):
    #終止條件
    if r<0 or c<0 or r==ROWS or c==COLS or (r,c) in visit_set:
        return

    visit_set.add((r, c)) #因為Graph中可能會回訪，要避免無窮遞迴
    print(grid[r][c]) #走訪
    dfs(r-1, c, grid, visit_set)
    dfs(r+1, c, grid, visit_set)
    dfs(r, c-1, grid, visit_set)
    dfs(r, c+1, grid, visit_set)
dfs(0, 0, grid, set())
print("=========")

# DFS: stack
def dfs_stack(r, c, grid, visit_set):
    stack = [(r,c)]
    while stack:
        curr = stack.pop()
        row, col = curr[0], curr[1]
        if (row, col) in visit_set:
            continue
        else:
            visit_set.add((row, col))
        print(grid[row][col]) #走訪
        if col+1<ROWS:
            stack.append((row, col+1))
        if col-1>=0:
            stack.append((row, col-1))
        if row+1<ROWS:
            stack.append((row+1, col))
        if row-1>=0:
            stack.append((row-1, col))
dfs_stack(0, 0, grid, set())
print("=======")

# BFS
def bfs(r,c, grid, visit_set):
    q = deque([(r, c)])
    while q:
        curr = q.pop()
        row, col = curr[0], curr[1]
        if (row, col) in visit_set:
            continue
        else:
            visit_set.add((row, col))
        print(grid[row][col]) #走訪
        if row-1>=0:
            q.appendleft((row-1, col))
        if row+1<ROWS:
            q.appendleft((row+1, col))
        if col-1>=0:
            q.appendleft((row, col-1))
        if col+1<ROWS:
            q.appendleft((row, col+1))

bfs(0, 0, grid, set())