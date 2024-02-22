# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        queue=[root]
        l=[]
        while queue:
            present=[]
            for i in range(len(queue)):
                p=queue.pop(0)
                present.append(p.val)
                if p.left:
                    queue.append(p.left)
                if p.right:
                    queue.append(p.right)
            if len(l)%2==0:
                l.append(present)
            else:
                l.append(present[::-1])
        return l