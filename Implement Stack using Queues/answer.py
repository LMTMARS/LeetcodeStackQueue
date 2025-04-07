"""
This code is for implementing stack
using queues.
"""
from collections import deque

class Queue:
    """
    This class represents Queue objects.
    """
    def __init__(self):
        """
        This method creates a Queue object.
        """
        self.items = deque()

    def enqueue(self, item):
        """
        This method adds an element
        to a queue.
        """
        self.items.append(item)  # додаємо в кінець

    def dequeue(self):
        """
        This method removes an element
        from a queue.
        """
        if self.is_empty():
            raise IndexError("Queue is empty.")
        return self.items.popleft()

    def peek(self):
        """
        This method returns a first element of a queue.
        """
        if self.is_empty():
            raise IndexError("Queue is empty.")
        return self.items[0]

    def is_empty(self):
        """
        This method checks if a queue is empty.
        """
        return len(self.items) == 0

    def __len__(self):
        """
        This method returns len of a queue.
        """
        return len(self.items)

    def __str__(self):
        """
        This method returns a string representation
        of a queue.
        """
        return f"Front -> {list(self.items)} <- Rear"
    

class MyStack:
    """
    This class represents Stack object
    implemented using queues.
    """
    def __init__(self):
        """
        This method creates a stack object.
        """
        self._first = Queue()
        self._second = Queue()

    def push(self, x: int) -> None:
        """
        This method pushes an element to a stack.
        """
        self._second.enqueue(x)
        while not self._first.is_empty():
            self._second.enqueue(self._first.dequeue())
        self._first, self._second = self._second, self._first

    def pop(self) -> int:
        """
        This method pops an element from a stack.
        """
        if self._first.is_empty():
            raise IndexError("Stack is empty.")
        return self._first.dequeue()

    def top(self) -> int:
        """
        This method returns a top element
        from a stack.
        """
        if self._first.is_empty():
            raise IndexError("Stack is empty.")
        return self._first.peek()

    def empty(self) -> bool:
        """
        This method checks if a stack is empty.
        """
        return self._first.is_empty()