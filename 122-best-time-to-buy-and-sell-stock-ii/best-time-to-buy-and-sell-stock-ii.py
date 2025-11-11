class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        '''
        input: prices
        output: max profit

        edge cases: monotonic decrease, negative, one, zero

        plan:

        compare to previous if less add to profit
        '''
        profit = 0

        for i in range(1, len(prices)):
            if prices[i] > prices[i - 1]:
                profit += prices[i] - prices[i - 1]

        return profit

            

