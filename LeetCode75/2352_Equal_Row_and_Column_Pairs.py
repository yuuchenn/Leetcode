# 2025/02/12 - hash map
def equalPairs(self, grid: List[List[int]]) -> int:
        h_map = {}

        for e in grid:
            h_map[tuple(e)] = h_map.get(tuple(e), 0) + 1

        grid_t = [[] for e in grid[0]]
        for e in grid:
            for i in range(len(e)):
                # if len(grid_t) < i:
                #     grid_t[i].append(e[i])
                # else :
                    # grid_t.append([e[i]])
                grid_t[i].append(e[i])
        res = {}
        for e in grid_t:
            if h_map.get(tuple(e)) is not None:
                res[tuple(e)] = res.get(tuple(e), 0) + h_map.get(tuple(e))

        return sum(res.values())
# time complexity:O(N*M) 
# space complexity:O(N*M) 

# 
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
