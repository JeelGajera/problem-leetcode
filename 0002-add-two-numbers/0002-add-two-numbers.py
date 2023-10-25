# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        num1 = ""
        num2 = ""
        i = l1
        while i:
            num1 += str(i.val)
            i = i.next
        num1 = num1[::-1]

        j = l2
        while j:
            num2 += str(j.val)
            j = j.next
        num2 = num2[::-1]

        res = str(int(num1) + int(num2))
        res = res[::-1]
        l_sum = ListNode(0,None)
        current = l_sum
        for char in res:
            val = int(char)
            node = ListNode(val, None)
            current.next = node
            current = current.next
        l_sum = l_sum.next
        return l_sum