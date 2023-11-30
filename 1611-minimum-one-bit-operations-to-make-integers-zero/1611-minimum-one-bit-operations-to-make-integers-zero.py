class Solution:
    def minimumOneBitOperations(self, n: int) -> int:
        if n==0:
            return 0
        for i in range(int(log2(log2(n + 2))), -1, -1):
            n ^= n >> (1 << i)

        return n