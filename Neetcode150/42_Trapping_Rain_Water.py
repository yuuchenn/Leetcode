    def trap(self, height: List[int]) -> int:
        n = len(height)
        maxLeft, maxRight = [0] * n, [0] * n
        res = 0
      
        maxHeight = 0
        for i in range(n):
            maxLeft[i] = maxHeight
            maxHeight = max(maxHeight, height[i])
        maxHeight = 0
        for i in range(n-1, -1, -1):
            maxRight[i] = maxHeight
            maxHeight = max(maxHeight, height[i])
        
        for i in range(n):
            res += max(0, min(maxLeft[i], maxRight[i]) - height[i])
        return res

# time : O(N)
# space : O(N)
