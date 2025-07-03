from collections import Counter
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        ransomNoteDic = Counter(ransomNote)
        magazineDic = Counter(magazine)

        for key, value in ransomNoteDic.items():
            if ransomNoteDic[key] > magazineDic[key]:
                return False

        return True
        