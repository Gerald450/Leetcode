class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        '''
        dp[0] = 0
        dp[1] = 1
        dp[2] = min(1 + dp[1], coin = 2 -> 1) = 1
        dp[3] = min(1 + dp[2], coin = 3 -> None) = 2
        dp[4] = min(1 + dp[4 - 3])
        if 

        '''
        dp = [amount + 1] * (amount + 1)
        dp[0] = 0

        for i in range(1, amount + 1):
            for c in coins:
                if i - c >= 0:
                    dp[i] = min(1 + dp[i - c], dp[i])

        return dp[amount] if dp[amount] != (amount + 1) else -1

        


            
       
                