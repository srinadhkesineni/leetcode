# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        def collectLeafNodes(root,arr):
            if not root:
                return
            if not root.left and not root.right:
                arr.append(root.val)
            collectLeafNodes(root.left,arr)
            collectLeafNodes(root.right,arr)
        leafArr1=[]
        leafArr2=[]
        collectLeafNodes(root1,leafArr1)
        collectLeafNodes(root2,leafArr2)
        return leafArr1==leafArr2