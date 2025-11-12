class Solution:
    def jump(self, nums: List[int]) -> int:
        '''


        edge: empty, negative numbers

        plan:
        find the farthest jump, take that one and increment count
        [2, 3, 1, 1, 4, 5, 6, 2]

        need two pointer to show the window
        on each index find the window it just to
        in that window find the furthest jump and update your point to point,
        furthest jump window and increment count
        return count
        '''

        l, r = 0, 0
        count = 0

        while r < len(nums) - 1:
            furthest = 0
            for i in range(l, r + 1):
                furthest = max(furthest, i + nums[i])

            l = r + 1
            r = furthest
            count += 1

        return count

        '''
        [2,3,1,1,4]

        l = 2
        r = 4 -> 4
        count = 2
        window = 4 - 2 + 1 = 3
        furthest = 4
        i = 2 -> 2
        l + nums[1] = 1 + 3 == 4 > furthest
        start = 2

        
        


        '''