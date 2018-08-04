# python3
"""
The goal is to splay tree implementation to store a set of integers and quickly compute range sums.
input: the number of operations
       the content of operations and index (add(+), del(-), find(?), sum(+))
"""
from sys import stdin


# Vertex of a splay tree
class Vertex:
    def __init__(self, key, sum, left, right, parent):
        (self.key, self.sum, self.left, self.right, self.parent) = (key, sum, left, right, parent)

    def __str__(self):
        return str(self.key)


def update(v):
    """
    update some properties that are not changed in small rotation.
    1. sum
    2. the subtree or leaf that are not mentioned in small rotation
    """
    if v is None:
        return
    v.sum = v.key + (v.left.sum if v.left is not None else 0) + (v.right.sum if v.right is not None else 0)
    if v.left:
        v.left.parent = v
    if v.right:
        v.right.parent = v


def smallRotation(v):
    """
    rotate the node with its parent.(one height)
    """
    parent = v.parent
    if parent is None:
        return
    grandparent = v.parent.parent
    if parent.left == v:
        m = v.right
        v.right = parent
        parent.left = m
    else:
        m = v.left
        v.left = parent
        parent.right = m
    update(parent)
    update(v)
    v.parent = grandparent
    if grandparent:
        if grandparent.left == parent:
            grandparent.left = v
        else:
            grandparent.right = v


def bigRotation(v):
    """
    rotate the node with its grandparent. (two heights)
    """
    if v.parent.left == v and v.parent.parent.left == v.parent:
        # Zig-zig
        smallRotation(v.parent)
        smallRotation(v)
    elif v.parent.right == v and v.parent.parent.right == v.parent:
        # Zig-zig
        smallRotation(v.parent)
        smallRotation(v)
    else:
        # Zig-zag
        smallRotation(v)
        smallRotation(v)


# Makes splay of the given vertex and makes it the new root.
def splay(v):
    if v is None:
        return None
    while v.parent:
        if v.parent.parent is None:
            smallRotation(v)
            break
        bigRotation(v)
    return v


# Searches for the given key in the tree with the given root and calls splay for the deepest visited node after that.
# Returns pair of the result and the new root.
# If found, result is a pointer to the node with the given key. Otherwise, result is a pointer to the node with
# the smallest bigger key (next value in the order).
# If the key is bigger than all keys in the tree, then result is None.
def find(root, key):
    v = root
    last = root
    next = None
    while v:
        if v.key >= key and (next is None or v.key < next.key):
            next = v
        last = v
        if v.key == key:
            break
        if v.key < key:
            v = v.right
        else:
            v = v.left
    root = splay(last)
    return next, root


def split(root, key):
    result, root = find(root, key)
    if result is None:
        return root, None
    right = splay(result)
    left = right.left
    right.left = None
    if left:
        left.parent = None
    update(left)
    update(right)
    return left, right


def merge(left, right):
    if left is None:
        return right
    if right is None:
        return left
    while right.left:
        right = right.left
    right = splay(right)
    right.left = left
    update(right)
    return right


# Code that uses splay tree to solve the problem

root = None


def insert(x):
    global root
    left, right = split(root, x)
    new_vertex = None
    if right is None or right.key != x:
        new_vertex = Vertex(x, x, None, None, None)
    root = merge(merge(left, new_vertex), right)


def erase(x):
    global root
    if search(x) is None:
        return
    root = splay(root)
    root = merge(root.left, root.right)
    if root:
        root.parent = None


def search(x):
    global root
    res, root = find(root, x)
    if res is None or res.key != x:
        return None
    return res.key


def sum(fr, to):
    global root
    left, middle = split(root, fr)
    middle, right = split(middle, to + 1)
    if middle is None:
        ans = 0
        root = merge(left, right)
    else:
        ans = middle.sum
        root = merge(merge(left, middle), right)
    return ans


MODULO = 1000000001
n = int(stdin.readline())
last_sum_result = 0
for i in range(n):
    line = stdin.readline().split()
    if line[0] == '+':
        x = int(line[1])
        insert((x + last_sum_result) % MODULO)
    elif line[0] == '-':
        x = int(line[1])
        erase((x + last_sum_result) % MODULO)
    elif line[0] == '?':
        x = int(line[1])
        print('Found' if search((x + last_sum_result) % MODULO) else 'Not found')
    elif line[0] == 's':
        l = int(line[1])
        r = int(line[2])
        res = sum((l + last_sum_result) % MODULO, (r + last_sum_result) % MODULO)
        print(res)
        last_sum_result = res % MODULO
