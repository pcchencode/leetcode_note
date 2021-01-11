import os

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

# h = ListNode(3)
# h.next = ListNode(2)
# h.next.next = ListNode(0)
# h.next.next.next = ListNode(4)
# h.next.next.next.next = h.next
# print(id(h.next))
# print(id(h.next.next.next.next))

h = ListNode(3)
h.next = ListNode(2)
h.next.next = ListNode(0)
h.next.next.next = ListNode(4)
h.next.next.next.next = ListNode(2)
# print(id(h.next))
# print(id(h.next.next.next.next))

# print(h.next.val)

addr_lst = []
addr_lst.append(id(h.val))
while h.next != None:
	# print(h)
	if id(h.next.val) not in addr_lst:
		addr_lst.append(id(h.next.val))
	else:
		print("cycle!!")
		break
	if h.next != None:
		h = h.next

print(addr_lst)


os._exit(0)
