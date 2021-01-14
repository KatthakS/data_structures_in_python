"""
Reverse a singly linked list.

Example:

Input: 1->2->3->4->5->NULL
Output: 5->4->3->2->1->NULL
"""
#LeetCode Question 206 - Easy
#LeetCode Top 100 Questions

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def __init__(self):
        self.head = None

    def reverseList(self) -> ListNode:
        curr = self.head
        prev = None
        while curr != None:
            next_temp = curr.next
            curr.next = prev
            prev = curr
            curr = next_temp
        return prev
    
    def addAtTail(self, val: int) -> None:
        """
        Append a node of value val to the last element of the linked list.
        """
        new_node = ListNode(val)
        if self.head is None:
            self.head = new_node
            return
        
        current = self.head
        while (current.next):
            current = current.next
        
        current.next = new_node
        
    
    def printLL(self, head) -> None:
        current = head
        if current is None:
            current = self.head
        i = 0
        while (current):
            print(i, current.val)
            current = current.next  
            i+=1

ob = Solution()
ob.addAtTail(1)
ob.addAtTail(2)
ob.addAtTail(3)
print("Actual List:")
ob.printLL(None)
print("Reversed List:")
prev = ob.reverseList()
ob.printLL(prev)
