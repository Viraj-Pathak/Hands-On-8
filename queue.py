class Queue:
    def __init__(self, capacity):
        self.capacity = capacity
        self.queue = [None] * capacity
        self.front = 0
        self.rear = -1
        self.size = 0

    def enqueue(self, item):
        if self.size == self.capacity:
            print("Queue Overflow")
            return
        self.rear = (self.rear + 1) % self.capacity
        self.queue[self.rear] = item
        self.size += 1

    def dequeue(self):
        if self.size == 0:
            print("Queue Underflow")
            return None
        item = self.queue[self.front]
        self.front = (self.front + 1) % self.capacity
        self.size -= 1
        return item

    def peek(self):
        if self.size == 0:
            return None
        return self.queue[self.front]

# Example usage:
queue = Queue(5)
queue.enqueue(1)
queue.enqueue(2)
queue.enqueue(3)
print("Front of the queue:", queue.peek())
print("Dequeued item:", queue.dequeue())
print("Front of the queue after dequeuing:", queue.peek())
