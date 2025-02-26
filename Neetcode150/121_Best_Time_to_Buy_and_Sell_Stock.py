    def maxProfit(self, prices: List[int]) -> int: 
        minPrice = prices[0]
        maxProfit = 0
        
        for p in prices:
            maxProfit = max(maxProfit, p - minPrice)
            minPrice = min(p, minPrice)
        return maxProfit

# time : O(N)
# space : O(1)
