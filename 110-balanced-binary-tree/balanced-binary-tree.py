# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
#py3
class Solution:

    def find_high(self,root_1):
        if not root_1:
            return 0
        
        lh = self.find_high(root_1.left)
        rh = self.find_high(root_1.right)

        return 1+max(lh,rh)

    def isBalanced(self, root: Optional[TreeNode]) -> bool:

        if not root:
            return True
        
        lh = self.find_high(root.left)
        rh = self.find_high(root.right)

        if abs(lh-rh) > 1 :
            return False
        
        left = self.isBalanced(root.left)
        right = self.isBalanced(root.right)

        if not left or not right:
            return False
        
        return True
        