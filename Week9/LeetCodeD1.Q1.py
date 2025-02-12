class Solution:
    def isAnagram(self, s, t):
        if len(s) != len(t):
            return False 
        x = list(t)
        for i in s: 
            if i in x: 
                x.remove(i)
            else:
                return False 
        return True 