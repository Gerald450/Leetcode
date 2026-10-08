class Solution:
    def wordBreak(self, s: str, wordDict: list[str]) -> list[str]:
        
        '''
        backtracking
        find word, add to path, recursively call the end and new path to find more words
        pop to explore new path
        '''

        words = set(wordDict)
        result = []

        def backtrack(start, path):
            if start == len(s):
                result.append(" ".join(path))
                return

            for end in range(start + 1, len(s) + 1):
                partition = s[start: end]

                if partition in words:
                    path.append(partition)
                    backtrack(end, path)
                    path.pop()

        backtrack(0, [])

        return result

        '''
        runtime: O(n.2^n)
        space: O(n.2^n)
        '''
            


