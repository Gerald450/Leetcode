class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:


        for mat in matrix:
            if mat[0] <= target <= mat[-1]:
                
                for i in range(len(mat)):
                    if mat[i] == target:
                        return True
                #commit

        return False

        