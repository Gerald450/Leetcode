class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        otp = []
        anagrams = {}


        for word in strs:
            sortedWord = str(sorted(word))
            if sortedWord in anagrams:
                anagrams[sortedWord].append(word)
            else:
                anagrams[sortedWord] = [word]
            

        return list(anagrams.values())

