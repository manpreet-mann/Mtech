
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class SinglyLinkedList:
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
            return

        temp = self.head
        while temp.next:
            temp = temp.next

        temp.next = new_node

    # (iii) Deletion by value
    def delete(self, key):
        if self.head is None:
            print("List is empty")
            return

        if self.head.data == key:
            self.head = self.head.next
            return

        temp = self.head
        while temp.next and temp.next.data != key:
            temp = temp.next

        if temp.next:
            temp.next = temp.next.next
        else:
            print("Value not found")

    # (iv) Traversal
    def traverse(self):
        temp = self.head
        while temp:
            print(temp.data, end=" -> ")
            temp = temp.next
        print("None")


# Main program
ll = SinglyLinkedList()
ll.create([10, 20, 30])
ll.traverse()

ll.insert(40)
ll.traverse()

ll.delete(20)
ll.traverse()
