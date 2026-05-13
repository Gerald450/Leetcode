class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        '''
        input: nums
        output: array of indices

        edge case: 

        plan:
            loop through arr
                calculate the compliment of the element
                if compliment in dic, return the value of that key alongside the curr index
            insert curr index in dic

        '''

        hashmap = {}

        for idx, num in enumerate(nums):
            compliment = target - num
            if compliment in hashmap:
                return [hashmap[compliment], idx]
            hashmap[num] = idx
        