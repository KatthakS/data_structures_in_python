"""
Design your implementation of the circular queue. 
The circular queue is a linear data structure in which the operations are performed based on FIFO (First In First Out)
 principle and the last position is connected back to the first position to make a circle. 
 It is also called "Ring Buffer".
 """

class MyCircularQueue:

    def __init__(self, k: int):
        self.front = self.rear = -1
        self.val = [None]*k
        self.size = k
        
   
    def isEmpty(self) -> bool:
        if self.front == -1:
            return True
        return False
        

    def isFull(self) -> bool:
        if ((self.rear + 1) % self.size) == self.front:
            return True
        return False

    
    def enQueue(self, value: int) -> bool:
        if self.isFull():
            return False
        elif self.isEmpty():
            self.front = self.rear = 0
            self.val[0] = value
        else:
            self.rear = (self.rear + 1) % self.size
            self.val[self.rear] = value
        return True
        

    def deQueue(self) -> bool:
        if self.isEmpty():
            return False
        elif self.rear == self.front:
            temp = self.val[self.rear]
            self.front = self.rear = -1
        else:
            temp = self.val[self.rear]
            self.front = (self.front + 1) % self.size
        return True
            
        
    def Front(self) -> int:
        if self.isEmpty():
            return -1
        else:
            temp = self.val[self.front]
            return temp
            
        
    def Rear(self) -> int:
        if self.isEmpty():
            return -1
        else:
            temp = self.val[self.rear]
            return temp
    

    def display(self): 
        if(self.front == -1):  
            print ("Queue is Empty") 
  
        elif (self.rear >= self.front): 
            print("Elements in the circular queue are:", end = " ") 
            for i in range(self.front, self.rear + 1): 
                print(self.val[i], end = " ")
            print()
  
        else: 
            print ("Elements in Circular Queue are:", end = " ") 
            for i in range(self.front, self.size): 
                print(self.val[i], end = " ") 
            for i in range(0, self.rear + 1): 
                print(self.val[i], end = " ")
            print()
  
        if ((self.rear + 1) % self.size == self.front): 
            print("Queue is Full") 


# Your MyCircularQueue object will be instantiated and called as such:
k = 4
obj = MyCircularQueue(k)
value1, value2, value3, value4 = 1, 2, 3, 4

param_1 = obj.enQueue(value1)
param_12 = obj.enQueue(value2)
param_13 = obj.enQueue(value3)
param_14 = obj.enQueue(value4)
param_2 = obj.deQueue()
param_3 = obj.Front()
param_4 = obj.Rear()
param_5 = obj.isEmpty()
param_6 = obj.isFull()
obj.display() 