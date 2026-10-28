class AVLNode:
    __slots__ = ("key", "left", "right", "height")

    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
        self.height = 1


class AVLTree:
    name = "AVL"

    def __init__(self):
        self.root = None
        self.rotations = 0

    @staticmethod
    def _h(node):
        return node.height if node else 0

    def _update(self, node):
        node.height = 1 + max(self._h(node.left), self._h(node.right))

    def _balance(self, node):
        return self._h(node.left) - self._h(node.right) if node else 0

    def height(self):
        return self._h(self.root)

    def _rotate_right(self, y):
        x = y.left
        y.left = x.right
        x.right = y
        self._update(y)
        self._update(x)
        self.rotations += 1
        return x

    def _rotate_left(self, x):
        y = x.right
        x.right = y.left
        y.left = x
        self._update(x)
        self._update(y)
        self.rotations += 1
        return y

    def _rebalance(self, node):
        self._update(node)
        bal = self._balance(node)
        if bal > 1:
            if self._balance(node.left) < 0:
                node.left = self._rotate_left(node.left)
            return self._rotate_right(node)
        if bal < -1:
            if self._balance(node.right) > 0:
                node.right = self._rotate_right(node.right)
            return self._rotate_left(node)
        return node

    def insert(self, key):
        if self.search(key):
            return False
        self.root = self._insert(self.root, key)
        return True

    def _insert(self, node, key):
        if node is None:
            return AVLNode(key)
        if key < node.key:
            node.left = self._insert(node.left, key)
        else:
            node.right = self._insert(node.right, key)
        return self._rebalance(node)

    def remove(self, key):
        if not self.search(key):
            return False
        self.root = self._remove(self.root, key)
        return True

    def _remove(self, node, key):
        if key < node.key:
            node.left = self._remove(node.left, key)
        elif key > node.key:
            node.right = self._remove(node.right, key)
        else:
            if node.left is None:
                return node.right
            if node.right is None:
                return node.left
            succ = node.right
            while succ.left:
                succ = succ.left
            node.key = succ.key
            node.right = self._remove(node.right, succ.key)
        return self._rebalance(node)

    def search(self, key):
        node = self.root
        while node:
            if key == node.key:
                return True
            node = node.left if key < node.key else node.right
        return False

    def inorder(self):
        out = []

        def walk(n):
            if n:
                walk(n.left)
                out.append(n.key)
                walk(n.right)

        walk(self.root)
        return out

    def tree_str(self):
        if not self.root:
            return "(árvore vazia)"
        lines = []

        def walk(n, depth):
            if n is None:
                return
            walk(n.right, depth + 1)
            lines.append("    " * depth + str(n.key))
            walk(n.left, depth + 1)

        walk(self.root, 0)
        return "\n".join(lines)

    def is_valid(self):
        def check(n, lo, hi):
            if n is None:
                return 0
            if (lo is not None and n.key <= lo) or (hi is not None and n.key >= hi):
                raise AssertionError(f"Violação BST em {n.key}")
            hl = check(n.left, lo, n.key)
            hr = check(n.right, n.key, hi)
            if abs(hl - hr) > 1:
                raise AssertionError(f"Nó {n.key} desbalanceado")
            if n.height != 1 + max(hl, hr):
                raise AssertionError(f"Altura errada em {n.key}")
            return 1 + max(hl, hr)

        check(self.root, None, None)
        return True