# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head or k == 0:
            return head

        # Calculate the length of the linked list
        length = 1
        tail = head
        while tail.next:
            length += 1
            tail = tail.next

        # Adjust k to avoid unnecessary rotations
        k = k % length
        if k == 0:
            return head

        # Find the new tail and head after rotation
        new_tail = head
        for _ in range(length - k - 1):
            new_tail = new_tail.next

        new_head = new_tail.next
        new_tail.next = None
        tail.next = head

        return new_head
        

