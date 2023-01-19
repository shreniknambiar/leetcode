class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        current = head
        prev = None
        currSize = 1
        if(left == 0 and right == 0):
            return None
        if(left == 1 and right == 1):
            return head
        
        while(current):
            if(currSize>=left and currSize<=right):
                next = current.next
                current.next = prev
                prev = current
                current = next
            currSize+=1
        return prev