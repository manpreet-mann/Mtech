
class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None


class DoublyLinkedList:
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
        new_node.prev = temp

    # (iii) Deletion by value
    def delete(self, key):
        temp = self.head

        while temp and temp.data != key:
            temp = temp.next

        if temp is None:
            print("Value not found")
            return

        if temp.prev:
            temp.prev.next = temp.next
        else:
            self.head = temp.next

        if temp.next:
            temp.next.prev = temp.prev

    # (iv) Traversal (forward)
    def traverse(self):
        temp = self.head
        while temp:
            print(temp.data, end=" <-> ")
            temp = temp.next
        print("None")


# Main program
dll = DoublyLinkedList()
dll.create([10, 20, 30])
dll.traverse()

dll.insert(40)
dll.traverse()

dll.delete(20)
dll.traverse()
