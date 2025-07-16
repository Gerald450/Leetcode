# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        n = 0
        otp = 0

        def dfs(node):
            nonlocal n, otp
            if not node or n >= k:
                return
            #commit
            dfs(node.left)

            if k - 1 == n:
                otp = node.val
            n += 1

            dfs(node.right)

        dfs(root)

        return otp
                
        