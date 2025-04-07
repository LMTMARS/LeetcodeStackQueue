"""
This code is for Implementing Queue using Stacks.
"""
from collections import deque

class Stack:
    """
    This class describes Stack objects.
    """
    def __init__(self):
        """
        This method creates a stack object.
        """
        self.items = deque()

    def push(self, item):
        """
        This method pushes a new value
        in stack.
        """
        self.items.append(item)

    def pop(self):
        """
        This method pops a value
        from a stack.
        """
        if self.is_empty():
            raise IndexError("Stack is empty.")
        return self.items.pop()

    def peek(self):
        """
        This method peeks a value
        from a stack.
        """
        if self.is_empty():
            raise IndexError("Stack is empty.")
        return self.items[-1]

    def is_empty(self):
        """
        This method checkes if stack is empty.
        """
        return len(self.items) == 0

    def __len__(self):
        """
        This method returns the length
        of the stack.
        """
        return len(self.items)

    def __str__(self):
        """
        This method returns a string representation
        of the stack.
        """
        return f"Bottom -> {list(self.items)} <- Top"
    
class MyQueue:
    """
    This class represents
    Queue objects made with Stack class.
    """
    def __init__(self):
        """
        This method creates a queue object.
        """
        self._first = Stack()
        self._second = Stack()

    def push(self, x):
        """
        This method pushes a value (x)
        in the queue.
        """
        while not self._first.is_empty():
            self._second.push(self._first.pop())
        self._first.push(x)
        while not self._second.is_empty():
            self._first.push(self._second.pop())

    def pop(self):
        """
        This method pops a value
        from the queue.
        """
        return self._first.pop()

    def peek(self):
        """
        This method peeks a value
        from a queue.
        """
        return self._first.peek()

    def empty(self):
        """
        This method checks whether
        the queue is empty.
        """
        return self._first.is_empty()