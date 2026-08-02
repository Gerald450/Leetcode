class Solution:
    def countSubstrings(self, s: str) -> int:
        '''
        input: string s
        output: int: num

        edge: empty, 1, uppercase

        plan: 
        loop through
        check for odd, check for even palindrome making the current index the middle
        increment every time we find a valid palindrome and move one

        return total
        '''

        total = 0

        for i in range(len(s)):
            
            #even
            l, r = i, i
            while l >= 0 and r < len(s):
                if s[l] == s[r]:
                    total += 1
                    l -= 1
                    r += 1
                else:
                    break

            #odd
            l, r = i, i + 1
            while l >= 0 and r < len(s):
                if s[l] == s[r]:
                    total += 1
                    l -= 1
                    r += 1
                else:
                    break 


        return total
    

        