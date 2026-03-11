# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        
        maxi=float('-inf')

        def pathsum(node):
            nonlocal maxi
            if not node:
                return 0
            
            left = max(0,pathsum(node.left))
            right = max(0,pathsum(node.right))

            maxi = max(maxi,right+left+node.val)

            return (node.val) + max(right,left)
        
        pathsum(root)
        return maxi

        