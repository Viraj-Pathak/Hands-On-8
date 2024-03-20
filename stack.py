class Stack:
    def __init__(self, capacity):
        self.capacity = capacity
        self.stack = [None] * capacity
        self.top = -1

    def push(self, item):
        if self.top == self.capacity - 1:
            print("Stack Overflow")
            return
        self.top += 1
        self.stack[self.top] = item

    def pop(self):
        if self.top == -1:
            print("Stack Underflow")
            return None
        item = self.stack[self.top]
        self.top -= 1
        return item

    def peek(self):
        if self.top == -1:
            return None
        return self.stack[self.top]

# Example usage:
stack = Stack(5)
stack.push(1)
stack.push(2)
stack.push(3)
print("Top of the stack:", stack.peek())
print("Popped item:", stack.pop())
print("Top of the stack after popping:", stack.peek())
