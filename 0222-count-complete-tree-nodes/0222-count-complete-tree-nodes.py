# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        count = 0
        seen = set()

        def dfs(node):
            nonlocal count, seen
            if not node:
                return
            if node in set():
                return
            
            seen.add(node)
            count += 1

            dfs(node.left)
            dfs(node.right)

        dfs(root)


        return count
        