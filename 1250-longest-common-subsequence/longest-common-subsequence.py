class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        '''
        input: text1: str, text:str
        output: LCS: int

        edge: empty str on either, no common subsequence

        plan:
        2dp, bottom-up
        create a 2d grid with rows length of text1 + 1, and columns length of text2 + 2
        extra row and column are for edge comparisons and will be initialised to zeros
        if two letters match, update grid to 1+ number in diagonal
        if they are not, take the minimum of grid bottom and one to the right
        return grid at top corner
        '''

        rows, cols = len(text1) + 1, len(text2) + 1
        '''
        [[3,4,5,5,2]
        [0,0,0,0,0]]

        '''
        dp = [[0 for _ in range(cols)] for _ in range(rows)] 


       
        for i in range(rows - 2, -1, -1):
            for j in range(cols - 2, -1, -1):
                if text1[i] == text2[j]:
                    dp[i][j] = 1 + dp[i + 1][j + 1]
                else:
                    dp[i][j] = max(dp[i + 1][j], dp[i][j + 1])



        return dp[0][0]


        '''
          a. c. b.
       [a[2, 1, 1, 0], 
        b[1, 1, 1, 0], 
        c[1, 1, 0, 0], 
         [0, 0, 0, 0]]
        
        rows = 4 - 2 = 2
        cols = 4 - 2 = 2
        text1[2] = c
        text2[2] = b
        text2[1] = c
        text2[0] = a


        i = 1
        text1[1] = b
        
        '''
        