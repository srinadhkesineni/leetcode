# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        count=0
        if not root:
            return 0
        def func( node):
            if not node:
                return 0
            nonlocal count
            count+=1
            func( node.left)
            func( node.right)
        func(root)
        return count 