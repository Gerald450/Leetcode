class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        dp = [False] * (len(s) + 1)
        dp[-1] = True



        for i in range(len(s), -1, -1):

            for word in wordDict:
                window = i + len(word)

                if window <= len(s) and s[i:window] == word:
                    dp[i] = dp[window]
                if dp[i]:
                    break

                
        return dp[0]

        '''
        s = "abcd"
        dp = [T, T, T, F, T]
        
        len(s) = 4
        i = 0
        word = "a" -> 1

        window = 0 + 1 = 1 =  1



        '''
        
        


        