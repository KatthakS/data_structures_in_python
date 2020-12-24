"""
 You are given two non-empty linked lists representing two non-negative integers. 
 The digits are stored in reverse order, and each of their nodes contains a single digit. 
 Add the two numbers and return the sum as a linked list.
"""
#Leetcode top 100 Liked Questions

# Definition for singly-linked list.
class ListNode:
     def __init__(self, val=0, next=None):
         self.val = val
         self.next = next

class Solution:
   
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        resultLL = ListNode(0)
        result_tail = resultLL
        carry = 0

        while l1 or l2 or carry:
            #print (l1.val, l2.val)
            if l1 != None:
                val1 = l1.val
            else:
                val1 = 0
            if l2 != None:
                val2 = l2.val
            else:
                val2 = 0

            carry, out = divmod(carry+val1+val2, 10)
            result_tail.next = ListNode(out)
            result_tail = result_tail.next
            if l1:
                l1= l1.next
            else:
                l1 = None
            if l2:
                l2 = l2.next
            else:
                l2 = None
        return resultLL.next

    def printLL(self, L1:ListNode):
        while L1:
            print (L1.val)
            L1 = L1.next

L1 = ListNode(2)
L1.next = ListNode(4)
L1.next.next =  ListNode(3)

L2 = ListNode(5)
L2.next = ListNode(6)
L2.next.next =  ListNode(4)

result = Solution()
L3 = result.addTwoNumbers(L1, L2)
result.printLL(L3)
