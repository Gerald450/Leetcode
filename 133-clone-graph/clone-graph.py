"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""
from collections import defaultdict
from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        '''
        input: node
        output: node of copy

        edge: empty

        plan:
            create a hashmap old: new

            traverse Node and neightbours and create copies of them
            dfs => {
                base case: if node in oldToNew: return oldToNew[node]
                copy = Node(node.val)
                oldToNew[node].append(copy)
                for nei in node.neighbours:
                    copy.neigborrs.append(dfs(nei))
                return copy
            }

        '''

        if not node:
            return None

        
        oldToNew = {}

        def dfs(node):
            if node in oldToNew:
                return oldToNew[node]
            if not node:
                return

            copy = Node(node.val)
            oldToNew[node] = copy

            for nei in node.neighbors:
                copy.neighbors.append(dfs(nei))

            return copy



        return dfs(node)