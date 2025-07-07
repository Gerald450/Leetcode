class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numsSet = set(nums)
        maxLength = 0
        seen = set()
        length = 0

        for num in nums:
            
            if num in seen:
                continue
            else:
                seen.add(num)

            if (num -  1) not in numsSet:
                length = 1
        
                while (num + 1) in numsSet:
                    length += 1
                    num += 1
                    seen.add(num)
            
                
            maxLength = max(maxLength, length)
        
        return maxLength



        