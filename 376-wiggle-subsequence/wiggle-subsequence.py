class Solution:
    def wiggleMaxLength(self, nums: List[int]) -> int:
        '''
        input:  array of nums
        output: int: length of longest wiggle subsequence

        edge: dups, zeros, length is 1 or empty

        plan:
        create a dp array of differences
        dont add zeros
        if length of dp is 0 return 0 else intiliase count to 2
        loop through incrementing count if it's wiggle

        '''
        if len(nums) == 1:
            return 1

        dp = [nums[i - 1] - nums[i] for i in range(1, len(nums)) if (nums[i - 1] - nums[i]) != 0]
        if not len(dp):
            return 1
        
        count = 2

        for i in range(1, len(dp)):
            #wiggle
            if (dp[i - 1] > 0 and dp[i] < 0) or (dp[i - 1] < 0 and dp[i] > 0):
                count += 1



        return count


        '''
        [-16, 12, -5, -3, -2, 5, 5, -11, 8]
                                         i
        
        count = 7

        time: O(n)
        space: O(n)
        '''
        