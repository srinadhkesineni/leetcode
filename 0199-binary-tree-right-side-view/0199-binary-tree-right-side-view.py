# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []       
        li=[]
        self.max_height=0
        li.append(root.val)
        def func(node,pre,l):
            if not node:
                self.max_height=max(pre-1,self.max_height)
                return 
            if pre > self.max_height:
                l.append(node.val)
            func(node.right,pre+1,l)
            func(node.left,pre+1,l)
            return    
        func(root,0,li)
        return li