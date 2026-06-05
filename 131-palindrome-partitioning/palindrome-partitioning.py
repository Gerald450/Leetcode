class Solution:
    def partition(self, s: str) -> List[List[str]]:
        '''
        input: string
        output: list of list of palindromes

        edge: no palidromes, uppercase, length is one

        plan:
        use backtrack
        check is substring is a palindrome if so, append to current path
        and pop after backtracking
        start new path at end + 1
        '''

        def is_palindrome(word):
            l, r = 0, len(word) - 1
            while l <= r:
                if word[l] != word[r]:
                    return False
                l += 1
                r -= 1
            return True
        
        path = []
        output = []

        def backtrack(start):
            if start == len(s):
                output.append(path[:])

            for end in range(start, len(s)):
                word =  s[start: end + 1]
                if is_palindrome(word):
                    path.append(word)
                    backtrack(end + 1)
                    path.pop()


        backtrack(0)

        return output



        '''
        'aab'
        path = []
        output = []

        end: 0 -> 3
        word = s[0:1] = a
        True
        backtrack(1)
        end: 1 -> 3
        ....
        output = [['a','a','b], ['aa', 'b']]

        runtime: O(n * 2^n)
        extra space: O(n)


        '''