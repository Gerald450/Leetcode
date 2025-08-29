class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:

        adj = collections.defaultdict(list)

        for i, val in enumerate(equations):
            a, b = val
            adj[a].append([b, values[i]])
            adj[b].append([a, 1/values[i]])

        def bfs(numero, target):
            if numero not in adj or target not in adj:
                return -1

            q, visit = deque(), set()
            q.append([numero, 1])

            while q:
                n, w = q.popleft()
                if n == target:
                    return w
                for nei in adj[n]:
                    l, weight = nei
                    if l not in visit:
                        q.append([l, w * weight])
                        visit.add(l)
            return -1


        return [bfs(q[0], q[1]) for q in queries]


            



        