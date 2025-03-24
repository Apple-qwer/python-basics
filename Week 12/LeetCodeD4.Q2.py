Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
            x = [(root.right, root.left)]
            while x: 
                y, z = x.pop(0)
                if not y and not z:
                    continue 
                if not y or not z or y.val != z.val:
                    return False 
                x.append((y.left, z.right))
                x.append((y.right, z.left))
            return True 