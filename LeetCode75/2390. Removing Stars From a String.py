    def removeStars(self, s: str) -> str:
        ans = []
        for c in s:
            if c == '*' and len(ans) > 0:
                ans.pop(-1)
            elif c != '*':
                ans.extend(c)
        return ''.join(ans)
# time complexity: O(N)
# space complexity: O(N)
