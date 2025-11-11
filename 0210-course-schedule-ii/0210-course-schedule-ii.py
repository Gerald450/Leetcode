from collections import defaultdict
from typing import List

class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        '''
        input: numCourses -> int, prerequisites -> arr of arr
        output: list of courses in order

        edge cases: cycle: return empty, 

        plan:
        make an adj graph -> {0: [1, 4]} e.tc
        initialise otp
        need a set for cycles
        loop through numCourses:
            call dfs(course): if false return []

        dfs => {
            base case: if in visitesd: return True
            if in set: return False

            add to set

            loop through neighbours: if dfs(nei) is false return false

            remove from set
            make adj[course] empty
            append to otp
        }

        return otp

        '''

        adj = defaultdict(list)
        otp = []

        for a, b in prerequisites:
            adj[a].append(b)

        visiting = set()
        visited = set()
        def dfs(course):
            if course in visited:
                return True
            if course in visiting:
                return False
            
            
            visiting.add(course)

            for nei in adj[course]:
                if not dfs(nei):
                    return False
            
            visiting.remove(course)
            visited.add(course)
            otp.append(course)
            return True


        for i in range(numCourses):
            if not dfs(i):
                return []

        return otp


        '''
        adj = {
            0: 1
        }

        i = 0 -> 2
        visited = {0}
        visiting = {0}
        otp = [1, 0]

        dfs(0) => {
            nei = 1 -> 1
            dfs(1) => {
                
            }
        }



        adj = {
            1:[],
            2:[],
            3:[1, 2]
        }
        visited = {0, 1, 2, 3}
        visiting = {3}
        otp = [0, 1, 2, 3]
        
        i = 3 -> 4
        dfs(0) => {
            True
        }
        dfs(1) => {
            nei = 0 -> 0
            dfs(0) => {
                True
            }
        }

        dfs(2) => {
            nei = 0 => 0
            dfs(0) => {
                True
            }
        }

        dfs(3) => {
            nei = 2 -> 2
            dfs
        }



        '''