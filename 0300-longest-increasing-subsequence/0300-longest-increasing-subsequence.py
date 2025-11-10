class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        '''
        output: LIS -> int

        edge: negative nums, repeated nums

        initialise dp -> [1] at each point
        use dp arr to store lis at each num in nums, start at the end
        run a loop at each point comparing nums
            if num is less than curr num, then get max(dp[curr], 1 + dp[i])
        return max(dp)

        '''
        dp = [1] * len(nums)

        for c in range(len(nums) - 1, -1, -1):

            for i in range(c + 1, len(nums)):
                if nums[i] > nums[c]:
                    dp[c] = max(dp[c], 1 + dp[i])
            
        return max(dp)
        
        '''
        [10,9,2,5,3,7,101,18]
                  ^
        
        dp = [2, 2, 4, 3, 3, 2, 1, 1]
        ix = [0, 1, 2, 3, 4, 5, 6, 7]

        c = 4 -> 3
            i = 6 -> 101
            101 > 3
            




        '''

        

                



        