
    def isAnagram(self, s: str, t: str) -> bool:
        dict_s = {}
        if len(s) != len(t):
            return False

        for sc in s:
            dict_s[sc] = dict_s.get(sc,0)+1
        for st in t:
            if dict_s.get(st,0) == 0 :
                return False
            dict_s[st] -= 1
        return True
# time complexity:O(N+M)
# space complexity:O(1)


    def isAnagram(self, s: str, t: str) -> bool:
        dict_s = {}
        dict_t = {}
        if len(s) != len(t):
            return False
        # 
        for sc in s:
            dict_s[sc] = dict_s.get(sc,0) + 1
        for tc in t:
            dict_t[tc] = dict_t.get(tc,0) + 1

        for k,v in dict_s.items() :
            if v != dict_t.get(k,-1):
                return False
        return True

# time complexity:O(N+M)
# space complexity:O(1)
