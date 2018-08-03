# python3


class RabinKarp:
    _multiplier = 263
    _prime = 1000000007

    def __init__(self):
        self.input = None
        self.pattern = None
        self.output = []

    def __polynomial_hash_func(self, s):
        """
        Hash function
        """
        ans = 0
        for c in reversed(s):
            ans = (ans * self._multiplier + ord(c)) % self._prime
        return ans

    def precompute_hashes(self):
        """
        Precompute hash value for each substring of input
        """
        t = len(self.input)
        p = len(self.pattern)

        hash_values = [None] * (t - p + 1)
        input_tail = self.input[-p:]
        hash_values[-1] = self.__polynomial_hash_func(input_tail)

        # computer hash for x^|P|
        y = 1
        for i in range(p):
            y = (y * self._multiplier) % self._prime
        # print("y = %d" % y)

        # fill in hash values
        for i in range(t - p)[::-1]:
            hash_values[i] = (self._multiplier * hash_values[i+1] + ord(self.input[i]) - y * ord(self.input[i + p])) % self._prime

        return hash_values

    def rabin_karp(self):
        """
        core algorithm:
        1. go through the input, find all substrings with the same length as pattern
        2. compare hash value of substring with pattern
        3. compare the exact equality
        """
        pattern_hash = self.__polynomial_hash_func(self.pattern)
        hash_values = self.precompute_hashes()

        t = len(self.input)
        p = len(self.pattern)

        for i in range(t - p + 1):
            if pattern_hash == hash_values[i]:
                if self.pattern == self.input[i: i + p]:
                    self.output.append(i)

    def write_result(self):
        self.rabin_karp()
        print(" ".join(map(str, self.output)))

"""        
def read_input():
    return (input().rstrip(), input().rstrip())

def print_occurrences(output):
    print(' '.join(map(str, output)))

def get_occurrences(pattern, text):
    return [
        i 
        for i in range(len(text) - len(pattern) + 1) 
        if text[i:i + len(pattern)] == pattern
    ]
"""


if __name__ == '__main__':
    pattern = input().rstrip()
    text = input().rstrip()

    rk = RabinKarp()
    rk.input = text
    rk.pattern = pattern
    rk.rabin_karp()
    print(rk.output)


