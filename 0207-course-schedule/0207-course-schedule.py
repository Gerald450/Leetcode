class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj = collections.defaultdict(list)
        seen = set()

        for pre in prerequisites:
            a, b = pre
            adj[a].append(b)
        print(adj[0])

        def dfs(num):
            if num in seen:
                return False
            if adj[num] == []:
                return True

            seen.add(num)

            for pre in adj[num]:
                if not dfs(pre):
                    return False
            seen.remove(num)
            adj[num] = []
            return True


        for i in range(numCourses):
            if not dfs(i):
                return False
        return True
        