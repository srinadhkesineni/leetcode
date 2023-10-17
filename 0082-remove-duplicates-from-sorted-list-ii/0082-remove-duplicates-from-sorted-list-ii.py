# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        d={}
        current=head
        while current is not None:
            if current.val in d:
                d[current.val]+=1
            else:
                d[current.val]=1
            current=current.next
        current=head
        prev=None
        # while current is not None:
        #     if d[current.val]>1:
        #         if prev:
        #             prev.next=current.next
        #     else:
        #         prev=current
        #     current=current.next
        new_head = None
        new_current = None
        current = head
        
        while current is not None:
            if d[current.val] == 1:
                if new_head is None:
                    new_head = ListNode(current.val)
                    new_current = new_head
                else:
                    new_current.next = ListNode(current.val)
                    new_current = new_current.next
            current = current.next

        return new_head









        