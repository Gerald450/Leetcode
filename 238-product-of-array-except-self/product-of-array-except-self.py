class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prev = [1] * len(nums)
        post = [1] * len(nums)
        otp = [1] * len(nums)
        temp = 1

      
        for i in range(1, len(nums)):
            prev[i] = nums[i-1] * temp
            temp = prev[i]
            

        temp = 1

        for i in range(len(nums) - 2, -1, -1):
            post[i] = nums[i+1] * temp
            temp = post[i]
        
        #commit

       


        for i in range(len(nums)):
            otp[i] = post[i] * prev[i]


  
        

        return otp
        