class Node:
    def __init__(self,value):
        self.left = None
        self.right = None
        self.v = value
class Tree:
    def __init__(self):
        self.root = None

    def get_root(self):
        return self.root

    def add(self,value):
        if self.root is None:
            self.root = Node(value)
        else:
            self._add(value,self.root)

    def _add(self,value,node):
        if val < node.v:
            if node.left is not None:
                self._add(value,node.left)
            else:
                node.left = Node(value)
        else:
            if node.right is not None:
                self._add(value,node.right)
            else:
                node.right = Node(value)

    def find(self,value):
        if self.root is not None:
            return self._find(value,self.root)

    def _find(self,value,node):
        if val == node.v:
            print('Found the value')
        elif val < node.v and node.left is not None:
            self._find(value,node.left)
        elif val > node.v and node.right is not None:
            self._find(value,node.right)
        else:
            print('Value is not found')

    def delete_tree(self):
        self.root = None
        print('Tree deleted')

    def print_tree(self):
        if self.root is not None:
            print('Tree values are shown below')
            self._print_tree(self.root)
            print('------------')

    def _print_tree(self,node):
        if node is not None:
            self._print_tree(node.left)
            print(str(node.v))
            self._print_tree(node.right)

tree = Tree()
while True:
    print('1.Add Elements, 2.Search for Element, 3.Print Tree, 4.Delete Tree and Exit')
    choice = int(input('Enter the choice: '))
    if choice == 1:
        val = int(input('Enter the value: '))
        tree.add(val)
    elif choice == 2:
        val = int(input('Enter the value to be searched: '))
        tree.find(val)
    elif choice == 3:
        tree.print_tree()
    elif choice == 4:
        tree.delete_tree()
        break
    else:
        print("invalid choice")
