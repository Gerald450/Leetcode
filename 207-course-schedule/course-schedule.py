from collections import deque, defaultdict
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        '''
        input: numCourses -> int, prerequisites -> arr of arr
        output: boolean

        edge cases: cycle [[1,0], [0,1]]

        plan:
        make an adj graph: adj[course] = [pre1, pre2.....]
        loop in range numCourses
        dfs(course) through adj
        use set to detect cycles 
        base case: if course in set: return False
        at the end return True

        '''
        adj = defaultdict(list)

        for a, b in prerequisites:
            adj[a].append(b)

        visiting = set()
        
        def dfs(course):
            if course in visiting:
                return False
            if course not in adj:
                return True
            if not adj[course]:
                return True

            visiting.add(course)

            for nei in adj[course]:
                if not dfs(nei):
                    return False
            
            visiting.remove(course)
            adj[course] = []
            return True



        for i in range(numCourses):
            if not dfs(i):
                return False

        return True

        '''
        numCourses = 2, pre = [[1,0]]

        adj = {
            1: 0
        }

        visiting = {1}

        i = 1 -> 2
        dfs(1)
        adj[1] = 0
            dfs(0)
            

        '''

