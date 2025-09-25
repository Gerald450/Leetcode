import collections
from typing import List

class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        adj = collections.defaultdict(list)

        for pre in prerequisites:
            a, b = pre
            adj[a].append(b)
            #0:1

        otp = []
        visiting, visited = set(), set()
        def dfs(course):
            if course in visiting:
                return False
            if course in visited:
                return True

            visited.add(course)
            visiting.add(course)

            for nei in adj[course]:
                if not dfs(nei):
                    return False
            visiting.remove(course)
            otp.append(course)
            return True

        for i in range(numCourses):
            if not dfs(i):
                return []

        return otp