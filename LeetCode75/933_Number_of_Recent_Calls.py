class RecentCounter:
# queue 
    def __init__(self):
        # save ping time data
        self.t_zone  = [-3000]
    
    def ping(self, t: int) -> int:
        # remove history ping time that have been out of specific the time range
        while self.t_zone and self.t_zone[0] < t-3000:
            self.t_zone.pop(0)
        
        self.t_zone.append(t)
        
        return len(self.t_zone)

# time complexity: O(N)
# space complexity: O(N)
