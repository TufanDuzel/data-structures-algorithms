# Can be created with both list and node.
class Node:
    def __init__(self, value):
        # Initialize a node with a value and set left and right children to None.
        self.value = value
        self.left = None
        self.right = None
        
class binary_search_tree:
    def __init__(self):
        # Initialize an empty binary search tree with no root.
        self.root = None
        
    def insert(self, value):
        # Create a new node with the given value.
        new_node = Node(value)
        
        if self.root is None:
            # If the tree is empty, set the new node as the root.
            self.root = new_node
            return True
        
        # Start from the root and traverse the tree.
        temp_node = self.root
        
        while True:
            # If the value already exists, do not insert a duplicate.
            if new_node.value == temp_node.value:
                return False
            
            # If the value is smaller, move to the left child.
            if new_node.value < temp_node.value:
                # If there's no left child, insert the new node here.
                if temp_node.left is None:
                    temp_node.left = new_node
                    return True
                temp_node = temp_node.left
            else:
                # If the value is greater, move to the right child.
                if temp_node.right is None:
                    temp_node.right = new_node
                    return True
                temp_node = temp_node.right
                
    def contains(self, value):
        # Start searching from the root node.
        temp_node = self.root
        
        while temp_node:
            # If the value is smaller, move to the left subtree.
            if value < temp_node.value:
                temp_node = temp_node.left
            # If the value is larger, move to the right subtree.
            elif value > temp_node.value:
                temp_node = temp_node.right
            # If the value matches, return True (value found).
            else:
                return True
        # If the loop ends, the value is not in the tree.
        return False


tree = binary_search_tree()

print(tree.insert(10))
print(tree.insert(10))
print(tree.insert(15))

print(tree.contains(10))
print(tree.contains(20))