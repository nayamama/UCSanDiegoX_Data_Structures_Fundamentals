# python3
"""
You will implement this data structure to store a string and efficiently cut a part (a
substring) of this string and insert it in a different position.
"""
import sys


class Rope:
    def __init__(self, s):
        self.s = s

    def result(self):
        return self.s

    def process(self, i, j, k):
        sub = self.s[i: j+1]
        self.s = self.s[:i] + self.s[j+1:]
        if k == 0:
            self.s = sub + self.s
        else:
            self.s = self.s[:k] + sub + self.s[k:]


rope = Rope(sys.stdin.readline().strip())
q = int(sys.stdin.readline())
for _ in range(q):
    i, j, k = map(int, sys.stdin.readline().strip().split())
    rope.process(i, j, k)
print(rope.result())
