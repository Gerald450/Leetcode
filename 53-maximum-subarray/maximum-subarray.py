class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxT = nums[0]
        currSum = 0
        maxArr = (0,0)
        l, r = 0,0

        for i, n in enumerate(nums):
            r  = i
            if currSum < 0:
                currSum = 0
                l = i

            currSum += n
            if currSum > maxT:
                maxArr = (l,r)
            maxT = max(maxT, currSum)
            

        l, r = maxArr
        print(nums[l:r + 1])
        return maxT
