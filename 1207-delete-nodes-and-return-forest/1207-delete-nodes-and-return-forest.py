# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
import collections

class Solution:
    def delNodes(self, root: Optional[TreeNode], to_delete: List[int]) -> List[TreeNode]:
        to_delete_set = set(to_delete)
        forest = []

        def dfs(node, is_root):
            if not node:
                return None

            # check if this node should be deleted
            deleted = node.val in to_delete_set

            # if it's a root and not deleted, add it to forest
            if is_root and not deleted:
                forest.append(node)

            # recursively check children
            node.left = dfs(node.left, deleted)
            node.right = dfs(node.right, deleted)

            # return None if deleted, else keep the node
            return None if deleted else node

        dfs(root, True)
        return forest
