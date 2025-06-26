class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        otp = ''
        shortest = strs[0]
        flag = True

        for i, word in enumerate(strs):
            if len(word) < len(shortest):
                shortest = word

        if len(shortest) == 0:
            return ''

        
        prev = strs[0][0]

        for i in range(len(shortest)):
            
            for j in range(len(strs)):
                
                if prev != strs[j][i]:
                    flag = False
                    return otp
                prev = strs[j][i]
            otp += prev
            
            if i+1 < len(shortest):
                prev = strs[j][i+1]
           
        

        return otp
            
        