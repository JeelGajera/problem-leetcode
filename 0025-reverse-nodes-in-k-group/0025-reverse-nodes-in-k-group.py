# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if head == None: return None
        prev, cur, next = None, head, None
        count = k
        while cur != None and count > 0:
            next = cur.next
            cur.next = prev
            prev = cur
            cur = next
            count -= 1
        if cur == None and count > 0:
            cur = prev
            prev = None
            next = None
            while cur != None:
                next = cur.next
                cur.next = prev
                prev = cur
                cur = next
        if count > 0:
            return prev
        else:
            head.next = self.reverseKGroup(cur, k)
        return prev