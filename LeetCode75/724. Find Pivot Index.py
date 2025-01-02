    def pivotIndex(self, nums: List[int]) -> int:
        s_left = 0
        s_right = sum(nums) 
        for i in range(len(nums)):
            s_right -= nums[i] 
            if s_left == s_right:
                return i
            s_left += nums[i]
        return -1

# time complexity:O(N)
# space complexiy:O(1)
