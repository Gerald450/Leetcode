# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def allPossibleFBT(self, n: int) -> list[TreeNode | None]:
        '''
        edge: even num of nodes

        plan:
        use recursion
        use memoization
        if num of nodes is even: return []
        use a loop to make differnt iterations of left_nodes and right_nodes
        use another loop to make the trees and add the head to the otp list
        return trees in recursive func
        '''

        memo = {}

        def make_tree(nodes):
            if nodes % 2 == 0:
                return []

            if nodes in memo:
                return memo[nodes]

            if nodes == 1:
                return [TreeNode()]
            
            tree = []
            
            for left_count in range(1, nodes, 2): #odd nums only
                right_count = nodes - left_count - 1

                left_nodes = make_tree(left_count)
                right_nodes = make_tree(right_count)


                for left in left_nodes:
                    for right in right_nodes:
                        root = TreeNode()
                        root.left = left
                        root.right = right
                        tree.append(root)

            memo[nodes] = tree
            return tree

        return make_tree(n)


