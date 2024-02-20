# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        
        def check(node, mx):
            if node is None:
                return 0, mx  # Return both the depth and the updated mx
            lt, mx = check(node.left, mx)
            rt, mx = check(node.right, mx)
            mx = max(mx, lt + rt)
            return 1 + max(lt, rt), mx  # Return depth and updated mx

        _, result = check(root, 0)
        return result
        