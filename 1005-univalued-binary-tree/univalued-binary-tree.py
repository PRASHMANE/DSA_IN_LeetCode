# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isUnivalTree(self, root: Optional[TreeNode]) -> bool:

        if not root:
            return True

        val = root.val

        def dfs(node):
            nonlocal val

            if not node:
                return True

            if node.val != val:
                return False
            
            lh = dfs(node.left)
            rh = dfs(node.right)

            if not lh or not rh:
                return False

            return True
        return dfs(root)        