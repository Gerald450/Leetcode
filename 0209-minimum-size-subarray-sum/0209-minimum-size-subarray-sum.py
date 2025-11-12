class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        l = 0
        length = float('inf')
        currSum = 0

        for r in range(len(nums)):
            currSum += nums[r]
            while currSum >= target:
                length = min(length, r - l + 1)
                currSum -= nums[l]
                l += 1
                

        return length if length != float('inf') else 0
            


        
            







        