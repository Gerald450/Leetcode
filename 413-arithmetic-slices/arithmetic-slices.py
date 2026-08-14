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
       
        for the next iterations, check last diff if it is equal to curr add 1

        '''

        total = 0

        prev = 0
        for i in range(2, len(nums)):
            if nums[i] - nums[i - 1] == nums[i - 1] - nums[i - 2]:
                prev += 1
            else:
                prev = 0
            total += prev


        return total


        '''
        runtime: O(n)
        space: O(1)

        '''
        