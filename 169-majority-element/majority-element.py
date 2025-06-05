class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count, res = 0, 0

        for n in nums:
            res = n if count == 0 else res
            count += (1 if res == n else -1)

        return res