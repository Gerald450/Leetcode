# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        otp = []
        res = []
        
        def dfs(node):
            if not node:
                return
            
            otp.append(node.val)

            if not node.left and not node.right:
                res.append(otp.copy())
            else:
                dfs(node.left)
                dfs(node.right)
            
            otp.pop()

        dfs(root)
        for group in res:
            if sum(group) == targetSum:
                return True

        return False
            

            


        


            

        