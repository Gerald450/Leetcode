class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        l = 0
        total = 0
        minSub = float('inf')

        for r in range(len(nums)):
            total += nums[r]

            while l <= r and total >= target:
                minSub = min(minSub, r - l + 1)
                total -= nums[l]
                l += 1
        
        return minSub if minSub != float('inf') else 0
            


        
            







        