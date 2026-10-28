RED = "R"
BLACK = "B"


class RBNode:
    __slots__ = ("key", "color", "left", "right", "parent")

    def __init__(self, key, color=RED, nil=None):
        self.key = key
        self.color = color
        self.left = nil
        self.right = nil
        self.parent = nil


class RBTree:
    name = "Rubro-Negra"

    def __init__(self):
        self.NIL = RBNode(None, BLACK)
        self.NIL.left = self.NIL.right = self.NIL.parent = self.NIL
        self.root = self.NIL
        self.rotations = 0

    def height(self):
        def h(n):
            return 0 if n is self.NIL else 1 + max(h(n.left), h(n.right))

        return h(self.root)

    def _rotate_left(self, x):
        y = x.right
        x.right = y.left
        if y.left is not self.NIL:
            y.left.parent = x
        y.parent = x.parent
        if x.parent is self.NIL:
            self.root = y
        elif x is x.parent.left:
            x.parent.left = y
        else:
            x.parent.right = y
        y.left = x
        x.parent = y
        self.rotations += 1

    def _rotate_right(self, y):
        x = y.left
        y.left = x.right
        if x.right is not self.NIL:
            x.right.parent = y
        x.parent = y.parent
        if y.parent is self.NIL:
            self.root = x
        elif y is y.parent.right:
            y.parent.right = x
        else:
            y.parent.left = x
        x.right = y
        y.parent = x
        self.rotations += 1

    def insert(self, key):
        parent = self.NIL
        cur = self.root
        while cur is not self.NIL:
            parent = cur
            if key == cur.key:
                return False
            cur = cur.left if key < cur.key else cur.right
        node = RBNode(key, RED, self.NIL)
        node.parent = parent
        if parent is self.NIL:
            self.root = node
        elif key < parent.key:
            parent.left = node
        else:
            parent.right = node
        self._insert_fixup(node)
        return True

    def _insert_fixup(self, z):
        while z.parent.color == RED:
            gp = z.parent.parent
            if z.parent is gp.left:
                uncle = gp.right
                if uncle.color == RED:
                    z.parent.color = BLACK
                    uncle.color = BLACK
                    gp.color = RED
                    z = gp
                else:
                    if z is z.parent.right:
                        z = z.parent
                        self._rotate_left(z)
                    z.parent.color = BLACK
                    z.parent.parent.color = RED
                    self._rotate_right(z.parent.parent)
            else:
                uncle = gp.left
                if uncle.color == RED:
                    z.parent.color = BLACK
                    uncle.color = BLACK
                    gp.color = RED
                    z = gp
                else:
                    if z is z.parent.left:
                        z = z.parent
                        self._rotate_right(z)
                    z.parent.color = BLACK
                    z.parent.parent.color = RED
                    self._rotate_left(z.parent.parent)
        self.root.color = BLACK

    def _find(self, key):
        cur = self.root
        while cur is not self.NIL:
            if key == cur.key:
                return cur
            cur = cur.left if key < cur.key else cur.right
        return self.NIL

    def _transplant(self, u, v):
        if u.parent is self.NIL:
            self.root = v
        elif u is u.parent.left:
            u.parent.left = v
        else:
            u.parent.right = v
        v.parent = u.parent

    def _minimum(self, n):
        while n.left is not self.NIL:
            n = n.left
        return n

    def remove(self, key):
        z = self._find(key)
        if z is self.NIL:
            return False
        y = z
        y_color = y.color
        if z.left is self.NIL:
            x = z.right
            self._transplant(z, z.right)
        elif z.right is self.NIL:
            x = z.left
            self._transplant(z, z.left)
        else:
            y = self._minimum(z.right)
            y_color = y.color
            x = y.right
            if y.parent is z:
                x.parent = y
            else:
                self._transplant(y, y.right)
                y.right = z.right
                y.right.parent = y
            self._transplant(z, y)
            y.left = z.left
            y.left.parent = y
            y.color = z.color
        if y_color == BLACK:
            self._delete_fixup(x)
        return True

    def _delete_fixup(self, x):
        while x is not self.root and x.color == BLACK:
            if x is x.parent.left:
                w = x.parent.right
                if w.color == RED:
                    w.color = BLACK
                    x.parent.color = RED
                    self._rotate_left(x.parent)
                    w = x.parent.right
                if w.left.color == BLACK and w.right.color == BLACK:
                    w.color = RED
                    x = x.parent
                else:
                    if w.right.color == BLACK:
                        w.left.color = BLACK
                        w.color = RED
                        self._rotate_right(w)
                        w = x.parent.right
                    w.color = x.parent.color
                    x.parent.color = BLACK
                    w.right.color = BLACK
                    self._rotate_left(x.parent)
                    x = self.root
            else:
                w = x.parent.left
                if w.color == RED:
                    w.color = BLACK
                    x.parent.color = RED
                    self._rotate_right(x.parent)
                    w = x.parent.left
                if w.right.color == BLACK and w.left.color == BLACK:
                    w.color = RED
                    x = x.parent
                else:
                    if w.left.color == BLACK:
                        w.right.color = BLACK
                        w.color = RED
                        self._rotate_left(w)
                        w = x.parent.left
                    w.color = x.parent.color
                    x.parent.color = BLACK
                    w.left.color = BLACK
                    self._rotate_right(x.parent)
                    x = self.root
        x.color = BLACK

    def search(self, key):
        return self._find(key) is not self.NIL

    def inorder(self):
        out = []

        def walk(n):
            if n is not self.NIL:
                walk(n.left)
                out.append(n.key)
                walk(n.right)

        walk(self.root)
        return out

    def tree_str(self, use_ansi=False):
        if self.root is self.NIL:
            return "(árvore vazia)"
        lines = []

        def fmt(n):
            label = f"{n.key}({n.color})"
            if use_ansi:
                code = "\033[91m" if n.color == RED else "\033[90;1m"
                return f"{code}{label}\033[0m"
            return label

        def walk(n, depth):
            if n is self.NIL:
                return
            walk(n.right, depth + 1)
            lines.append("    " * depth + fmt(n))
            walk(n.left, depth + 1)

        walk(self.root, 0)
        return "\n".join(lines)

    def is_valid(self):
        if self.root is not self.NIL and self.root.color != BLACK:
            raise AssertionError("Raiz deve ser preta")

        def check(n, lo, hi):
            if n is self.NIL:
                return 1
            if (lo is not None and n.key <= lo) or (hi is not None and n.key >= hi):
                raise AssertionError(f"Violação BST em {n.key}")
            if n.color == RED and (n.left.color == RED or n.right.color == RED):
                raise AssertionError(f"Dois vermelhos seguidos em {n.key}")
            bl = check(n.left, lo, n.key)
            br = check(n.right, n.key, hi)
            if bl != br:
                raise AssertionError(f"Altura-negra diferente em {n.key}")
            return bl + (1 if n.color == BLACK else 0)

        check(self.root, None, None)
        return True