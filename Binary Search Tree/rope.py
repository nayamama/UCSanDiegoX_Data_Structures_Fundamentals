# python3
"""
You will implement this data structure to store a string and efficiently cut a part (a
substring) of this string and insert it in a different position.
"""


class Rope:
    def __init__(self):
        self.s = None

    def result(self):
        return self.s

    def process(self, i, j, k):
        sub = self.s[i: j+1]
        self.s = self.s[:i] + self.s[j+1:]
        if k == 0:
            self.s = sub + self.s
        else:
            self.s = self.s[:k] + sub + self.s[k:]

    def read_file(self, file):
        with open(file, "r") as f:
            lines = f.readlines()
            self.s = lines[0]
            n = int(lines[1])
            assert n == len(lines[2:])
            queries = []
            for i in range(n):
                queries.append(list(map(int, lines[i+2].strip().split())))
        return queries


if __name__ == "__main__":
    file_path = "rope_example.txt"
    r = Rope()
    queries = r.read_file(file_path)
    for q in queries:
        r.process(q[0], q[1], q[2])

    print(r.s)
