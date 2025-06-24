class Solution:
    def trap(self, height: List[int]) -> int:

        l, r = 0, len(height) - 1
        maxr, maxl = height[r], height[l]
        res = 0

        while l < r:
            if maxl < maxr:
                l += 1
                maxl = max(maxl, height[l])
                res += maxl - height[l]
            else:
                r -= 1
                maxr = max(maxr, height[r])
                res += maxr - height[r]

        return res


            
        