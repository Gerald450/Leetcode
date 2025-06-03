class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:


      

        while val in set(nums):
            nums.remove(val)
        
        print(nums)
        return len(nums)
        