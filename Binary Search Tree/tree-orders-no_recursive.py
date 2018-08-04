"""
Input format (start from i = 0 )
the key of node
the index of left child
the index of right child
"""

import sys, threading

sys.setrecursionlimit(10 ** 6)  # max depth of recursion
threading.stack_size(2 ** 27)  # new thread will get stack of such size


class TreeOrders:

    def read(self, file):
        with open(file, "r") as f:
            l = f.readlines()
            self.n = int(l[0])
            self.key = [0] * self.n
            self.left = [0] * self.n
            self.right = [0] * self.n
            for i in range(self.n):
                self.key[i], self.left[i], self.right[i] = map(int, l[i+1].split())

    def inOrder(self):
        """
        Inorder (left, root, right)
        """
        result = []
        stack = []
        root = 0

        while True:
            if root != -1:
                stack.append(root)
                root = self.left[root]
            elif stack:
                root = stack.pop()
                result.append(self.key[root])
                root = self.right[root]
            else:
                break
        return result

    def preOrder(self):
        """
        Preorder (root, left, right)
        """
        result = []
        stack = []
        root = 0

        while True:
            if root != -1:
                result.append(self.key[root])
                stack.append(root)
                root = self.left[root]
            elif stack:
                root = stack.pop()
                root = self.right[root]
            else:
                break

        return result

    def postOrder(self):
        """
        PostOrder: (left, right, root)
        The order of result is from root to leaves
        """
        stack = [0]
        result = []

        while stack:
            id = stack.pop()
            result.append(self.key[id])

            left, right = self.left[id], self.right[id]
            if left != -1:
                stack.append(left)
            if right != -1:
                stack.append(right)
        return result[::-1]


def main():
    tree = TreeOrders()
    tree.read("tree_order_sample")
    print(" ".join(str(x) for x in tree.inOrder()))
    print(" ".join(str(x) for x in tree.preOrder()))
    print(" ".join(str(x) for x in tree.postOrder()))

    print(" ".join(str(x) for x in tree.inOrder()) + " "
          + " ".join(str(x) for x in tree.preOrder()) + " "
          + " ".join(str(x) for x in tree.postOrder()))


threading.Thread(target=main).start()
