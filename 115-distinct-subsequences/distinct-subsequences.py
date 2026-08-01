class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        '''
        input: s and t: str
        output: ways: int

        edge: s or t are empty, or both, non engl, s < t

        plan:
        recursion with memoization
        store a cache with i, j indices for curr i and j in s and t
        how many ways t[j:] from s[i:]
        {
            parameter => s, t
            base: if j out of bounds: return 1
            if i out of bounds: return 0
            if (i,j) in cache: return cache[(i,j)]
            
            if chars at i and j are equal: ways += recursively call with j+1, i+1, dont take
            if not equal: ways += call with i + 1, j

            cache[(i,j)] = ways
        }
        call recursive function
        return ways
        '''

        cache = {}
    
    
        def find_ways(i, j):
            
            if j >= len(t): return 1
            if i >= len(s): return 0
            if (i, j) in cache: return cache[(i, j)]
            ways = 0
            ways += find_ways(i + 1, j)
            if s[i] == t[j]:
                #take
                ways += find_ways(i + 1, j + 1)
            cache[(i, j)] = ways
            return ways

    
        return find_ways(0, 0)


        '''

        '''