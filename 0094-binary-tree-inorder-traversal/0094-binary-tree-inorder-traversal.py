# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res=[]
        if root is None:
            return None
        if root is not None:
            la=self.inorderTraversal(root.left)
            if la:
                for i in la:
                    res.append(i)
            
            res.append(root.val)
                    
            ra=self.inorderTraversal(root.right)
            if ra:
                for i in ra:
                    res.append(i)
                    
        return res
                    
        