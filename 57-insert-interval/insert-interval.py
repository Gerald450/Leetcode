class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        if len(intervals) == 0:
            return [newInterval]

        intervals.append(newInterval)

        intervals = sorted(intervals, key=lambda x:x[0])

        stack = [intervals[0]]

        for x, y in intervals:
            start, end = stack[-1]

            if end >= x:
                stack.pop()
                stack.append([start, max(end, y)])
            else:
                stack.append([x, y])

        return stack
        