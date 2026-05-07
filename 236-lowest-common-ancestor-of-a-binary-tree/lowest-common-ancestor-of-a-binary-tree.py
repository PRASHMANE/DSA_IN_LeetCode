# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        
        def dfs(node,p,q):
            if not node:
                return None
            
            if node == p or node == q:
                return node

            lf = dfs(node.left,p,q)
            rf = dfs(node.right,p,q)

            if lf and rf:
                return node
            return lf if lf else rf

            
        return dfs(root,p,q)