def longestPalindrome(self, s: str) -> str:
        # init
        ans = ""
        max_lens = 0
        # two pointer : center approach
        for i in range(len(s)):
            # odd length string 
            l, r = i, i
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if (r - l + 1) > max_lens:
                    ans = s[l:r+1]
                    max_lens = r - l + 1
                l -= 1
                r += 1
            # even length string
            l, r = i, i + 1
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if (r - l + 1) > max_lens:
                    ans = s[l:r+1]
                    max_lens = r - l + 1
                l -= 1
                r += 1
        return ans

# time :O(N^2)
# space :O(1)
