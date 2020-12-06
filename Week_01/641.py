class MyCircularDeque:

    def __init__(self, k: int):
        """
        Initialize your data structure here. Set the size of the deque to be k.
        """
        self.max_length,self.queue = k,[]

    def insertFront(self, value: int) -> bool:
        """
        Adds an item at the front of Deque. Return true if the operation is successful.
        """
        if self.isFull() is True:
            return False
        self.queue.reverse()
        self.queue.append(value)
        self.queue.reverse()
        return True

    def insertLast(self, value: int) -> bool:
        """
        Adds an item at the rear of Deque. Return true if the operation is successful.
        """
        if self.isFull() is True:
            return False
        self.queue.append(value)
        return True

    def deleteFront(self) -> bool:
        """
        Deletes an item from the front of Deque. Return true if the operation is successful.
        """
        if self.isEmpty() is True:
            return False
        self.queue.pop(0)
        return True

    def deleteLast(self) -> bool:
        """
        Deletes an item from the rear of Deque. Return true if the operation is successful.
        """
        if self.isEmpty() is True:
            return False
        self.queue.pop()
        return True
        

    def getFront(self) -> int:
        """
        Get the front item from the deque.
        """
        if self.isEmpty() is True:
            return -1
        return self.queue[0]

    def getRear(self) -> int:
        """
        Get the last item from the deque.
        """
        if self.isEmpty() is True:
            return -1
        return self.queue[-1]
        

    def isEmpty(self) -> bool:
        """
        Checks whether the circular deque is empty or not.
        """
        return False if len(self.queue) > 0 else True
        

    def isFull(self) -> bool:
        """
        Checks whether the circular deque is full or not.
        """
        if len(self.queue) < self.max_length:
            return False
        else:
            return True
        
if __name__ == '__main__':
    obj = MyCircularDeque(3)
    param_1 = obj.insertLast(1)
    param_2 = obj.insertLast(2)
    param_3 = obj.insertFront(3)
    param_4 = obj.insertFront(4)
    print(param_4)
    exit()

# Your MyCircularDeque object will be instantiated and called as such:
# obj = MyCircularDeque(k)
# param_1 = obj.insertFront(value)
# param_2 = obj.insertLast(value)
# param_3 = obj.deleteFront()
# param_4 = obj.deleteLast()
# param_5 = obj.getFront()
# param_6 = obj.getRear()
# param_7 = obj.isEmpty()
# param_8 = obj.isFull()