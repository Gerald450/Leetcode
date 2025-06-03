class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        k = 0  # Index to place the next non-val element
        for i in range(len(nums)):
            print(i, k, nums)
            if nums[i] != val:
                nums[k] = nums[i]
                k += 1
        return k
