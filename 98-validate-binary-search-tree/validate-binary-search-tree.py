# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        prev = None
        flag = True
        

        def dfs(node):
            nonlocal prev, flag
            if not node or not flag:
                return
            
            dfs(node.left)

            if prev:
                if prev.val >= node.val:
                    flag = False
            prev = node

            dfs(node.right)

        
        dfs(root)

        return flag


        