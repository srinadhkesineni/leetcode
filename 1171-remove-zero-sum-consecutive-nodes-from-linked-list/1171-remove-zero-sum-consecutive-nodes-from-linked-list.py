# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeZeroSumSublists(self, head: Optional[ListNode]) -> Optional[ListNode]:
        root=ListNode(0,head)
        d={}
        pre_sum=0
        node=root
        while node:
            pre_sum+=node.val
            if pre_sum in d:
                prev=d[pre_sum]
                tmp=prev.next
                tmp_sum=pre_sum
                while tmp != node:
                    tmp_sum+=tmp.val
                    if tmp_sum in d and d[tmp_sum]==tmp:
                        d.pop(tmp_sum)
                    tmp=tmp.next
                prev.next=node.next
                node=prev
            else:
                d[pre_sum]=node
            node=node.next
        return root.next