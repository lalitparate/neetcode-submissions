class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adj = [[] for _ in range(n)]

        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)


        visit = set()

        def bfs(node):
            q = deque([node])
            visit.add(node)
            while(q):
                cur = q.popleft()
                for nei in adj[cur]:
                    if nei not in visit:
                        visit.add(nei)
                        q.append(nei)

        
        res = 0
        for node in range(n):
            if node not in visit:
                bfs(node)
                res += 1
        return res
