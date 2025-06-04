class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if len(nums) <= 2:
            return len(nums)
        
        k = 2  # Start from index 2 since we allow 2 of the same element
        for i in range(2, len(nums)):
            if nums[i] != nums[k - 2]:  # Check if current number is not the same as the one 2 spots behind
                nums[k] = nums[i]
                k += 1
        
        return k
