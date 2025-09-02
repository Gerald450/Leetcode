class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        hashmap = collections.Counter(nums)

        for key, value in hashmap.items():
            if value > len(nums) / 2:
                return key