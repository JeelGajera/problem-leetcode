# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head or k == 0 or (head.next == None):
            return head

        count = 1 if head else 0
        cur = head
        while cur.next != None:
            count += 1
            cur = cur.next

        k %= count # effective rotations
        
        while k != 0:
            i = 0
            cur = head
            last_node = ListNode()
            while i < count and cur:
                i += 1
                if i == count-1:
                    last_node = cur.next
                    cur.next = None
                cur = cur.next

            last_node.next = head
            head = last_node
            k -= 1

        return head