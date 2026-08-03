class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        '''
        input: nums[int], target
        output: int, num of ways that evaluate to target

        edge: negative nums, nums is empty


        plan:
        recursion
        parameters: i, sum
        base: if i == len(nums) and sum == target: return 1
        if it's the sum != target: return 0

        ways = 0
        try negative
        try positive


        return ways 
        
        '''
        cache = {}

        def find_ways(i, total):
            if i == len(nums) and total == target:
                return 1

            if i == len(nums) or total - sum(nums[i:]) > target or total + sum(nums[i:]) < target:
                return 0

            if (i, total) in cache:
                return cache[(i, total)]

            
            ways = 0

            #negative
            num = nums[i]
            ways += find_ways(i+1, total - num)

            #positive
            ways += find_ways(i+1, total + num)

            cache[(i, total)] = ways
            return ways

        
        res = find_ways(0, 0)

        return res


        '''
        find(-1, 0) {
            ways = 0
            ways += find(0, -1){
                ways = 0
                ways += find(1, -2){
                    ways = 0
                    ways += find(2, -3){
                        ways = 0
                        ways += 0
                        
                        {
                            
                            
                        }
                    }
                }
            }

        }

        runtime: O(nS)
        space:O(nS) + O(n) recursion stack
        '''