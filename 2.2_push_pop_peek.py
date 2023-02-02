class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Stack:
    def __init__(self):
        self.head = None

    def push(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node
        print("%d pushed to stack" % (data))

    def pop(self):
        if self.head is None:
            print("Underflow")
        else:
            popped = self.head.data
            self.head = self.head.next
            print("%d popped from stack" % (popped))
            return popped

    def peek(self):
        if self.head is None:
            print("Stack is empty")
        else:
            print("Top element is: %d" % (self.head.data))

if __name__ == '__main__':
    stack = Stack()
    while True:
        print("\nStack operations")
        print("1. Push")
        print("2. Pop")
        print("3. Peek")
        print("4. Quit")
        choice = int(input("Enter your choice: "))
        if choice == 1:
            data = int(input("Enter data to be pushed: "))
            stack.push(data)
        elif choice == 2:
            stack.pop()
        elif choice == 3:
            stack.peek()
        elif choice == 4:
            break
        else:
            print("Wrong choice, please try again")
