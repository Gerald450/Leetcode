# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque

class Solution:
    def delNodes(self, root: Optional[TreeNode], to_delete: List[int]) -> List[TreeNode]:
        '''
        input: binary tree
        output: forest of disjoint trees(just roots in a list)

        edge cases: not root

        plan:

        traverse tree: bfs
        if next node is in to_delete, make pointer point to None
        before that store node in temp, add children as roots to the list

        '''

        to_delete = set(to_delete)
        otp = set([root])

        def dfs(node):
            if not node:
                return None

            res = node
            if node.val in to_delete:
                res = None
                otp.discard(node)
                if node.left: otp.add(node.left)
                if node.right: otp.add(node.right)
            
            node.right = dfs(node.right)
            node.left = dfs(node.left)

            return res
        
        dfs(root)

        return list(otp)


        