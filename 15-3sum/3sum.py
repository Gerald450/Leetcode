class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        otp = []


        for i,a in enumerate(nums):
            if a > 0:
                break

            if i > 0 and a == nums[i-1]:
                continue
            
            l,r = i + 1, len(nums) - 1

            while l < r:
                total = a + nums[l] + nums[r]

                if total > 0: 
                    r -= 1
                elif total < 0:
                    l += 1
                else:
                    otp.append([a, nums[l], nums[r]])
                    l += 1
                    r -= 1
                    while l < len(nums) and nums[l] == nums[l-1]:
                        l += 1

        return otp        
        