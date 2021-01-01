class Node:

    def __init__(self, x):
        self.data = x
        self.next = None

class MyLinkedList:

    def __init__(self):
        self.head = None
        

    def get(self, index: int) -> int:
        """
        Get the value of the index-th node in the linked list. If the index is invalid, return -1.
        """
        if index < 0:
            print('index is invalid')
            return -1
        current = self.head
        for i in range(0, index):
            current = current.next
        if current is None:
            return -1
        return current.data    
        

    def addAtHead(self, val: int) -> None:
        """
        Add a node of value val before the first element of the linked list. After the insertion, the new node will be the first node of the linked list.
        """
        new_node = Node(val)
        new_node.next = self.head
        self.head = new_node
        

    def addAtTail(self, val: int) -> None:
        """
        Append a node of value val to the last element of the linked list.
        """
        new_node = Node(val)
        if self.head is None:
            self.head = new_node
            return
        
        current = self.head
        while (current.next):
            current = current.next
        
        current.next = new_node
        

    def addAtIndex(self, index: int, val: int) -> None:
        """
        Add a node of value val before the index-th node in the linked list. If index equals to the length of linked list, the node will be appended to the end of linked list. If index is greater than the length, the node will not be inserted.
        """
        if index < 0:
            print('Invalid index')
            return

        current = self.head
        if index == 0:
            new_node = Node(val)
            new_node.next = current
            self.head = new_node
            return

        new_node = Node(val)
        
        for i in range(index-1):
            current = current.next

        new_node.next = current.next
        current.next = new_node


    def deleteAtIndex(self, index: int) -> None:
        """
        Delete the index-th node in the linked list, if the index is valid.
        """
        if index < 0:
            print('Invalid index')
            return
        
        current = self.head
        if index == 0:
            self.head = current.next
            return
        
        for i in range(index-1):
            current = current.next
        
        if current is None:
            return
        if current.next is None:
            return
        current.next = current.next.next

    def printLL(self) -> None:
        current = self.head
        i = 0
        while (current):
            print(i, current.data)
            current = current.next  
            i+=1      

# Your MyLinkedList object will be instantiated and called as such:

if __name__=='__main__': 
    ll = MyLinkedList()
    ll.addAtHead(1)

    ll.addAtTail(3)

    value = ll.get(0)
    print('value at index 0 is', value)

    ll.addAtIndex(1,2)

    ll.deleteAtIndex(1)
    ll.printLL()
