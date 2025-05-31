from collections import deque
class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        graph = {}
        for u, v, w in times:
            graph[u] = (v, w) 
        D = {} 
        D[k] = 0 
        queue = deque([(0, k)])

        while queue:
            current_distance, n = queue.popleft()
            if current_distance > D[n]:
                continue
            for neighbor, weight in graph[n]:
                if neighbor not in D:
                    D[neighbor] = current_distance + weight 
                    queue.append((current_distance + weight, neighbor))

        return max(D.values()) 
