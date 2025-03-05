    def coloredCells(self, n: int) -> int:
        res = 1
        # can be divided to 4 side, every side can append (n-1) new blue cells
        for i in range(n):
            res += i * 4

        return res

# time: O(n)
# space: O(1)
