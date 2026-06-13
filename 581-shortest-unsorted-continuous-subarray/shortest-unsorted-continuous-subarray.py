class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        '''
        [2, 5, 6, 3, 4, 5, 6, 3]
        input: nums
        output: int 

        edge: size 1, empty, dups

        plan:
        initialise right at 0 and left at size of nums
        loop from front and capture max seen
        if find a num lower than max seen update variable right to that idx
        loop from back while capturing min seen
        if find a num greater than min seen update variable left to that idx
        return right - left + 1 if variables changed
        '''

        

        n = len(nums)

        if n == 1 or n == 0:
            return 0

        right = 0
        left = n - 1

        max_seen = nums[0]
        for i in range(n):
            max_seen = max(nums[i], max_seen)
            if nums[i] < max_seen:
                right = i
            
        
        min_seen = nums[-1]
        for i in range(n - 1, -1, -1):
            min_seen = min(min_seen, nums[i])
            if nums[i] > min_seen:
                left = i
        
        
        
        print(right, left)
        otp = right - left + 1
        return otp if otp > 0 else 0

        '''
        [0,1,2,3, 4,5, 6]
        [2,6,4,8,10,9,15]
       

        '''



        