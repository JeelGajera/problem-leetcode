# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        temp = ListNode(-1)
        temp.next = head
        cur = temp
        while cur.next and cur.next.next:
            first = cur.next
            second = cur.next.next
            #swaping
            first.next = second.next
            second.next = first
            cur.next = second

            cur = cur.next.next
        return temp.next