# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        
        def check(node):
            if node==None:
                return 0
            lt=check(node.left)
            rt=check(node.right)
            if lt==-1 or rt ==-1:
                return -1
            if(abs(lt-rt)>1):
                return -1
            return 1 + max(lt,rt)
        res=check(root)
        if res==-1:
            return False
        return True
        