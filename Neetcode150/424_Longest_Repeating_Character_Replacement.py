    def characterReplacement(self, s: str, k: int) -> int:
        l = 0 
        charDict = {}
        maxLen = 0
        for r in range(len(s)):
            charDict[s[r]] = charDict.get(s[r], 0) + 1

            if charDict and (r-l+1) - max(charDict.values()) > k:
              
                charDict[s[l]] -= 1
                l += 1
            
            maxLen = max(maxLen, r-l+1)
          
        return maxLen

# time: O(N)
# space: O(1)
