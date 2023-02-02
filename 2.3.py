# Implement a Queue using linked list using python class
print("Sabuj Routh")

# Here is an implementation of a queue using a linked list in Python:


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Queue:
    def __init__(self):
        self.front = None
        self.rear = None

    def is_empty(self):
        return self.front is None

    def enqueue(self, data):
        new_node = Node(data)
        if self.rear is None:
            self.front = self.rear = new_node
            return
        self.rear.next = new_node
        self.rear = new_node

    def dequeue(self):
        if self.is_empty():
            return None
        temp = self.front
        self.front = temp.next
        if self.front is None:
            self.rear = None
        return temp.data

    def peek(self):
        if self.is_empty():
            return None
        return self.front.data

# Here is a menu-driven example to show how to use the Queue class:
if __name__ == '__main__':
    queue = Queue()
    while True:
        print("Queue operations")
        print("1. Enqueue")
        print("2. Dequeue")
        print("3. Peek")
        print("4. Quit")
        choice = int(input("Enter your choice: "))
        if choice == 1:
            data = int(input("Enter the data: "))
            queue.enqueue(data)
        elif choice == 2:
            data = queue.dequeue()
            if data is not None:
                print("Dequeued data:", data)
            else:
                print("Queue is empty")
        elif choice == 3:
            data = queue.peek()
            if data is not None:
                print("Peek data:", data)
            else:
                print("Queue is empty")
        elif choice == 4:
            break
        else:
            print("Invalid choice")
