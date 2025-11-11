from collections import defaultdict
from collections import deque
class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:

        '''
        input: eqns, values, queries
        output: answers to queries

        edge: cant find ans, division by self, undefined letter

        plan:
        make an adj dictionary
        a -> b => 2
        b -> a => 1/2
        adj[a] = [b, 2]
        adj[b] = [a, 1/2]

        need a set to avoid cycles
        loop in qeuries: pass two values in bfs as start and target
        traverse through the adj graph till find target
        base case: if start in set(), return 

        '''
        adj = defaultdict(list)
        otp = []

        for i in range(len(equations)):
            a, b = equations[i]
            adj[a].append([b, values[i]])
            adj[b].append([a, 1 / values[i]])

        visiting = set()

        def bfs(start, target):
            
            if start not in adj or target not in adj:
                return -1
            
            q = deque([(start, 1)])
            visiting = set([start])
            while q:
                node, weight = q.popleft()

                if node == target:
                    return weight
                
                for nei in adj[node]:
                    # a : [[b, 2], [c, 4]]
                    if nei[0] not in visiting:
                        q.append((nei[0], weight * nei[1]))
                        visiting.add(nei[0])
                
            return -1
        

        for start, target in queries:
            otp.append(bfs(start, target))

        return otp


      