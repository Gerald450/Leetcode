class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        '''
        input: nums[int]
        output: int

        edge: <3

        [1, 3, 5, 7, 4]
        [-2, -2, -3, -3, -3]
        []
        plan:
        generate diff array
        if its first three check to see if the diffs are all equal, save it in dp array
        for the next iterations, check last diff if it is equal to curr add 1


        '''
        if len(nums) < 3:
            return 0

        total = 0
        dp = [0 for _ in range(len(nums) - 1)]
        diffs = [nums[i] - nums[i + 1] for i in range(len(nums) - 1)]

        prev = 0
        for i in range(1, len(diffs)):
            
            if diffs[i] == diffs[i - 1]:
                prev += 1
            else:
                prev = 0
            total += prev


        return total


        '''
        [1,2,3,4]
         ^     ^
        i = 3
        j = 0 -> 0
        nums[0:3]

        '''
        