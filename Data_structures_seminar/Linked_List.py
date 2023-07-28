class Node:
    def __init__(self,data=None):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def print(self):
        node = self.head
        while node is not None:
            print(node.data)
            node = node.next

    def add(self,new):
        new_node = Node(new)
        new_node.next = self.head
        self.head = new_node

l1 = LinkedList()
e1 = Node('Python')
l1.head = e1
# # l1.print()
e2 = Node('programming')
l1.head.next = e2
# l1.print()
# # # Add an element at Beginning :
l1.add("Course:")
l1.print()




















