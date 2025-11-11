class Solution:
    def maxEnvelopes(self, envelopes: List[List[int]]) -> int:
        '''
        output: max num of envelopes that can get into each other including the outside one

        edge cases: empty return 0
                    all same return 1


        sort them by width, if they same, sort by h in reverse [[2,3], [5,4], [6,7], [6,4]]
        count starts at 1
        compare w and h if they all less increment count
        do lis

        '''
        envelopes.sort(key=lambda x: (x[0], -x[1]))
        dp = []

        def binary_search(num, arr):
            l, r = 0, len(arr) - 1

            while l <= r:
                m = (l + r) // 2
                if arr[m] < num:
                    l = m + 1
                elif arr[m] > num:
                    r = m - 1
                else:
                    return m
            
            return l

        for w, h in envelopes:
            length = len(dp)

            # while i < length:
            #     if h <= dp[i]:
            #         break
            #     i += 1

            pos = binary_search(h, dp)
            
            if pos == length:
                dp.append(h)
            else:
                dp[pos] = h
        
        return len(dp)



        '''
        [[1,3],[3,5],[6,7],[6,8],[8,4],[9,5]]

        envelopes = [[1,3], [3,5], [6,8], [6,7], [8,4], [9,5]]
                                                   ^ 
        prev = [6, 8]
        count = 3
        w, h = 6, 7
        prevW, prevH = 6, 8



        '''

    
    
        
        
                

                
                

        