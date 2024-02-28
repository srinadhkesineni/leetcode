class Solution:
    def findBottomLeftValue(self, root: Optional[TreeNode]) -> int:
        self.max_idx=[root.val,0]
        def func(node,idx):
            if not node:
                return
            lt=func(node.left,idx+1)
            if self.max_idx[1]<idx:
                self.max_idx[1],self.max_idx[0]=idx,node.val
            rt=func(node.right,idx+1)
            return
        func(root,0)
        return self.max_idx[0]