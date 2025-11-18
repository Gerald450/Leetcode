# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        preorder = nlr

        input: root
        output: root but with .left null
        edges: empty

        plan:
        dfs(node, tempNode)
        if we have a left subtree, store right subtree elsewhere
        if we reach leaf node then root.left = leafnode and leaf.left = temp, set .right to null

        """

        

        def dfs(node):
            if not node:
                return None

            leftTail = dfs(node.left)
            rightTail = dfs(node.right)

            if leftTail:
                leftTail.right = node.right
                node.right = node.left
                node.left = None

            last = rightTail or leftTail or node
            return last


        dfs(root)


        