class Solution:
    def pivotIndex(self, nums: List[int]) -> int:

        rightSum = 0
        leftSum = sum(nums)

        for i, num in enumerate(nums):
            leftSum -= num
            if rightSum == leftSum:
                return i
            rightSum += num

        return -1
            