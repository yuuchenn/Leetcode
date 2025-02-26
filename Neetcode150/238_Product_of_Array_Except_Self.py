def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        res = [1] * n
        
        curr = 1
        for i in range(n):
            res[i] = curr
            curr *= nums[i]

        curr = 1
        for i in range(n-1, -1, -1):
            res[i] *= curr
            curr *= nums[i]
          
        return res
# time: O(N)
# space : O(N)
