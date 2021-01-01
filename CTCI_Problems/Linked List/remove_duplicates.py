# Write code to remove duplicates from unsorted linked list
# Cracking the coding interview - Linked List - Problem_1

class list_node:
    def __init__(self, val = 0, next = None):
        self.val = val
        self.next = next

class solution:
    def remove_duplicates(self, l1: list_node) -> list_node:
        checking_dict = {}
        if not l1:
            return None
        checking_dict[l1.val] = l1.val
        current = l1
        while current.next is not None:
            if current.next.val in checking_dict:
                current.next = current.next.next
            else:
                checking_dict[l1.val] = l1.val
                current = current.next
        return l1


    def print_linkedlist(self, l1: list_node):
        while l1:
            print(l1.val)
            l1 = l1.next

ll = list_node(3)
ll.next = list_node(1)
ll.next.next = list_node(3)
ob = solution()
ob.print_linkedlist(ll)
new_ll = ob.remove_duplicates(ll)
ob.print_linkedlist(new_ll)

            


