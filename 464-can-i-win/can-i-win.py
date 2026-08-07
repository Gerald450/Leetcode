class Solution:
    def canIWin(self, maxChoosableInteger: int, desiredTotal: int) -> bool:
        '''
        input: ints
        output: bool

        edge: 0s, choosable==desiredTotal

        plan:

        '''

        if maxChoosableInteger >= desiredTotal:
            return True

        total = maxChoosableInteger * (maxChoosableInteger + 1) // 2

        if total < desiredTotal:
            return False

        memo = {}
        def dfs(used, remaining):
            state = tuple(sorted(used))
            if state in memo:
                return memo[state]

            for num in range(1, maxChoosableInteger + 1):
                if num in used:
                    continue
                
                #can reach target
                if num >= remaining:
                    memo[state] = True
                    return True
                
                used.add(num)

                if not dfs(used, remaining - num):
                    used.remove(num)
                    memo[state] = True
                    return True
                
                #undo move
                used.remove(num)

            memo[state] = False
            return False

        return dfs(set(), desiredTotal)
