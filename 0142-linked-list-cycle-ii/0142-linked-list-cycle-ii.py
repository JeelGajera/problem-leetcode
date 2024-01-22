# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return
        
        slow = head
        fast = head

        while True:
            slow = slow.next
            if fast == None:
                return
            else:
                fast = fast.next
                if fast:
                    fast = fast.next

            if slow == fast:
                break

        slow = head
        while slow != fast:
            slow = slow.next
            if fast:
                fast = fast.next

        return slow
