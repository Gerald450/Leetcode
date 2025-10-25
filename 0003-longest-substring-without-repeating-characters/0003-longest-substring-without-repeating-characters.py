class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        hashSet = set()
        l = 0
        maxWin = 0

        for r in range(len(s)):

            while s[r] in hashSet:
                hashSet.remove(s[l])
                l += 1
            
            hashSet.add(s[r])
            window = r - l + 1
            maxWin = max(maxWin, window)

        return maxWin


        '''
        "pwwkew"
              ^
        l = 3
        r = 5
        s[l] = k
        s[r] = e
        hashSet = {k, e, w}
        window = 3
        maxWin = 3
        '''
       