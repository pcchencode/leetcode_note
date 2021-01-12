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


r_v = ListNode(node_val[0])
target = r_v
i=1
while i < len(node_val):
    print(node_val[i])
    target.next = ListNode(node_val[i])


    target = r_v.next
    i = i+1
print(r_v.val)
print(r_v.next.val)
print(r_v.next.next.val)


os._exit(0)
