from collections import Counter
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False


        hashmapS = Counter(s)
        hashmapT = Counter(t)


        if hashmapS != hashmapT:
            return False
        return True
        