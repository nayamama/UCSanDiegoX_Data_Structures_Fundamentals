# python3
from math import floor

class HeapBuilder:
    def __init__(self):
        self._swaps = []
        self._data = []

    def ReadData(self):
        n = int(input())
        self._data = [int(s) for s in input().split()]
        assert n == len(self._data)

    def WriteResponse(self):
        print(len(self._swaps))
        for swap in self._swaps:
            print(swap[0], swap[1])

    def sift_down(self, i):
        size = len(self._data)
        min_idx = i

        # compare the value of parent with that of left child
        left_child = 2*i + 1
        if left_child < size and self._data[left_child] < self._data[min_idx]:
            min_idx = left_child

        # compare the value of parent with that of right child
        right_child = 2*i + 2
        if right_child < size and self._data[right_child] < self._data[min_idx]:
            min_idx = right_child

        # check if we need to swap
        if i != min_idx:
            self._data[i], self._data[min_idx] = self._data[min_idx], self._data[i]
            self._swaps.append((i, min_idx))
            self.sift_down(min_idx)

    def GenerateSwaps(self):
        # The following naive implementation just sorts
        # the given sequence using selection sort algorithm
        # and saves the resulting sequence of swaps.
        # This turns the given array into a heap,
        # but in the worst case gives a quadratic number of swaps.
        #
        # TODO: replace by a more efficient implementation
        """
        for i in range(len(self._data)):
            for j in range(i + 1, len(self._data)):
                if self._data[i] > self._data[j]:
                    self._swaps.append((i, j))
                    self._data[i], self._data[j] = self._data[j], self._data[i]
        """
        size = len(self._data)
        for i in range(floor((size-1)/2))[::-1]:
            self.sift_down(i)
			

    def Solve(self):
        self.ReadData()
        self.GenerateSwaps()
        self.WriteResponse()


if __name__ == '__main__':
    heap_builder = HeapBuilder()
    heap_builder.Solve()
