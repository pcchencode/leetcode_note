import os
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class MyLinkedList:
    def __init__(self):
        self.head = None

    def get_length(self):
        res = 0; curr = self.head
        while curr:
            res += 1
            curr = curr.next
        return res
            
    def get(self, index: int) -> int:
        if not self.head:
            return -1
        length = self.get_length()
        # print("length:", length)
        if index > length -1:
            return -1 
        curr = self.head
        for i in range(index):
            curr = curr.next
        return curr.val

    def addAtHead(self, val: int) -> None:
        if self.head:
            result = ListNode(val)
            result.next = self.head
            self.head = result
        else:
            self.head = ListNode(val)
        pass

    def addAtTail(self, val: int) -> None:
        result = ListNode(0)
        curr = result
        while self.head:
            curr.next = ListNode(self.head.val)

            curr = curr.next
            self.head = self.head.next
        if self.head is None:
            curr.next = ListNode(val)
        self.head = result.next
        pass

    def addAtIndex(self, index: int, val: int) -> None:
        length = self.get_length()
        if index > length:
            return
        
        result = ListNode(0)
        curr = result
        for i in range(index):
            curr.next = ListNode(self.head.val)
            curr = curr.next
            self.head = self.head.next
        remain_node = self.head
        curr.next = ListNode(val)
        curr.next.next = remain_node

        self.head = result.next
        pass

    def deleteAtIndex(self, index: int) -> None:
        length = self.get_length()
        if index > length-1:
            return
        result = ListNode(0)
        curr = result
        for i in range(index):
            curr.next = ListNode(self.head.val)
            curr = curr.next
            self.head = self.head.next
        remain_node = self.head.next
        curr.next = remain_node

        self.head = result.next


# Your MyLinkedList object will be instantiated and called as such:
obj = MyLinkedList()
obj.addAtHead(4)
obj.addAtHead(1)
obj.addAtHead(5)
obj.addAtTail(9)
obj.addAtTail(6)
obj.addAtTail(3)
obj.addAtTail(2)
obj.addAtIndex(2, 87)
obj.deleteAtIndex(5)
# a = obj.get(2)
# print(a)
print("===")
for i in range(8):
    print(obj.get(i))


# print(obj.head.next.next.val)
# print(obj.get(1))
# print(obj.get(2))
# print(obj.get(3))

# print(obj.length)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)

os._exit(0)


class MyLinkedList:

    def __init__(self):
        self.arr = [] #感覺本身就是要存一個資料結構

    def get(self, index: int) -> int:
        if index > len(self.arr)-1:
            pass
        else:
            return self.arr[index]

    def addAtHead(self, val: int) -> None:
        self.arr.insert(0, val)
        pass

    def addAtTail(self, val: int) -> None:
        self.arr.append(val)
        pass

    def addAtIndex(self, index: int, val: int) -> None:
        self.arr.insert(index, val)
        pass

    def deleteAtIndex(self, index: int) -> None:
        if index > len(self.arr)-1:
            pass
        else:
            self.arr.pop(index)
        pass


# Your MyLinkedList object will be instantiated and called as such:
obj = MyLinkedList()
# param_1 = obj.get(index)
print(obj.get(1))
obj.addAtHead(4)
print(obj.get(1))
obj.addAtHead(1)
obj.addAtHead(5)
obj.deleteAtIndex(3)
obj.addAtHead(7)
print(obj.get(3))
print(obj.get(3))
print(obj.get(3))
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)

os._exit(0)


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

# addr_lst = []
# addr_lst.append(id(h.val))
# while h.next != None:
# 	# print(h)
# 	if id(h.next.val) not in addr_lst:
# 		addr_lst.append(id(h.next.val))
# 	else:
# 		print("cycle!!")
# 		break
# 	if h.next != None:
# 		h = h.next

# print(addr_lst)

a = 1
b = 1
b = 2
print(id(a))
print(a)
print(id(b))
print(b)
os._exit(0)
