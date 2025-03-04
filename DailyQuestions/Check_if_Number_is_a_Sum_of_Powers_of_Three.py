  def checkPowersOfThree(self, n: int) -> bool:

        stack = [] # res, powers
        def backtrack(n):
            powers = 1
            while n >= powers:
                res = [n - powers, powers]
                powers *= 3
            stack.append(res)

            if stack[-1][0] > stack[-1][1] :
                return False
            if len(stack) > 1 and stack[-1][1] >= stack[-2][1]:
                return False
            if stack[-1][0] == 0 :
                return True
                
            if stack[-1][0] >= 1:
                return backtrack(stack[-1][0])

        return backtrack(n)

# time: O(log_3(N))
# space: O(log_3(N))
