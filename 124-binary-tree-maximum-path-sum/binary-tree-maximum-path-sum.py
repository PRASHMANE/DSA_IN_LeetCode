# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        
        maxi = float('-inf')

        def find_sum(node):
            nonlocal maxi

            if not node:
                return 0

            ls = max(0,find_sum(node.left))
            rs = max(0,find_sum(node.right))

            maxi = max(maxi,ls+rs+node.val)

            return node.val + max(rs,ls)


        find_sum(root)
        return maxi