class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = {}

        def dfs(total):
            if total > amount:
                return float('inf')
            if total == amount:
                return 0
            if total in dp:
                return dp[total]

            minCount = float('inf')
            for c in coins:
                res = dfs(total + c)
                if res != float('inf'):
                    minCount = min(minCount, 1 + res)
            
            dp[total] = minCount
            
            return minCount
        
        result = dfs(0)

        return result if result != float('inf') else -1

            
       
                