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
