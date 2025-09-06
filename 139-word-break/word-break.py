class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        dp = [False] * (len(s) + 1)
        dp[len(s)] = True

        for i in range(len(s) - 1, -1, -1):
            for w in wordDict:
                n = len(w)
                if i + n <= len(s) and s[i:i+n] == w:
                    dp[i] = dp[i + n]
                if dp[i]:
                    break


                #commit2

        return dp[0]
        
   
        