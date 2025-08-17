class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxT = nums[0]
        currSum = 0

        for n in nums:
            if currSum < 0:
                currSum = 0
            currSum += n
            maxT = max(maxT, currSum)

        return maxT
