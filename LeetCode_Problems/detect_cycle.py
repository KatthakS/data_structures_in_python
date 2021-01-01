#Given head, the head of a linked list, determine if the linked list has a cycle in it.

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        if head == None or head.next == None:
            return False
        slow = head
        fast = head.next
        
        while fast != slow:
            if fast == None or slow == None or fast.next == None or fast.next.next == None:
                return False
            slow = slow.next
            fast = fast.next.next
        return True
            