# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
#py3
class Solution:

    def maxDepth(self,node):
        if not node:
            return 0

        lh = self.maxDepth(node.left)
        rh = self.maxDepth(node.right)

        return 1 + max(lh,rh)

    def isBalanced(self, root: Optional[TreeNode]) -> bool:

        if not root:
            return True
        
        lh = self.maxDepth(root.left)
        rh = self.maxDepth(root.right)

        if abs(lh-rh) > 1:
            return False
        
        left = self.isBalanced(root.left)
        right = self.isBalanced(root.right)

        if not left or not right:
            return False
        
        return True

       