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

    def min_of_node(self, current_node):
        while current_node.left:
            current_node = current_node.left
        return current_node
    
    def max_of_node(self, current_node):
        while current_node.right:
            current_node = current_node.right
        return current_node

    # Breadth First Search. (BFS)
    def bfs(self):
        current_node = self.root
        my_queue = []
        values = []
        my_queue.append(current_node)
        
        while len(my_queue) > 0:
            current_node = my_queue.pop(0)
            values.append(current_node.value)
            
            if current_node.left is not None:
                my_queue.append(current_node.left)
            if current_node.right is not None:
                my_queue.append(current_node.right)
        
        return values
    
    # Depth First Search. (DFS)
    # Pre-Order
    def dfs_pre_order(self):
        values = []
        
        def traverse(current_node):
            values.append(current_node.value)
            
            if current_node.left is not None:
                traverse(current_node.left)
            if current_node.right is not None:
                traverse(current_node.right)
        
        traverse(self.root)
        return values
    
    # Post-Order
    def dfs_post_order(self):
        values = []
        
        def traverse(current_node):
            if current_node.left is not None:
                traverse(current_node.left)
            if current_node.right is not None:
                traverse(current_node.right)
                
            values.append(current_node.value)
            
        traverse(self.root)
        return values
    
    # In-Order
    def dfs_in_order(self):
        values = []
        
        def traverse(current_node):
            if current_node.left is not None:
                traverse(current_node.left)
                
            values.append(current_node.value)
            
            if current_node.right is not None:
                traverse(current_node.right)
        
        traverse(self.root)
        return values


my_tree = binary_search_tree()
my_tree.insert(38)
my_tree.insert(19)
my_tree.insert(69)
my_tree.insert(12)
my_tree.insert(24)
my_tree.insert(59)
my_tree.insert(95)

print(my_tree.bfs())
print(my_tree.dfs_pre_order())
print(my_tree.dfs_post_order())
print(my_tree.dfs_in_order())