class Solution:
    def longestPalindrome(self, s: str) -> str:
        '''
        input: string
        output: substr of longest palidrome

        edge cases: odd or even, if len is 1

        plan:
        traverse through str and make each point a midpoint
        use two pointers to check left and right if they match, if so
        check if the longest and save it
        return longest
        '''

        maxWin = 0
        l, r = 0, 0
        win = (l, r)


        for i in range(len(s)):

            #odd
            l, r = i, i
            while l >= 0 and r < len(s) and s[l] == s[r]:
                l -= 1
                r += 1
            window = r - l  - 1
            if window > maxWin:
                maxWin = window
                win = (l + 1, r - 1)
            
            #even
            l, r = i, i + 1
            while l >= 0 and r < len(s) and s[l] == s[r]:
                l -= 1
                r += 1
            window = r - l - 1
            if window > maxWin:
                maxWin = window
                win = (l + 1, r - 1)

        l, r = win
        return s[l:r + 1]

        '''
        "babad"
        
        maxWin = 0
        l, r = 0, 0
        win = (l,r)
        i = 0 -> 5
        l, r = -1, 1
        win = 1 - -1 + 1 = 3



        '''

                

                




        