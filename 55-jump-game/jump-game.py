class Solution:
    def canJump(self, nums: List[int]) -> bool:
        l = len(nums) - 1
        flag = True  # Start with True, assume we can reach the end

        if len(nums) == 1:
            return True

        while l >= 0:
            if nums[l] == 0 and l != len(nums) - 1:
                r = l
                flag = False  # Assume stuck for now

                # Move left to find a jumper that can bypass zero
                l -= 1
                while l >= 0:
                    if nums[l] > r - l:
                        flag = True  # Found a jumper
                        break
                    l -= 1

                if not flag:
                    return False
            else:
                l -= 1

        return True
