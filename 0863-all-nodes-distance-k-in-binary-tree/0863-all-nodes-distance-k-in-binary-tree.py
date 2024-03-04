# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        def helper(node,parent):
            if not node:
                return 
            node.parent=parent
            helper(node.left,node)
            helper(node.right,node)
        ans=[]
        seen=set()
        helper(root,None)
        def dfs(node,dist):
            if not node or node in seen or dist>k:
                return 
            seen.add(node)
            if dist==k:
                ans.append(node.val)
            dfs(node.parent,dist+1)
            dfs(node.left,dist+1)
            dfs(node.right,dist+1)
        dfs(target,0)
        return ans
        