        c_grid = copy.deepcopy(grid)
        for r in range(len(grid)):
            for c in range(len(grid)):
                c_grid[c][r] = copy.deepcopy(grid[r][c])
        count = 0
        for r in range(len(grid)):
            for c in range(len(grid)):
                if grid[r] == c_grid[c]:
                    count += 1
        return count
        # time complexity:O(N^2) 
        # space complexity:O(N^2) 
        #
