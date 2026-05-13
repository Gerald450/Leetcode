class Solution:
    def jump(self, nums: List[int]) -> int:
        '''
        input: array of nums
        output: min num of jumps
        edge cases: empty, negative nums

        plan:
        form jump windows
        farthest each window can jump
        [2, 3, 3, 5, 4, 1]
        [ , [ , ],[ , , ]]
        use two pointers to maintain the window
        '''

        
        jumps = 0
        l, r = 0, 0

        while r < len(nums) - 1:
            farthest = 0
            for i in range(l, r + 1):
                farthest = max(farthest, i + nums[i])
            
            l = r + 1
            r = farthest
            jumps += 1

        return jumps