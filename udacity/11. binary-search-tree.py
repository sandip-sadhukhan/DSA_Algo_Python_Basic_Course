"""
Implimentation of BST
And Search(), insert()
"""


class Node:
    def __init__(self, value: int) -> None:
        self.value: int = value
        self.left: "Node" | None = None
        self.right: "Node" | None = None


class BST:
    def __init__(self, root) -> None:
        self.root = Node(root)

    def insert(self, new_val: int) -> None:
        self.bst_insert(self.root, new_val)

    def bst_insert(self, current: Node, new_val: int) -> None:
        if current.value == new_val:
            print("Value already present.")
            return

        elif current.value > new_val:
            # if left child is empty then add there
            if current.left is None:
                current.left = Node(new_val)
            else:
                # move to left side
                self.bst_insert(current.left, new_val)

        elif current.value < new_val:
            # if right child is empty then add there
            if current.right is None:
                current.right = Node(new_val)
            else:
                # move to right side
                self.bst_insert(current.right, new_val)

    def search(self, find_val) -> bool:
        return self.bst_search(self.root, find_val)

    def bst_search(self, current: Node | None, find_val: int) -> bool:
        # Base condition
        if current is None:
            return False
        if current.value == find_val:
            return True

        if current.value > find_val:
            return self.bst_search(current.left, find_val)
        else:
            return self.bst_search(current.right, find_val)

    def print_tree_inorder(self, current: Node | None) -> None:
        if current is None:
            return
        else:
            self.print_tree_inorder(current.left)
            print(current.value)
            self.print_tree_inorder(current.right)


# Set up tree
tree = BST(4)

# Insert elements
tree.insert(2)
tree.insert(1)
tree.insert(3)
tree.insert(5)

# print inorder
tree.print_tree_inorder(tree.root)

# Check search
# Should be True
print(tree.search(4))
# Should be False
print(tree.search(6))
