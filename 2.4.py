# Here is one way to implement a Circular Queue using a linked list in Python:
print("Sabuj Routh")


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class CircularQueue:
    def __init__(self):
        self.rear = None

    def is_empty(self):
        return self.rear == None

    def enqueue(self, data):
        temp = Node(data)
        if self.rear == None:
            self.rear = temp
            self.rear.next = self.rear
        else:
            temp.next = self.rear.next
            self.rear.next = temp
            self.rear = temp

    def dequeue(self):
        if self.rear == None:
            return None
        if self.rear.next == self.rear:
            temp = self.rear
            self.rear = None
            return temp.data
        else:
            temp = self.rear.next
            self.rear.next = temp.next
            return temp.data

    def display(self):
        if self.rear == None:
            return None
        else:
            temp = self.rear.next
            while temp != self.rear:
                print(temp.data, end=' ')
                temp = temp.next
            print(temp.data)


cq = CircularQueue()

while True:
    print("1. Enqueue")
    print("2. Dequeue")
    print("3. Display")
    print("4. Quit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        data = int(input("Enter the element to be enqueued: "))
        cq.enqueue(data)
    elif choice == 2:
        data = cq.dequeue()
        if data != None:
            print("Dequeued element: ", data)
        else:
            print("Queue is empty")
    elif choice == 3:
        cq.display()
    elif choice == 4:
        break