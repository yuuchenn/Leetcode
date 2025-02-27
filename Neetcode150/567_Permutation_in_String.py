    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        
        s1Dict = {}
        for i in range(len(s1)) :
            s1Dict[s1[i]] = s1Dict.get(s1[i],0) + 1
        for i in range(len(s1)) :
            if s1Dict.get(s2[i]) is not None:
                s1Dict[s2[i]] = s1Dict.get(s2[i],0) - 1      
        if all([val == 0 for val in s1Dict.values()]) :
            return True

        l = 0 
        for r in range(len(s1), len(s2)) :
            if s1Dict.get(s2[r]) is not None:
                s1Dict[s2[r]] = s1Dict.get(s2[r], 0) - 1
            if s1Dict.get(s2[l]) is not None:
                s1Dict[s2[l]] = s1Dict.get(s2[l], 0) + 1
            l += 1
            if all([val == 0 for val in s1Dict.values()]) :
                return True

        return False

# time: O(N)
# space: O(1)
