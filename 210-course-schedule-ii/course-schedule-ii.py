import collections
from typing import List

class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph = collections.defaultdict(list)
        for a, b in prerequisites:
            graph[b].append(a)   # edge b → a

        visited = set()   # fully processed
        path = set()      # current recursion path
        order = []        # topological order
        cycle = False

        def dfs(node):
            nonlocal cycle
            if node in path:   # cycle detected
                cycle = True
                return
            if node in visited:
                return

            path.add(node)
            for nei in graph[node]:
                dfs(nei)
            path.remove(node)
            visited.add(node)
            order.append(node)

        for i in range(numCourses):
            if i not in visited:
                dfs(i)
            if cycle:
                return []   # cycle found → no valid ordering

        return order[::-1]  # reverse to get correct order
