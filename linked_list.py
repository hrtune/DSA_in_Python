class Node:
    key = None
    data = None
    next = None

    def __init__(self, data):
        self.data = data

class LinkedList:

    head = None
    tail = None

    def add_from_tail(self, data):
        if (self.tail is None):
            self.tail = Node(data)
            self.head = self.tail
            return
        
        self.tail.next = Node(data)
        self.tail = self.tail.next

    def add_from_head(self, data):
        if (self.head is None):
            self.head = Node(data)
            self.tail = self.head
            return

        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    