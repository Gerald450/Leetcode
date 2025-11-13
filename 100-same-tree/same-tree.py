# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        '''
        input: two roots, p and q
        output: boolean, if they are the same
        Match: Dfs
        edge cases: p is empty, q is not or vice versa
        if both empty: return true

        base cases:
        if not p and not q: true
        if not p or not q: false

        return p.val == q.val and  traverse q.right and p.right and traverse q.left and p.left
        '''

        if not p and not q: 
            return True
        
        if not p or not q:
            return False


        return (p.val == q.val and self.isSameTree(p.right, q.right) and self.isSameTree(p.left, q.left))
            

                

        