class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self, capacity):
        self.capacity = capacity
        self.head = None
        self.size = 0

    def insert(self, data):
        if self.size == self.capacity:
            print("Linked List is full")
            return
        new_node = Node(data)
        if not self.head:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node
        self.size += 1

    def display(self):
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")

# Example usage:
linked_list = LinkedList(5)
linked_list.insert(1)
linked_list.insert(2)
linked_list.insert(3)
linked_list.display()
