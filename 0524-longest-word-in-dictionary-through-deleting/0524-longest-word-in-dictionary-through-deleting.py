from typing import List

class Solution:
    def findLongestWord(self, s: str, dictionary: List[str]) -> str:
        maxWord = ""

        for word in dictionary:
            l = 0
            letterCount = 0

            for letter in word:
                foundLetter = False

                while l < len(s) and not foundLetter:
                    if s[l] == letter:
                        foundLetter = True
                        letterCount += 1
                    l += 1

            if letterCount == len(word):
                # choose longer word or lexicographically smaller if equal
                if len(word) > len(maxWord) or (len(word) == len(maxWord) and word < maxWord):
                    maxWord = word

        return maxWord
