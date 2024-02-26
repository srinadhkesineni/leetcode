# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        def func(node, A, B):
            if node is None:
                return None
            if node.val == A:
                return node
            if node.val == B:
                return node

            lt = func(node.left, A, B)
            rt = func(node.right, A, B)

            if lt is not None and rt is not None:
                return node
            if lt is not None:
                return lt
            if rt is not None:
                return rt

            return None
        return func(root, p.val, q.val)