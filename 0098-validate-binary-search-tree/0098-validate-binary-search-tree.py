# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def func(node, min_val, max_val):
            if node is None:
                return True

            if node.val <= min_val or node.val >= max_val:
                return False

            # For the left subtree, the maximum value is the node's value.
            # For the right subtree, the minimum value is the node's value.
            return (func(node.left, min_val, node.val) and
                    func(node.right, node.val, max_val))

        # For the root, we set the minimum and maximum values as negative and positive infinity respectively.
        return func(root, float('-inf'), float('inf'))