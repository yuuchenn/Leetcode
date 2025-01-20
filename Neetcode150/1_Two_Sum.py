    def twoSum(self, nums: List[int], target: int) -> List[int]:
        remains = dict()
        for i in range(len(nums)):
            print(remains.get(nums[i]))
            if remains.get(nums[i]) != None: # nums[i] in remains
                return [remains[nums[i]],i]
            else :
                remains[target - nums[i]] = i

  # time complexity: O(N)
  # space complexity: O(N)
