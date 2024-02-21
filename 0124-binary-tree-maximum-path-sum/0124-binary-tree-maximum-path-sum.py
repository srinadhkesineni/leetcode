# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        s=[root.val]
        def func(node):
            if node==None:
                return 0
            ls=max(0,func(node.left))
            rs=max(0,func(node.right))
            s[0]=max(s[0],node.val+ls+rs)
            return (node.val) + max(ls, rs)
        func(root)
        return s[0]