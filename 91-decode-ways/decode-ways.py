class Solution:
    def numDecodings(self, s: str) -> int:
        '''
        input: string of nums
        output: num of ways to decode

        edge: leading 0, len == 1

        plan: 
        recursively calculate the valid ways
        base: if we reach end return 1
        increment ways with each valid call
        '''
        cache = {}
        
        def recursion(i):
            ways = 0
            if i >= len(s):
                return 1
            if i in cache:
                return cache[i]

            
            if s[i] != '0':
                ways += recursion(i + 1)
            
            two_digits = s[i:i + 2]
            if len(two_digits) != 1 and'10' <= two_digits <= '26':
                ways += recursion(i + 2)


            cache[i] = ways
            return ways


        
        return recursion(0)

