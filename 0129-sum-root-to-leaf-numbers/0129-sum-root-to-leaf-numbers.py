# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        #Regular DFS solution
        res = 0
        def dfs(root, path):
            nonlocal res
            path += str(root.val)
            if root.left is None and root.right is None:
                res += int(path)
                return
            if root.left is not None:
                dfs(root.left, path)
            if root.right is not None:
                dfs(root.right, path)
            return
        path = ''
        dfs(root, path)
        return res