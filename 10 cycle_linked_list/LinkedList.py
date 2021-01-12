import os

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


#n1 = ListNode(3)
#n1.next = ListNode(4)
#n2 = ListNode(3)
#n2.next = ListNode(4)
#print(id(n1))
#print(id(n2))
#print(n1.next.next)
#os._exit(0)


h = ListNode(3)
h.next = ListNode(2)
h.next.next = ListNode(0)
h.next.next.next = ListNode(4)
h.next.next.next.next = h.next
# print(id(h.next))
# print(id(h.next.next.next.next))

# h = ListNode(3)
# h.next = ListNode(2)
# h.next.next = ListNode(0)
# h.next.next.next = ListNode(4)
# h.next.next.next.next = ListNode(2)
# print(id(h.next))
# print(id(h.next.next.next.next))

# print(h.next.val)

addr_lst = []
addr_lst.append(id(h))
if h: # 如果為空節點，就一定沒有cycle
    while h.next != None:
        # print(h)
        if id(h.next) not in addr_lst:
            print(id(h.next))
            addr_lst.append(id(h.next))
        else:
            print("cycle!!")
            break
        if h.next != None:
           h = h.next

print(addr_lst)


os._exit(0)
