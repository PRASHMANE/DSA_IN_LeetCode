# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:

        hsh = {}

        def dfs(node,col,row):
            if not node:
                return
            
            hsh[row] = node.val

            dfs(node.left,col-1,row+1)
            dfs(node.right,col+1,row+1)

        dfs(root,0,0)

        hsh = dict(sorted(hsh.items()))

        return [hsh[x] for x in hsh]
        