        ans = []
        for a in asteroids:
            if len(ans) == 0 or ans[-1] < 0:
                ans.append(a)
            elif ans[-1] > 0 and a > 0 :
                ans.append(a)
            else :
                while len(ans) > 0 and ans[-1] > 0 and ans[-1] + a < 0 :
                    ans.pop(-1)
                if len(ans) == 0 or ans[-1] < 0 :
                    ans.append(a)
                elif ans[-1] > 0 and ans[-1] + a == 0:
                    ans.pop(-1)
                    
        return ans
# time complexity:O(N)
# space complexity:O(N)
