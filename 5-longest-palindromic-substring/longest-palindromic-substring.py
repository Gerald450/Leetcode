class Solution:
    def longestPalindrome(self, s: str) -> str:
        length = 0
        res = (0,0) 
        

        for i in range(len(s)):
            #odd
            l, r = i, i

            while l >= 0 and r < len(s) and s[l] == s[r]:
                window = r - l + 1
                if window > length:
                    length = window
                    res = (l, r)
                l -= 1
                r += 1

            #even
            l, r = i, i + 1

            while l >= 0 and r < len(s) and s[l] == s[r]:
                window = r - l + 1
                if window > length:
                    length = window
                    res = (l, r)
                l -= 1
                r += 1

        l,r = res

        return s[l: r+ 1]

                

                




        