class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        triangle.reverse()


        for i in range(len(triangle) - 1):
           
            for j in range(len(triangle[i]) - 1):
                minVal = min(triangle[i][j], triangle[i][j+1])
                triangle[i + 1][j] += minVal

        
        
        return triangle[-1][0]

        