class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        #sort it
        #if intervals[i][1] > interval[i+1][0]
        #end max(intervals[i][1], intervals[i+1][1])

        intervals.sort(key=lambda x:x[0])

        stack = [intervals[0]]

        for i in range(1, len(intervals)):
            if stack:
                start, end = stack.pop()
                if end >= intervals[i][0]:
                    stack.append([start, max(end, intervals[i][1])])
                else:
                    stack.append([start, end])
                    stack.append(intervals[i])

        return stack

       


