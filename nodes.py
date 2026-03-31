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
            
    def search(self, value):
        return self._search_recursive(self.root, value)
    
    def _search_recursive(self, current, value):
        if current is None:
            return False
        
        if current.value == value:
            return True
        elif value < current.value:
            return self._search_recursive(current.left, value)
        else:
            return self._search_recursive(current.right, value)
        
        
    def delete(self, value):
        return self._delete_recursive(self.root, value)
  
    def _delete_recursive(self, current, value):
        if current in None:
            return False
        
        if value < current.value:
            current.left = self._delete_recursive(current.left, value)
        elif value > current.value:
            current.right = self._delete_recursive(current.right, value)
        else:
            if current.left is None:
                return current.right
            elif current.right is None:
                return current.left
            
            current.value = self._min_value_node(current.right).value
            current.right = self._delete_recursive(current.right, current.value)
            
        return current
    
    def _min_value_node(self, node):
        current = node
        while current.left is not None:
            current = current.left
        return current
        
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