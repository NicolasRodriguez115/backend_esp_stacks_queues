def line():
    print('~'*20)

class Node():
    def __init__(self, data):
        self.data = data
        self.next = None

class simpleOrdersQueue():
    def __init__(self):
        self.head = None
        self.tail = None

    def enqueue(self, data):
        new_order = Node(data)
        if self.head == None:
            self.head = new_order
            self.tail = new_order
        else:
            self.tail.next = new_order
            self.tail = new_order

    def dequeue(self):
        if self.head == None:
            return "No orders in the queue!"
        else:
            removed = self.head
            self.head = self.head.next
            return removed.data
        
    def traverse(self):
        current = self.head
        while current:
            print(current.data)
            current = current.next
        

class complexOrdersQueue():
    def __init__(self) -> None:
        self.head = None
        self.tail = None

    def length_of_order(self, arr):
        count = 0
        for item in arr:
            count += 1
        return count
    
    def enqueue(self, data):
        new_order = Node(data)
        if self.head == None:
            self.head = new_order
            self.tail = new_order
        else:
            if self.length_of_order(new_order.data) < self.length_of_order(self.head.data):
                self.tail.next = new_order
                self.tail = new_order
            elif self.length_of_order(new_order.data) > self.length_of_order(self.head.data):
                new_order.next = self.head
                self.head = new_order
            else:
                new_order.next = self.head.next
                self.head.next = new_order

    def dequeue(self):
        if self.head == None:
            return "No orders in the queue!"
        else:
            removed = self.head
            self.head = self.head.next
            return removed.data
        
    def traverse(self):
        current = self.head
        while current:
            print(current.data)
            current = current.next

simple_queue = simpleOrdersQueue()

simple_queue.enqueue("#1 medium")
simple_queue.enqueue("#3 large")
simple_queue.enqueue("#9 large")
simple_queue.enqueue("#5 small")

simple_queue.traverse()

line()

simple_queue.dequeue()
simple_queue.dequeue()

simple_queue.traverse()

line()

complex_queue = complexOrdersQueue()

complex_queue.enqueue(["Vanilla ice-cream"])
complex_queue.enqueue(["Big Mac", "Large Coke", "Large Fries", "4 piece Nuggets"])
complex_queue.enqueue(["Quarter Pounder", "Medium Fanta"])
complex_queue.enqueue(["Big Mac", "Large Dr.Pepper", "Large Fries", "4 piece Nuggets"])
complex_queue.enqueue(["Cheese burger"])

complex_queue.traverse()

line()

complex_queue.dequeue()
complex_queue.dequeue()
complex_queue.dequeue()

complex_queue.traverse()