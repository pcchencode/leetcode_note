import os
import math
import heapq

lst = [3,1,6,5,2,4]
print(lst)
heapq.heapify(lst)
print(lst)

#自己實作 build min heap
array = [3,1,6,5,2,4]
heap = []
for ele in array:
    heap.append(ele)
    idx = len(heap)-1
    while idx >0:
        parent_idx = math.ceil(idx/2)-1
        if heap[parent_idx] > heap[idx]:
            heap[idx], heap[parent_idx] = heap[parent_idx], heap[idx]
        idx = parent_idx
        # print(heap)
print(heap)