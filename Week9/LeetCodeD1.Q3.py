class Solution:
    def longestPalindrome(self, s: str) -> int:
        x = {}
        z = 0
        Odd = False 
        for i in s: 
            x[i] = x.get(i, 0) + 1 
        for i in x.values(): 
            if i % 2 == 0: 
                z += i 
            else: 
                z += i - 1 
                Odd = True 
        if Odd: 
            z += 1
        return z 
