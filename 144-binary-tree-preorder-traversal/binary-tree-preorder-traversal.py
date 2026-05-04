# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        self.pre(root,res)
        return res

    def pre(self,node,res):
        if not node:
            return
        
        res.append(node.val)
        self.pre(node.left,res)
        self.pre(node.right,res)
    