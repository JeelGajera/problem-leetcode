# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:

        cur = head
        length = 0
        while cur.next != None:
            length += 1
            cur = cur.next
        else:
            length += 1

        target = length - n
        prev = ListNode()
        cur = head

        if target == 0:
            head = cur.next
        else:
            for i in range(target):
                if i == target-1:
                    prev = cur
                cur = cur.next
            prev.next = cur.next
        return head