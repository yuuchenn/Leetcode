    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        answer = [0] * 2
        set1 = set(nums1)
        set2 = set(nums2)

        answer[0] = list(set1 - set2)
        answer[1] = list(set2 - set1)
        return answer


# hashset
# time complexity:O(N+M)
# list(set1 - set2) is O(N) * O(1): 
#   1. Because we have to check each element in nums1, O(N)
#   2. And checked if the element exists in nums2, Set will calculate the hash value and check if the keys are the same, O(1)
# space complexity:O(N+M)
