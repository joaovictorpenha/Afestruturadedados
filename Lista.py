class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class ListaSimplesEncadeada:
    def __init__(self):
        self.head = None

    def is_empty(self):
        return self.head is None

    def append(self, data):
        new_node = Node(data)
        if self.is_empty():
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node

    def remove(self, data):
        if self.is_empty():
            return None
        if self.head.data.id == data.id:
            self.head = self.head.next
        else:
            current = self.head
            while current.next and current.next.data.id != data.id:
                current = current.next
            if current.next:
                current.next = current.next.next

    def display(self):
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")

    def to_list(self):
        result = []
        current = self.head
        while current:
            result.append(current.data)
            current = current.next
        return result

    def from_list(self, items):
        self.head = None
        for item in items:
            self.append(item)
