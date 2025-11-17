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

        prev =None

        def dfs(node):
            nonlocal prev
            if not node:
                return

            # traverse in reverse preorder: right -> left -> node
            dfs(node.right)
            dfs(node.left)

            # rewire pointers
            node.right = prev
            node.left = None
            prev = node


        dfs(root)


        