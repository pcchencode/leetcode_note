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
    # print(h.val)
    node_val.append(h.next.val)
    h = h.next
node_val.reverse()
print(node_val)


r_v = ListNode(node_val[0])
target = r_v
i=1
while i < len(node_val):
    # print(target.val)
    target.next = ListNode(node_val[i])
    target = target.next
    i = i+1

print(r_v.val)
print(r_v.next.val)
print(r_v.next.next.val)
print(r_v.next.next.next.val)
print(r_v.next.next.next.next.val)

def reverseList(head):
    if head:
        node_val = []
        node_val.append(head.val)
        while head.next:
            # print(head.val)
            node_val.append(head.next.val)
            head = head.next
        node_val.reverse()
        print(node_val)

        r_v = ListNode(node_val[0])
        target = r_v
        i=1
        while i < len(node_val):
            # print(target.val)
            target.next = ListNode(node_val[i])
            target = target.next
            i = i+1
    else:
        r_v = head
    
    return r_v


os._exit(0)
