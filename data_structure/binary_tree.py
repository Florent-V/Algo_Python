class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self):
        self.root = None
    
    def is_empty(self):
        return self.root is None
    
    def size(self):
        return self._size(self.root)

    def _size(self, node):
        if node is None:
            return 0
        return 1 + self._size(node.left) + self._size(node.right)

    def insert(self, value):
        if not self.root:
            self.root = Node(value)
            return
        self._insert(self.root, value)

    def _insert(self, node, value):
        if node.value == value:
            return None
        direction = 'left' if value < node.value else 'right'
        if not getattr(node, direction):
            setattr(node, direction, Node(value))
            return
        self._insert(getattr(node, direction), value)

    def find_min(self):
        return self._find_min(self.root)

    def _find_min(self, node):
        if node is None:
            return None
        if node.left is None:
            return node.value
        return self._find_min(node.left)

    def find_max(self):
        return self._find_max(self.root)

    def _find_max(self, node):
        if node is None:
            return None
        if node.right is None:
            return node.value
        return self._find_max(node.right)

    def is_present(self, value):
        return self._is_present(self.root, value)

    def _is_present(self, node, value):
        if node is None:
            return False
        if node.value == value:
            return True
        direction = 'left' if value < node.value else 'right'
        if getattr(node, direction):
            return self._is_present(getattr(node, direction), value)   
        return False

    def find_min_height(self):
        return self._find_min_height(self.root)

    def _find_min_height(self, node):
        if node is None:
            return -1
        return 1 + min(
            self._find_min_height(node.left),
            self._find_min_height(node.right)
            )

    def find_max_height(self):
        return self._find_max_height(self.root)

    def _find_max_height(self, node):
        if node is None:
            return -1
        return 1 + max(
            self._find_max_height(node.left),
            self._find_max_height(node.right)
            )

    def is_balanced(self):
        return self.find_min_height() == self.find_max_height()

    # DFS - Depth First Search in Binary Tree
    def inorder(self):
        return self._inorder(self.root)

    def _inorder(self, node):
        if node is None:
            return []
        return (self._inorder(node.left) +
                [node.value] +
                self._inorder(node.right))

    def preorder(self):
        return self._preorder(self.root)

    def _preorder(self, node):
        if node is None:
            return []
        return ([node.value] +
                self._preorder(node.left) +
                self._preorder(node.right))

    def postorder(self):
        return self._postorder(self.root)

    def _postorder(self, node):
        if node is None:
            return []
        return (self._postorder(node.left) +
                self._postorder(node.right) +
                [node.value])

    # BFS - Breadth First Search in Binary Tree
    def level_order(self):
        if not self.root:
            return []
        result = []
        queue = [self.root]
        while queue:
            node = queue.pop(0)
            result.append(node.value)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        return result

    # def reverse_level_order(self):
    #     if not self.root:
    #         return []
    #     result = []
    #     queue = [self.root]
    #     while queue:
    #         node = queue.pop(0)
    #         result.append(node.value)
    #         if node.right:
    #             queue.append(node.right)
    #         if node.left:
    #             queue.append(node.left)
    #     return result

    def reverse_level_order(self):
        if not self.root:
            return []
        result = []
        queue = [self.root]
        while queue:
            node = queue.pop(0)
            result = [node.value] + result
            if node.right:
                queue.append(node.right)
            if node.left:
                queue.append(node.left)
        return result

    def invert(self):
        self.root = self._invert(self.root)

    def _invert(self, node):
        if node is None:
            return None
        node.left, node.right = self._invert(node.right), self._invert(node.left)
        return node

    def remove(self, value):
        self.root = self._remove(self.root, value)

    def _remove(self, node, value):
        if node is None:
            return None
        if value < node.value:
            node.left = self._remove(node.left, value)
        elif value > node.value:
            node.right = self._remove(node.right, value)
        else:
            if node.left is None:
                return node.right
            elif node.right is None:
                return node.left
            min_node = self._find_min_node(node.right)
            node.value = min_node.value
            node.right = self._remove(node.right, min_node.value)
        return node

    def _find_min_node(self, node):
        current = node
        while current.left is not None:
            current = current.left
        return current
    

if __name__ == "__main__":
    #elements = [30, 20, 40, 15, 25, 35, 45, 10, 18, 22, 28, 32, 38, 42, 48, 5, 12, 16, 24, 26, 31, 34, 39, 41, 46, 49, 3, 8, 14, 21]
    elements = [10, 5, 20, 2, 7, 15, 30]
    tree = BinaryTree()
    print("isEmpty", tree.is_empty())

    for element in elements:
        tree.insert(element)

    print("isEmpty", tree.is_empty())
    print("size", tree.size())

    print("find_max", tree.find_max())
    print("find_min", tree.find_min())

    print(tree.root.value, tree.root.left.value, tree.root.right.value)
    print(tree.root.left.left.value, tree.root.left.right.value, tree.root.right.left.value, tree.root.right.right.value)


    print("is_present 74", tree.is_present(74))
    print("is_present 92", tree.is_present(92))

    print("find_min_height", tree.find_min_height())
    print("find_max_height", tree.find_max_height())

    print("is_balanced", tree.is_balanced())

    print("inorder", tree.inorder())
    print("preorder", tree.preorder())
    print("postorder", tree.postorder())
    print("level_order", tree.level_order())
    print("reverse_level_order", tree.reverse_level_order())
