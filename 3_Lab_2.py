class AVLNode:
    def __init__(self, value):
        self.value = value
        self.left_child = None
        self.right_child = None
        self.node_height = 1

class AVLTreeStructure:
    def __init__(self):
        self.root_node = None

    def node_height(self, node):
        return 0 if not node else node.node_height

    def balance_factor(self, node):
        return 0 if not node else self.node_height(node.left_child) - self.node_height(node.right_child)

    def rotate_left(self, node):
        new_root = node.right_child
        temp_subtree = new_root.left_child
        
        new_root.left_child = node
        node.right_child = temp_subtree
        
        node.node_height = max(self.node_height(node.left_child), self.node_height(node.right_child)) + 1
        new_root.node_height = max(self.node_height(new_root.left_child), self.node_height(new_root.right_child)) + 1
        
        return new_root

    def rotate_right(self, node):
        new_root = node.left_child
        temp_subtree = new_root.right_child
        
        new_root.right_child = node
        node.left_child = temp_subtree
        
        node.node_height = max(self.node_height(node.left_child), self.node_height(node.right_child)) + 1
        new_root.node_height = max(self.node_height(new_root.left_child), self.node_height(new_root.right_child)) + 1
        
        return new_root

    def insert_node(self, current_node, value):
        if not current_node:
            return AVLNode(value)
        
        if value < current_node.value:
            current_node.left_child = self.insert_node(current_node.left_child, value)
        else:
            current_node.right_child = self.insert_node(current_node.right_child, value)
        
        current_node.node_height = max(self.node_height(current_node.left_child), self.node_height(current_node.right_child)) + 1
        balance = self.balance_factor(current_node)
        
        if balance > 1 and value < current_node.left_child.value:
            return self.rotate_right(current_node)
        
        if balance < -1 and value > current_node.right_child.value:
            return self.rotate_left(current_node)
        
        if balance > 1 and value > current_node.left_child.value:
            current_node.left_child = self.rotate_left(current_node.left_child)
            return self.rotate_right(current_node)
        
        if balance < -1 and value < current_node.right_child.value:
            current_node.right_child = self.rotate_right(current_node.right_child)
            return self.rotate_left(current_node)
        
        return current_node

    def add_value(self, value):
        self.root_node = self.insert_node(self.root_node, value)

    def pre_order_traversal(self, node):
        if node:
            print(f"{node.value} ", end="")
            self.pre_order_traversal(node.left_child)
            self.pre_order_traversal(node.right_child)
    
    def print_tree_structure(self, node, depth=0, prefix="Root:"):
        if node:
            print("    " * depth + prefix + str(node.value))
            if node.left_child:
                self.print_tree_structure(node.left_child, depth + 1, "L---")
            if node.right_child:
                self.print_tree_structure(node.right_child, depth + 1, "R---")


# Example: Constructing and demonstrating the AVL Tree
avl_tree = AVLTreeStructure()

# Insert values into the tree
avl_tree.add_value(50)
avl_tree.add_value(30)
avl_tree.add_value(70)
avl_tree.add_value(20)
avl_tree.add_value(40)
avl_tree.add_value(15)
avl_tree.add_value(80)

# Pre-order traversal
print("Pre-order traversal of AVL Tree:")
avl_tree.pre_order_traversal(avl_tree.root_node)
print("\n")

# Tree structure visualization in console
print("Tree structure view:")
avl_tree.print_tree_structure(avl_tree.root_node)

