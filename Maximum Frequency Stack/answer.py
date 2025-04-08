"""
This code is for Maximum freq Stack.
"""

from collections import deque, defaultdict

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

class FreqStack:
    """
    This class represents a frequency stack.
    """
    def __init__(self):
        """
        This method creates a FreqStack object.
        """
        self.freq_stack = defaultdict(Stack)
        self.freq = defaultdict(int)
        self.max_freq = 0

    def push(self, item: int) -> None:
        """
        This method pushes an integer value onto the stack.
        """
        if item in self.freq:
            self.freq[item] += 1
        else:
            self.freq[item] = 1
            
        freq = self.freq[item]
        
        self.freq_stack[freq].push(item)
        
        if freq > self.max_freq:
            self.max_freq = freq

    def pop(self) -> int:
        """
        This method removes and returns the most frequent element.
        """
        if self.max_freq == 0:
            return None

        stack = self.freq_stack[self.max_freq]
        
        item = stack.pop()
        
        self.freq[item] -= 1
        if self.freq[item] == 0:
            del self.freq[item]

        if stack.is_empty():
            self.max_freq -= 1
            
        return item
