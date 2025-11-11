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
        dp = []

        def binary_search(num, arr):
            l, r = 0, len(arr) - 1

            while l <= r:
                m = (l + r) // 2
                if arr[m] < num:
                    l = m + 1
                elif arr[m] > num:
                    r = m - 1
                else:
                    return m

            return l

        for num in nums:
            length = len(dp)

            pos = binary_search(num, dp)

            if pos == length:
                dp.append(num)
            else:
                dp[pos] = num

        return len(dp)
        
        '''
        [10,9,2,5,3,7,101,18]
                  ^
        
        dp = [2, 2, 4, 3, 3, 2, 1, 1]
        ix = [0, 1, 2, 3, 4, 5, 6, 7]

        c = 4 -> 3
            i = 6 -> 101
            101 > 3
            

        '''

        

                



        