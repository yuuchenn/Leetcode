    def decodeString(self, s: str) -> str:
        ans = []
        for c in s:
            if c != ']':
                ans.append(c)
            else :
                decode = ''
                while ans[-1] != '[':
                    decode = ans.pop(-1) + decode 
                ans.pop(-1)
                k = ''
                while ans and ans[-1].isdigit():
                    k = ans.pop(-1) + k
                ans.append(decode * int(k))
        return ''.join(ans)

   # time complexity: O(maxK^countk+n)
   # space complexity: O(N)
