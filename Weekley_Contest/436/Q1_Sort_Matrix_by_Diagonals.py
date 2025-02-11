def sortMatrix(self, grid: List[List[int]]) -> List[List[int]]:
        len_r = len(grid)
        len_c = len(grid[0])
        # Bottem right - non increasing
        for i in range(len_r):
            r, c = i, 0
            temp = []
            while r < len_r and c < len_c:
                temp.append(grid[r][c])
                r += 1
                c += 1
            r, c = i, 0
            temp.sort()
            while r < len_r and c < len_c:
                grid[r][c] = temp.pop()
                r += 1
                c += 1
        # top right - non decreasing
        for i in range(1,len_c):
            r, c = 0, i
            temp = []
            while r < len_r and c < len_c:
                temp.append(grid[r][c])
                r += 1
                c += 1
            r, c = 0, i
            temp.sort(reverse = True)
            while r < len_r and c < len_c:
                grid[r][c] = temp.pop()
                r += 1
                c += 1
        return grid

# time : O(N^2 * logN) # N = min(r,c)
# space : O(N) # N = min(r,c)
