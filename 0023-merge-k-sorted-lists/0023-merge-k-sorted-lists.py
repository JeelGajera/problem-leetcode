# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        res = []
        for i in lists:
            tmp = i
            while tmp:
                res.append(tmp.val)
                tmp = tmp.next

        res.sort()
        
        llist = ListNode(res[0] if len(res) >= 1 else '')
        tmpll = llist
        for j in range(1,len(res)):
            llist.next = ListNode(res[j])
            llist = llist.next
        return tmpll