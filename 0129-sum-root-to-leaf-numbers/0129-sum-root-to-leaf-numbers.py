# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        #dfs 
        #base case: if not node: return 0
        #nrl
        #add to list then do operations
        otp = []
        res = []
        total = 0

        def dfs(node):
            if not node:
                return 

            otp.append(str(node.val))
            
            if not node.left and not node.right:
                res.append(otp.copy())
            else:
                dfs(node.right)
                dfs(node.left)
            
            otp.pop()
         

        dfs(root)

        for re in res:
            total += int(''.join(re))

        return total
           