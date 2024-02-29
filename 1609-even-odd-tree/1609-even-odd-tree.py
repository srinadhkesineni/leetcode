# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isEvenOddTree(self, root: Optional[TreeNode]) -> bool:
        queue=[root]
        level=0
        while queue:
            prev_val=None
            for i in range(len(queue)):
                node=queue.pop(0)
                if(level%2==0 and (node.val%2==0 or (prev_val is not None and prev_val>=node.val )))or\
                    (level%2==1 and (node.val%2==1 or (prev_val is not None and prev_val<=node.val)) ):
                    return False
                prev_val=node.val
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            level+=1
        return True
                    
                