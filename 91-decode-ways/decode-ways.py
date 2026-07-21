class Solution:
    def numDecodings(self, s: str) -> int:
        '''
        input: string
        output: int: num of ways

        edge: empty, 1, 2, leading zero

        plan:
        recursion
        if the value at that index is valid, recurse
        if the value of the two adj indices is valid, recurse
        accumulate ways along the way

        base case: if we reach end of string =, return 1

        return ways
        '''

        cache = {}
        
        def findWays(i):

            if i >= len(s):
                return 1

            if i in cache:
                return cache[i]

            ways = 0

            if s[i] != '0':
                ways += findWays(i + 1)
            if len(s[i:i+2]) == 2 and '10' <= s[i:i+2] <= '26':
                ways += findWays(i + 2)

            cache[i] = ways
            return ways



        return findWays(0)


        '''
        runtime: O(n)
        space: O(n) fo cache and recursion stack
        '''