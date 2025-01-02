    def uniqueOccurrences(self, arr: List[int]) -> bool:
        unique_list = [arr[0]]
        nums = [0]
        for i in range(len(arr)):
            if arr[i] not in unique_list:
                unique_list.extend([arr[i]])
                nums.extend([1])
            else : 
                for j in range(len(unique_list)):
                    if arr[i] == unique_list[j]:
                        nums[j] += 1
        return True if len(set(nums)) == len(nums) else False
      # time complexity:O(N^2)
      # space complexity:O(N)

# Better way
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        Occurences = {}
        for i in arr:
            Occurences[i] = Occurences.get(i,0)+1
        #return True if len(Occurences) == len(set(Occurences.values())) else False
        return len(Occurences) == len(set(Occurences.values()))
      # time complexity:O(N)
      # space complexity:O(N)
      # dictionary.get(key,default = None) it will return the value of the key in the dictionary, and if the key doesn't exist return none by default.
