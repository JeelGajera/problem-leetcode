class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class MyLinkedList:

    def __init__(self):
        self.head = None
        self.size = 0

    def get(self, index: int) -> int:
        if index >= self.size or index < 0 or self.head is None:
            return -1

        cur = self.head
        for i in range(index):
            cur = cur.next
        return cur.val

    def addAtHead(self, val: int) -> None:
        node = ListNode(val)
        node.next = self.head
        self.head = node
        self.size += 1

    def addAtTail(self, val: int) -> None:
        cur = self.head
        node = ListNode(val)
        if cur is None:
            self.head = node
        else:
            while cur.next is not None:
                cur = cur.next

            cur.next = node
            
        self.size += 1


    def addAtIndex(self, index: int, val: int) -> None:
        cur = self.head
        node = ListNode(val)

        if index > self.size or index < 0:
            return

        if index == 0:
            self.addAtHead(val)
        else:
            for i in range(index-1):
                cur = cur.next

            node.next = cur.next
            cur.next = node
            self.size += 1
        

    def deleteAtIndex(self, index: int) -> None:
        cur = self.head

        if index >= self.size or index < 0:
            return

        if index == 0:
            self.head = cur.next
        else:
            for i in range(index-1):
                cur = cur.next

            cur.next = cur.next.next

        self.size -= 1


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)