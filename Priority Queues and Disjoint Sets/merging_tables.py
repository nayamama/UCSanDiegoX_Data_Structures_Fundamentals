# python3

import sys

class MergeTable:

    def read_data(self, file=None):
        """
        read data from input
        """
        self.jobs = []

        if file:
            with open(file, "r") as f:
                l = f.readlines()
                self.n, self.m = map(int, l[0].split())
                self.lines = list(map(int, l[1].split()))
                for i in range(2, len(l)):
                    job = tuple(map(int, l[i].split()))
                    self.jobs.append(job)

        else:
            self.n, self.m = map(int, sys.stdin.readline().split())
            self.lines = list(map(int, sys.stdin.readline().split()))
            for _ in range(self.m):
                self.jobs.append(map(int, sys.stdin.readline().split()))

        self.rank = [1] * self.n
        self.parent = list(range(0, self.n))

    def getParent(self, table_id):
        """
        update a set of id of parent (from table_id to root) and compresses path
        :param table_id:
        :return: root
        """
        path = []

        # find the root of table
        root = table_id
        while root != self.parent[root]:
            path.append(self.parent[root])
            root = self.parent[root]

        # compresses path
        for id in path:
            self.parent[id] = root

        return root

    def merge(self, destination, source):
        """
        Union two tables from source to destination
        :param destination, source:
        :return: if src == destination, return None, otherwise update object parameters
        """
        realDestination, realSource = self.getParent(destination), self.getParent(source)

        if realDestination == realSource:
            return

        if self.rank[realSource] <= self.rank[realDestination]:
            self.parent[realSource] = realDestination
        else:
            self.parent[realDestination] = realSource
            if self.rank[realDestination] == self.rank[realSource]:
                self.rank[realDestination] += 1

        self.lines[realDestination] += self.lines[realSource]
        self.lines[realSource] = 0
        # print(self.rank)

    def write_result(self):
        ans = []
        for des, src in self.jobs:
            self.merge(des - 1, src - 1)
            ans.append(max(self.lines))
        for x in ans:
            print(x, end=" ")
    

if __name__ == "__main__":
    solution = MergeTable()
    solution.read_data("merge_table_sample1.txt")
    solution.write_result()
