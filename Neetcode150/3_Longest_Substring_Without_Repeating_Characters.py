def lengthOfLongestSubstring(self, strings: str) -> int:
        l = 0
        strSet = set()
        maxLen = 0
        for r in strings:
            while s in strSet:
                strSet.remove(s[r])
                l += 1
            strSet.add(s[r])
            maxLen = max(maxLen, r-l+1)
        return maxLen

# time: O(N)
# space: O(N)
                




def lengthOfLongestSubstring(self, strings: str) -> int:
        # init
        ans = {}
        max_len = lens = 0
        idx = 0
        
        for s in strings :
            if ans and ans.get(s) != None :
                # find the repeat character then check if the length bigger than the last one
                if lens > max_len :
                    max_len = lens
                # remove the item before the exist repeat in the dictionary 
                ans = {k:v for k,v in ans.items() if v >= ans[s]}
                ans[s] = idx
                lens = len(ans)
                idx += 1
            else :
                lens += 1
                ans[s] = idx
                idx += 1
        if lens > max_len:
            max_len = lens
        return max_len

# time complexity : O(N)
# space complexity :O(N)


 def lengthOfLongestSubstring(self, strings: str) -> int:
        # init
        l , r = 0,0
        max_len = 0
        char_index = {}
        
        for s in strings:
            # check if existed: update max_len and move l pointer
            if char_index.get(s) != None and char_index[s] >= l:
                max_len = max(max_len, r - l)
                l = char_index[s] + 1

            char_index[s] = r
            r += 1
        
        max_len = max(max_len, r - l)
        return max_len

# time complexity : O(N)
# space complexity :O(N)
