class TimeMap:

    def __init__(self):
        self.store = {} # {key: [[value, timestamp]]}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.store:
            self.store[key] = [[value, timestamp]]
        else:
            self.store[key].append([value, timestamp])

    def get(self, key: str, timestamp: int) -> str:
        if self.store.get(key) is None:
            return ""

        valList = self.store.get(key)
        res = ""
        l,r = 0 , len(valList) - 1
        
        while l <= r:
            m = (l + r) // 2

            if valList[m][1] == timestamp:
                return valList[m][0]
            if valList[m][1] < timestamp:
                res = valList[m][0]
                l = m + 1
            else:
                r = m - 1
        
        return res

# time : set(): O(1), get():O(log(m)) # m: num of values
# space : O(n * m) # n: num of keys, m: num of values
