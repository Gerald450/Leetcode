# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        p = deque([root])
        level = 0

        while p:

            for i in range(len(p)):
                node = p.popleft()
                if node.left:
                    p.append(node.left)
                if node.right:
                    p.append(node.right)
            level += 1
        
        return level

        