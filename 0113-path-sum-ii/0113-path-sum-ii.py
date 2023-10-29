# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        def dfs(node,currSum,path):
            if not node:
                return []
            currSum+=node.val
            path.append(node.val)
            
            if currSum==targetSum and node.left is None and node.right is None:
                return [path.copy()]
                
            leftPaths=dfs(node.left,currSum,path.copy())
            rightPaths=dfs(node.right,currSum,path.copy())
            
            return leftPaths + rightPaths
        
        path=[]
        allPaths=[]
        return dfs(root,0,path)
        