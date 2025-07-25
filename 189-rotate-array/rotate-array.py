class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        k %= len(nums)

        def reverse(start, end):
            while start < end:
                nums[start], nums[end] = nums[end], nums[start]
                start += 1
                end -= 1
        #for the commit
        #reverse entire arr
        reverse(0, len(nums) - 1)
        #reverse first k elements
        reverse(0, k - 1)
        #reverse rest
        reverse(k, len(nums) - 1)



        
