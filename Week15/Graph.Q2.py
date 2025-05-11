class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        x = {}
        for u, v in edges:
            x[u] = x.get(u, [])
            x[u].append(v)
            x[v] = x.get(v, [])
            x[v].append(u)
 
        visited = set()
        y = [source]
        while y: 
            node = y.pop() 
            if node == destination: 
                return True 
            if node not in visited:
                visited.add(node)
                for i in x[node]:
                    y.append(i)
        return False 