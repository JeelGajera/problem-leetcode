import random

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:

    def __init__(self, head: Optional[ListNode]):
        self.elems = []       
        cur = head
        while cur.next != None:
            self.elems.append(cur.val)
            cur = cur.next
        else:
            self.elems.append(cur.val)
        

    def getRandom(self) -> int:
        return random.choice(self.elems)


# Your Solution object will be instantiated and called as such:
# obj = Solution(head)
# param_1 = obj.getRandom()