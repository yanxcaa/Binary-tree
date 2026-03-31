class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        
        
    def __str__(self):
        return f"Node({self.value})"
    
class BinarySearchTree:
    def __init__(self):
        self.root = None
        
    def insert(self, value):
        if self.root == None:
            self.root = Node(value)
        else:
            self._insert_recursive(self.root, value)
    
    def _insert_recursive(self, current, value):
        if value < current.value:
            if current.left is None:
                current.left = value
            else:
                self._insert_recursive(current.left, value)
        elif value > current.value:
            if current.right is None:
                current.right = value
            else:
                self._insert_recursive(current.right, value)
        else:
            print(f"Value already exists ({value})")
            
    def display(self, node=None, level=0):
        if node is None and level == 0:
            node = self.root
        
        if node is not None:
            self.display(node.right, level + 1) 
            print(' ' * 4 * level + '->', node.value)
            self.display(node.left, level + 1)
        
if __name__ == "__main__":
    tree = BinarySearchTree()
    elements = [50, 30, 70, 20, 40, 60, 80]
    for x in elements:
        tree.insert(x)
        
    print("Binary Search Tree Structure:")
    tree.display()