# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def allPossibleFBT(self, n: int) -> list[TreeNode | None]:
        '''
        Note: only odd nums form full trees
        edge: even num

        plan:
        use recursion with memoization
        make a helper recursive build function that returns the trees
        each combination should have it's own trees array
        use a loop to try new combos
        '''

        memo = {}

        def build(nodes):
            if nodes % 2 == 0:
                return []
            if nodes == 1:
                return [TreeNode()]
            if nodes in memo:
                return memo[nodes]

            trees = []

            for left_count in range(1, nodes, 2):
                right_count = nodes - 1 - left_count

                left_nodes = build(left_count)
                right_nodes = build(right_count)

                for left in left_nodes:
                    for right in right_nodes:
                        root = TreeNode()
                        root.right = right
                        root.left = left
                        trees.append(root)

            memo[nodes] = trees
            return trees

        return build(n)

        