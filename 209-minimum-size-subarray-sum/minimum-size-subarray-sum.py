from typing import List

class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        size = float('inf')  # Start with "infinity" to track minimum
        l = 0
        total = 0

        for r in range(len(nums)):
            total += nums[r]
            
            # Try to shrink the window
            while total >= target:
                size = min(size, r - l + 1)
                total -= nums[l]
                l += 1

        return 0 if size == float('inf') else size
