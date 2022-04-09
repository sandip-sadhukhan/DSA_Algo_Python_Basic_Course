"""
Implement a Binary Tree
and preorder search on that tree
"""


class Node:
    def __init__(self, value: int) -> None:
        self.value: int = value
        self.left: "Node" | None = None
        self.right: "Node" | None = None


class BinaryTree:
    def __init__(self, root: int) -> None:
        self.root = Node(root)

    def search(self, find_val: int) -> bool:
        """Return True, if the value
        is in the tree, return
        False otherwise."""

        return self.preorder_search(self.root, find_val)

    def print_tree(self) -> str:
        """Print out all tree nodes
        as they are visited in
        a preorder traversal."""

        return self.preorder_print(self.root)

    def preorder_search(self, start: Node | None, find_val: int) -> bool:
        """Helper method - use this to create a
        recursive search solution."""
        # Base condition
        if start is None:
            return False
        if start.value == find_val:
            return True

        leftSearch: bool = self.preorder_search(start.left, find_val)
        rightSearch: bool = self.preorder_search(start.right, find_val)

        return leftSearch or rightSearch

    def preorder_print(self, start: Node | None) -> str:
        """Helper method - use this to create a
        recursive print solution."""
        # Base condition
        if start is None:
            return ""

        leftTraversal: str = self.preorder_print(start.left)
        rightTraversal: str = self.preorder_print(start.right)

        traversal: str = ""

        if leftTraversal != "" and rightTraversal != "":
            traversal = (
                str(start.value) + "-" + leftTraversal + "-" + rightTraversal
            )
        elif leftTraversal != "" and rightTraversal == "":
            traversal = str(start.value) + "-" + leftTraversal
        elif leftTraversal == "" and rightTraversal != "":
            traversal = str(start.value) + "-" + rightTraversal
        else:
            traversal = str(start.value)

        return traversal


# Set up tree
tree = BinaryTree(1)
tree.root.left = Node(2)
tree.root.right = Node(3)
tree.root.left.left = Node(4)
tree.root.left.right = Node(5)

# Test search
# Should be True
print(tree.search(4))
# Should be False
print(tree.search(6))

# Test print_tree
# Should be 1-2-4-5-3
print(tree.print_tree())
