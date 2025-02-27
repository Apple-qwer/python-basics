class Solution:
    def firstUniqChar(self, s: str) -> int: 
        x = {} 
        for i in s: 
            x[i] = x.get(i,0) + 1 
        for i in x.keys(): 
            if x[i] == 1: 
                for j in range(len(s)): 
                    if s[j] == i: 
                        return j
        
        return -1