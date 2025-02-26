def encode(self, strs: List[str]) -> str:
        """Encodes a list of strings to a single string.
        """
        # decode the abbc into '4@abbc'
        res = ''
        for s in strs:
            res += str(len(s))+'@'+s
        return res

    def decode(self, s: str) -> List[str]:
        """Decodes a single string to a list of strings.
        """
        res = []
        l = 0
        while l < len(s):
            r = l
            while s[r] != '@': # r locate the position of '@'
                r += 1 
            length = int(s[l:r])
            res.append(s[r+1:r+1+length]) # next to @ 
            l = r+length+1 
        return res
# time : O(M) # M for the lenth of the list 
# space : O(1)
