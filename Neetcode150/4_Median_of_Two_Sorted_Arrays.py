# Need to modify to binary search method






# merge and sort
def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        # init 
        tot = len(nums1) + len(nums2)
        median = tot//2 + 1
        ans = []
        n1 = n2 = 0
        # if len > 
        while n1 + n2 < median :
            if nums1 and nums2 and nums1[0] > nums2[0] :
                ans.append(nums2.pop(0))
                n2 += 1
            elif nums1 and nums2 and nums1[0] < nums2[0] :
                ans.append(nums1.pop(0))
                n1 += 1
            elif nums1 and not nums2 :
                ans.append(nums1.pop(0))
                n1 += 1
            else :
                ans.append(nums2.pop(0))
                n2 += 1
        if tot % 2 > 0 :
            return ans[tot//2]
        else : 
            return (ans[tot//2-1] + ans[tot//2])/2
