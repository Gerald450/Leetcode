class Solution:
    def numTrees(self, n: int) -> int:
        '''
        input: n: int
        output: int

        edge: n == 1

        plan:
        use recursion
        try every possible
        count all left possibillities
        count all right possibilities, multiply them and add them to total
        '''


        cache = {}
        def count(nodes):
            if nodes <= 1:
                return 1
            if nodes in cache:
                return cache[nodes]
            
            ways = 0
            for root in range(1, nodes + 1):
                left = root - 1
                right = nodes - root

                ways += count(left) * count(right)
            
            cache[nodes] = ways
            return ways


        return count(n)


        '''
        time: O(n^2)
        space: O(n)
        '''

            

            




       
            



        