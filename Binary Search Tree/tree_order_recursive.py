class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

    def __str__(self):
        return str(self.key)


with open("tree_order_sample", "r") as f:
    l = f.readlines()
    n = int(l[0])
    Empty = None
    if n == 0:
        Empty = True
    tree = []
    if not Empty:
        for i in range(n):
            key, left, right = map(int, l[i + 1].split())
            node = Node(key)
            node.left, node.right = left, right
            tree.append(node)

        for node in tree:
            if node.left == -1:
                node.left = None
            else:
                node.left = tree[node.left]
            if node.right == -1:
                node.right = None
            else:
                node.right = tree[node.right]


def in_order(root):
    if not Empty:
        res = []
        if root:
            res = in_order(root.left)
            res.append(root.key)
            res += in_order(root.right)
        return res


def pre_order(root):
    if not Empty:
        res = []
        if root:
            res.append(root.key)
            res += pre_order(root.left)
            res += pre_order(root.right)
        return res


def post_order(root):
    if not Empty:
        res = []
        if root:
            res = post_order(root.left)
            res += post_order(root.right)
            #print(root.key, end=" ")
            res.append(root.key)
        return res


def is_bst(root):
    if Empty:
        return "Correct"
    else:
        order = in_order(root)
        if all(order[i] <= order[i+1] for i in range(len(order)-1)):
            return "Correct"
        else:
            return "Incorrect"


if __name__ == "__main__":
    if not Empty:
        root = tree[0]

        print(in_order(root))
        print(pre_order(root))
        print(post_order(root))
        print(is_bst(root))
    else:
        print("Correct")
