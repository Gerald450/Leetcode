class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        if sum(nums) % 2 == 1:
            return False

        target = sum(nums) / 2

        dp = set()
        dp.add(0)

        for i in range(len(nums)):
            nextDp = dp.copy()
            for t in dp:
                nextDp.add(t + nums[i])
                if target in nextDp:
                    return True
            dp = nextDp

        
        return False

            
        