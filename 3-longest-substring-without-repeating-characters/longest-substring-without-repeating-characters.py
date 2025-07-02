class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        l, substring = 0, 0
        hashmap = set()


        for r in range(len(s)):
            
            while s[r] in hashmap:
                hashmap.remove(s[l])
                l += 1
            hashmap.add(s[r])
            substring = max(substring, len(hashmap))

        return substring
