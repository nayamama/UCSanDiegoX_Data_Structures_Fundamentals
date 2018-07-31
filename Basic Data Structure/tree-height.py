# python3

import sys, threading

sys.setrecursionlimit(10 ** 7)  # max depth of recursion
threading.stack_size(2 ** 27)  # new thread will get stack of such size


class TreeHeight:
    def read(self):
        self.n = int(sys.stdin.readline())
        self.parent = list(map(int, sys.stdin.readline().split()))

    class Node:
        def __init__(self, key=None):
            self.key = key
            self.children = []

        def add_child(self, obj):
            self.children.append(obj)

        def __str__(self):
            kids = [str(kid.key) for kid in self.children]
            return str(self.key) + ":" + ",".join(kids)

    def get_tree_height(self, root):
        if len(root.children) == 0:
            return 1

        return 1 + max([self.get_tree_height(child) for child in root.children])

    def build_tree(self):
        self.tree = [self.Node(i) for i in range(self.n)]
        for i in range(self.n):
            if self.parent[i] == -1:
                self.root = self.tree[i]
            else:
                self.tree[self.parent[i]].add_child(self.tree[i])

    def compute_height(self):
        self.build_tree()
        return self.get_tree_height(self.root)


def main():
    tree = TreeHeight()
    tree.read()
    print(tree.compute_height())


threading.Thread(target=main).start()

