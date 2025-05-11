class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        x = [] 
        for i in edges[0:2]: 
            x.extend(i)
        y = set(x) 
        for i in y: 
            z = x.count(i)
            if z >= 2: 
                return i
        return -1
    