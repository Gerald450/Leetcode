class Solution:
    def makeConnected(self, n: int, connections: List[List[int]]) -> int:

        if len(connections) < n - 1:
            return -1

        adj = collections.defaultdict(list)

        for a, b in connections:
            adj[a].append(b)
            adj[b].append(a)


        visited = set()

        def bfs(node):
            q = collections.deque([node])
            visited.add(node)
            while q:
                n = q.popleft()
                for nei in adj[n]:
                    if nei not in visited:
                        q.append(nei)
                        visited.add(nei)
            


        components = 0
        for i in range(n):
            if i not in visited:
                components += 1
                bfs(i)

        return components - 1

        