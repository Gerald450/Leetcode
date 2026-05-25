class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        '''
        input: string s
        output: int: length of longest

        edge: empty, no sequence

        'abcdduwscba'

        plan:
        make a new string s1, which is the reverse of s
        do LCS on the two strings{
            make a 2d grid with rows and cols the lengths of the strings plus one
            intialise the grids to zero
            loop from the back
            if two letters are the same update cell to one plus the value in diagonal cell
            if they are not take the max num between the two values in bottom and right cells 
        }
        return corner grid
        
        '''

        rows, cols = len(s) + 1, len(s) + 1

        dp = [[0 for _ in range(cols)] for _ in range(rows)]

        idx = len(s) - 1
        for i in range(rows - 2, -1, -1):
            for j in range(cols - 2, -1, -1):
                
                if s[i] == s[idx - j]:
                    dp[i][j] = 1 + dp[i + 1][j + 1]
                else:
                    dp[i][j] = max(dp[i + 1][j], dp[i][j + 1])

        return dp[0][0]


        '''
          d b b c
        c[2,2,1,1,0]
        b[2,2,1,0,0]
        b[1,1,1,0,0]
        d[1,0,0,0,0]
         [0,0,0,0,0]]

        rows=5-2=3
        cols=5-2=3
        i=3
        j=2
        idx=3
        s[3] = d,s[0] = c
        s[3] = d, s[1] = b
        ....
        s[0] = c, s[3]= d

        runtime: O(n^2)
        space: O(n^2)
        '''

