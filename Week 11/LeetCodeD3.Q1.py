class Solution:
    def isValid(self, s: str) -> bool: 
        x = [] 
        y = {')' : '(', "]" : "[", "}" : "{"}
        for i in s: 
            if i in y: 
                if x: 
                    z = x.pop()
                else: 
                    z = "h"
                if y[i] != z: 
                    return False
            else:
                x.append(i)
        if not x: 
            return True 
        else: 
            return False