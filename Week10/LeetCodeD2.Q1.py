class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def deleteDuplicates(self, head):
        current = head 
        while current.next: 
            if current.val == current.next.val: 
                current.next = current.next.next 
            current = current.next 
        return head 