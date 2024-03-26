# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        self.list=[]
        def func(node,target):
            if not node:
                return 
            if target-node.val in self.list:
                return True
            self.list.append(node.val)
            x = func(node.left,target) or func(node.right,target)
            return x
            
        return func(root,k)