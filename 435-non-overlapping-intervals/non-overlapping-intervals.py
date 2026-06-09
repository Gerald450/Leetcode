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

        if not intervals:
            return 0

        intervals.sort(key=lambda x: (x[0], x[1]))
        count = 0
        prev_end = intervals[0][1]

        for interval in intervals[1:]:
            start, end = interval
            if prev_end > start:
                count += 1
                if prev_end > end:
                    prev_end = end
            else:
                prev_end = end

        return count

    '''
    runtime:O(nlogn)
    space:O(1)
    '''

        