# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:

        

        node1 = []

        def dfs(node,col,row):
            if not node:
                return
            
            node1.append((col,row,node.val))

            dfs(node.left,col-1,row+1)
            dfs(node.right,col+1,row+1)
        
        dfs(root,0,0)

        node1.sort()

        res = defaultdict(list)

        for col,row,val in node1:
            res[col].append(val)
        
        return [res[x] for x in sorted(res)]


