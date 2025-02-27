Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        current = head 
        x = []
        while current: 
            x.append(current.val)
            current = current.next 
        if x == x[::-1]: 
            return True 
        else: 
            return False