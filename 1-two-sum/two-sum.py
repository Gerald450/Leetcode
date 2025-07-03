class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}

        for idx, num in enumerate(nums):
            comp = target - num
            if comp in hashmap:
                return [hashmap[comp], idx]
            hashmap[num] = idx
        