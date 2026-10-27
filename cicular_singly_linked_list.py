
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class CircularLinkedList:
    def __init__(self):
        self.head = None

    # (i) Creation
    def create(self, values):
        for value in values:
            self.insert(value)

    # (ii) Insertion at end
    def insert(self, data):
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            new_node.next = self.head
            return

        temp = self.head
        while temp.next != self.head:
            temp = temp.next

        temp.next = new_node
        new_node.next = self.head

    # (iii) Deletion by value
    def delete(self, key):
        if self.head is None:
            print("List is empty")
            return

        current = self.head
        previous = None

        # Find the node
        while True:
            if current.data == key:
                break
            previous = current
            current = current.next

            if current == self.head:
                print("Value not found")
                return

        # Only one node
        if current.next == self.head and current == self.head:
            self.head = None
            return

        # Deleting the first node
        if current == self.head:
            last = self.head
            while last.next != self.head:
                last = last.next

            self.head = self.head.next
            last.next = self.head

        # Deleting any other node
        else:
            previous.next = current.next

    # (iv) Traversal
    def traverse(self):
        if self.head is None:
            print("List is empty")
            return

        temp = self.head
        while True:
            print(temp.data, end=" -> ")
            temp = temp.next

            if temp == self.head:
                break

        print("(back to head)")


# Main program
cll = CircularLinkedList()
cll.create([10, 20, 30])
cll.traverse()

cll.insert(40)
cll.traverse()

cll.delete(20)
cll.traverse()
