class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        '''
        input: nums[int]
        output: int

        edge: negative nums, 0, empty, 1

        plan:
        keep track of max res up until the current index
        keep track of min and max
        '''
        if len(nums) == 1:
            return nums[0]

        
        currMin = nums[0]
        currMax = nums[0]
        res = nums[0]

        for i in range(1, len(nums)):
            
            temp = currMax
            n = nums[i]
            currMax = max(n, currMin * n, currMax * n)
            currMin = min(n, currMin * n, temp * n)

            res = max(res, currMax)


        return res

        '''
        [2,3,-2,4,-2]
        ^
        currMax = -2  {4, -8, -48}
        currMin = -12
        res = 6

        '''

