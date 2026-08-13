class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        '''
        input: amount, coins[int]
        output: int

        edge: amount is unreachable, empty list, amout == 0 or negative, dups

        plan:
        use dp memoization
        start from amount == 0 and work my way up
        calculate by looping through coins, subtract from curr amount and use value stored in dp
        '''

        dp = [0 for _ in range(amount + 1)]
        dp[0] = 1
        
        for coin in coins:
            for curr in range(amount + 1):
                if curr - coin >= 0:
                    dp[curr] += dp[curr - coin]
        
        return dp[amount]

        '''

        dp = [0, 1, 0, 0, 0, 0]
                 ^
        n = len(coins)
        m = ammout
        runtime: O(nm)
        space: O(m)

        '''

        