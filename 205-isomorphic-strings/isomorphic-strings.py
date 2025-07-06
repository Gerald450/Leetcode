class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        mapping = {}


        for i in range(len(s)):
            if s[i] in mapping:
                if mapping[s[i]] != t[i]:
                    return False
            else:
                mapping[s[i]] = t[i]

        otp = set(mapping.values())

        if len(mapping) != len(otp):
            return False

        return True
        