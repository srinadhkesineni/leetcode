# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if not preorder or not inorder:
            return None
        inorderMap = {}
        for i in range(len(inorder)):
            inorderMap[inorder[i]] = i
        def helper(l, r):
            if l > r:
                return None
            root = TreeNode(preorder.pop(0))
            mid = inorderMap[root.val]
            root.left = helper(l, mid - 1)
            root.right = helper(mid + 1, r)
            return root
        root = helper(0, len(inorder) - 1)
        return root