class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj = collections.defaultdict(list)

        for p in prerequisites:
            a, b = p
            adj[a].append(b)

        visitCrs = set()

        def dfs(crs):
            if adj[crs] == []:
                return True
            if crs in visitCrs:
                return False

            visitCrs.add(crs)
            for pre in adj[crs]:
                if not dfs(pre):
                    return False
            visitCrs.remove(crs)
            adj[crs] = []
            return True


        for p in range(numCourses):
            if not dfs(p): return False

        return True
            

        

        


        