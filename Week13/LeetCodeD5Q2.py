Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        if not root: 
            return None 
        result = [] 
        x = [root]
        while x: 
            y = 0 
            c = len(x)
            z = []
            for i in x: 
                y += i.val 
                if i.left: 
                    z.append(i.left)
                if i.right:
                    z.append(i.right)
            result.append(y/c)
            x = z
        return result