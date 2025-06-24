class Solution:
    def romanToInt(self, s: str) -> int:
        romanDict = {
            'I':1,
            'V':5,
            'X':10,
            'L':50,
            'C':100,
            'D':500,
            'M':1000
        }
        total = 0
        l = 0

        while l < len(s):
            if l < len(s) - 1 and romanDict[s[l+1]] > romanDict[s[l]] :
                total += (romanDict[s[l+1]] - romanDict[s[l]])
                l += 1
            else:
                total += romanDict[s[l]]

            l += 1
        return total
        
            

        