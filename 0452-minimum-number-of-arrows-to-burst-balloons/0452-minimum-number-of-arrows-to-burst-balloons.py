class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        stack = []
        points.sort(key=lambda x:x[0])


        for p in points:
            start, end = p
            if stack and start <= stack[-1]:
                val = stack.pop()
                stack.append(min(val, end))
            else:
                stack.append(end)
           
        
   
        
        return len(stack)

        