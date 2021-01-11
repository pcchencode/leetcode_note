import os

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

h = ListNode(3)
h.next = ListNode(2)
h.next.next = ListNode(0)
h.next.next.next = ListNode(4)
h.next.next.next.next = h.next

print(h.next.val)


os._exit(0)
