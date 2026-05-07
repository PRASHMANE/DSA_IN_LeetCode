# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getDirections(self, root: Optional[TreeNode], startValue: int, destValue: int) -> str:
        # ---------- FIND LCA ----------
        def findLCA(node):

            if not node:
                return None

            if node.val == startValue or node.val == destValue:
                return node

            left = findLCA(node.left)
            right = findLCA(node.right)

            if left and right:
                return node

            return left if left else right

        lca = findLCA(root)

        # ---------- FIND PATH ----------
        def dfs(node, target, path):

            if not node:
                return False

            if node.val == target:
                return True

            path.append("L")

            if dfs(node.left, target, path):
                return True

            path.pop()

            path.append("R")

            if dfs(node.right, target, path):
                return True

            path.pop()

            return False

        pathToStart = []
        pathToDest = []

        dfs(lca, startValue, pathToStart)
        dfs(lca, destValue, pathToDest)

        return "U" * len(pathToStart) + "".join(pathToDest)