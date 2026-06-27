class Solution:
    def rob(self, nums: List[int]) -> int:
        '''
        input: nums
        output: max money stolen: int

        edge: only 1 or 2 houses, empty

        plan:
        get the max of robbing a house and the house 2 steps behind it, and just robbing the house behind it
        update selection on that curr house, for future decision making
        for this case do the algorithm for house 1 to n -1, and house 0 to n - 2, n is length
        and get the max of the two
        '''

        if len(nums) == 1:
            return nums[0]

        rob1, rob2 = 0, 0
        
        #start from 0, n - 2
        for n in nums[:len(nums) - 1]:
            temp = rob2
            rob2 = max(rob2, n + rob1)
            rob1 = temp
        
        otp1 = rob2
        rob1, rob2 = 0, 0

        #start from 1, n - 1
        for n in nums[1:]:
            temp = rob2
            rob2 = max(rob2, n + rob1)
            rob1 = temp

        otp2 = rob2

        return max(otp1, otp2)


        '''
        runtime: O(n)
        space: O(n) because of slices being created
        '''
        