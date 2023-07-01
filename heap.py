import os
import math
import heapq

lst = [3,1,6,5,2,4]
print(lst)
heapq.heapify(lst)
print(lst)

#自己實作 build min heap
##遍歷數組，慢慢塞入 heap，塞入的同時一直做 heapify
##換法很簡單，對最後一個idx，比較其parent，如果parent比較大就做交換
##交換完，繼續針對原本的parent做一樣的動作
##Build: O(nlogn)
##Since the time complexity to insert an element is O(log n), for n elements the insert is repeated n times, so the time complexity is O(n log n)
##Insert a Value: O(logn)
array = [3,1,6,5,2,4]
heap = []
for ele in array:
    heap.append(ele)
    idx = len(heap)-1
    while idx >0:
        parent_idx = math.ceil(idx/2)-1
        if heap[parent_idx] > heap[idx]: #若parent較大，就做交換
            heap[idx], heap[parent_idx] = heap[parent_idx], heap[idx]
        idx = parent_idx #繼續對parent做一樣的事情

print(heap)

#heap sort(簡單版本)
arr = [3,1,6,5,2,4]
heapq.heapify(arr)
sort_list = []
for _ in range(len(arr)):
    sort_list.append(heapq.heappop(arr))
arr = sort_list
print('arr', arr)

#heapq預設是 build min heap, 如何實作 max heap? -> 負號進、負號出
arr = [3,1,6,5,2,4]
arr = [-x for x in arr]
heapq.heapify(arr)
sort_list = []
for _ in range(len(arr)):
    sort_list.append(-heapq.heappop(arr))
arr = sort_list
print('arr', arr)

#本質上是個 priority queue
##這裡數字越小，代表優先度越高（可以想成deadline，要盡快完成）
pq = []
heapq.heappush(pq, 3) #先進不一定先出
heapq.heappush(pq, 1)
heapq.heappush(pq, 6)
heapq.heappush(pq, 5)
heapq.heappush(pq, 2)
heapq.heappush(pq, 4)
while pq:
    print(heapq.heappop(pq)) #會依照優先度推出