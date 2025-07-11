class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        res = []
        if not nums:
            return res
        
        r = 0

        while r < len(nums):
            start = nums[r]
            while r < len(nums) - 1 and nums[r] + 1 == nums[r+1]:
                r += 1
            if start != nums[r]:
                res.append(str(start) + '->' + str(nums[r]))
            else:
                res.append(str(start))
            r += 1

        return res
            

        