# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        left_node = ListNode()
        right_node = ListNode()
        left_head = ListNode()

        tmp = head
        i = 1
        prev = None
        while tmp:
            if i == left-1:
                left_node = tmp
                left_head = tmp.next

            while i >= left and i <= right and tmp:
                curr = tmp
                tmp = tmp.next
                curr.next = prev
                prev = curr
                i += 1
                right_node = tmp
            else:
                i += 1
                if tmp and tmp.next:
                    tmp = tmp.next
                else:
                    break
        
        if left != 1:
            left_node.next = prev
        else:
            left_head = head
            head = prev
            
        left_head.next = right_node

        return head