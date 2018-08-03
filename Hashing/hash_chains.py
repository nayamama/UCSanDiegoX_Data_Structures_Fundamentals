# python3


class Query:

    def __init__(self, query):
        self.type = query[0]
        if self.type == 'check':
            self.ind = int(query[1])
        else:
            self.s = query[1]


class QueryProcessor:
    _multiplier = 263
    _prime = 1000000007

    def __init__(self, bucket_count):
        self.bucket_count = bucket_count
        self.buckets = [[] for _ in range(bucket_count)]

    def _hash_func(self, s):
        """
        Hash function
        """
        ans = 0
        for c in reversed(s):
            ans = (ans * self._multiplier + ord(c)) % self._prime
        return ans % self.bucket_count

    def add(self, string):
        """
        Insert string into the table.
        If there is already such string in the hash table,
        then the query is ignored.
        """
        hashed = self._hash_func(string)
        bucket = self.buckets[hashed]
        if string not in bucket:
            self.buckets[hashed] += [string]

    def delete(self, string):
        """
        Removes string from the table.
        If there is no such string in the hash table,
        then the query is ignored.
        """
        hashed = self._hash_func(string)
        bucket = self.buckets[hashed]
        """
        for i in range(len(bucket)):
            if bucket[i] == string:
                bucket.pop(i)
                break
        """
        if string in bucket:
            bucket.pop(bucket.index(string))

    def find(self, string):
        """
        Looks up for the string in the table.
        Returns “yes” or “no” (without quotes) depending on whether
        the table contains string or not.
        """
        hashed = self._hash_func(string)
        if string in self.buckets[hashed]:
            return "yes"
        return "no"

    def check(self, i):
        """
        Returns the content of the i-th list in the table, if it is empty, return a blank line.
        """
        return reversed(self.buckets[i])

    def process_queries(self, queries):
        """
        Runs query processor and sends the results to standard output.
        """
        for query in queries:
            if query.type == "add":
                self.add(query.s)
            elif query.type == "del":
                self.delete(query.s)
            elif query.type == "find":
                print(self.find(query.s), end=" ")
            elif query.type == "check":
                print(" ".join(self.check(query.ind)), end=" ")


def read_file(file):
    queries = []
    bucket_count = 0

    if file:
        with open(file, "r") as f:
            l = f.readlines()
            bucket_count = int(l[0])
            queries_count = int(l[1])
            for i in range(2, len(l)):
                query = Query(l[i].split())
                queries.append(query)
        assert queries_count == len(queries)
    # print("the file is loaded.")
    return bucket_count, queries


if __name__ == "__main__":

    bucket_count, queries = read_file("hash_chains_sample")
    qp = QueryProcessor(bucket_count)
    qp.process_queries(queries)

