class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        sList = s.split(' ')
        mapping = {}

        if len(sList) != len(pattern):
            return False

        for i in range(len(pattern)):
            if pattern[i] in mapping:
                if mapping[pattern[i]] != sList[i]:
                    return False
            else:
                mapping[pattern[i]] = sList[i]

        duplicates = set(mapping.values())

        if len(duplicates) != len(mapping):
            return False
        
        return True

        