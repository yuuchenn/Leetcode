def largestAltitude(self, gain: List[int]) -> int:
        highest = 0
        s = 0
        for g in gain:
            s = s+g
            if s > highest:
                highest = s
        return highest
# time complexity:O(N)
# space complexiyy:O(1)
