class Solution:
    def maxEnvelopes(self, envelopes: List[List[int]]) -> int:
        envelopes.sort(key=lambda x:(x[0], -x[1]))

        heights = [h for _, h in envelopes]

        dp = []

        for height in heights:
            idx = bisect_left(dp, height)

            if idx == len(dp):
                dp.append(height)
            else:
                dp[idx] = height

        return len(dp)

            

        
        
        
                

                
                

        