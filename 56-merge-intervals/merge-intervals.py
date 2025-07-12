class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        #1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18
        #if end >= start
        #sort by start
        # sorted(intervals, key=lambda x: x[0], reverse = True)

       

        if len(intervals) == 1:
            return intervals

        intervals = sorted(intervals, key=lambda x:x[0])
        stack = [intervals[0]]


        for x, y in intervals:
            start, end = stack[-1]

            if end >= x:
                stack.pop()
                stack.append([start, max(y, end)])
            else:
                stack.append([x, y])

        return stack

       


