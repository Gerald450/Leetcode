class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:

        adj = collections.defaultdict(list)
        otp = []

        for idx, eq in enumerate(equations):
            a, b = eq
            adj[a].append([b, values[idx]])
            adj[b].append([a, 1/values[idx]])
        
        

        def bfs(curr, target):
            if target not in adj or curr not in adj:
                return -1

            q = collections.deque()
            visited = set()
            q.append([curr, 1])
            visited.add(curr)

            while q:
                n, w = q.popleft()

                if n == target:
                    return w
                for nei in adj[n]:
                    node, weight = nei
                    
                    if node not in visited:
                        q.append([node, w * weight])
                        visited.add(node)

            return -1


        for q in queries:
            otp.append(bfs(q[0], q[1]))
        
        return otp



        