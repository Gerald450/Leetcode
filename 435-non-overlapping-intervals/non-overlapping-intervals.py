class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        '''
        input: list of intervals
        output: int

        edge: no overlap

        plan:
        sort by first in ascending, if equal sort by second in ascending
        [[1,2] ,[1,3], [2,4],[3,4]]
        use stack
        compare last of prev to first of curr
        if it's greater then that's an overlapp, dont add to stack
        increment count
        '''

        stack = []
        intervals.sort(key=lambda x: (x[0], x[1]))
        count = 0
    #[1, 7] [2, 5]
        for interval in intervals:
            start, end = interval
            if stack and stack[-1][1] > start:
                count += 1
                if stack[-1][1] > end:
                    stack.pop()
                    stack.append(interval)
            else:
                stack.append(interval)


        return count



        