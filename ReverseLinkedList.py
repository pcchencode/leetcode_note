import os

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None



h = ListNode(1)
h.next = ListNode(2)
h.next.next = ListNode(3)
h.next.next.next = ListNode(4)
h.next.next.next.next = ListNode(5)
# print(id(h.next))
# print(id(h.next.next.next.next))

node_val = []
node_val.append(h.val)
while h.next:
	print(h.val)
	node_val.append(h.next.val)
	h = h.next
node_val.reverse()
print(node_val)



for i in range(0, len(node_val)):
	



os._exit(0)
