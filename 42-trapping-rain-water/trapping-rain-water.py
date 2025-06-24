class Solution:
    def trap(self, height: List[int]) -> int:
        maxR, maxL = [], []

        maxr, maxl = 0, 0
        water = 0

        for i in range(len(height)):
            maxL.append(maxl)
            maxl = max(maxl, height[i])
        
        for i in range(len(height) - 1, -1, -1):
            maxR.append(maxr)
            maxr = max(maxr, height[i])

        maxR.reverse()
        
        for i in range(len(maxR)):
            diff = min(maxR[i], maxL[i]) - height[i]
            water += max(0, diff)

        return water


            
        