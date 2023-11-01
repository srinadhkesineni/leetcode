# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if not head:
            return False
        s=set()
        a=1
        while head:
            if head in s:
                return True
            else:
                s.add(head)
            head=head.next
        return False
            
        