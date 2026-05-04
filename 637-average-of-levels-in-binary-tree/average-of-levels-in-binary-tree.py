# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:

        if not root:
            return []

        que = deque([root])
        res = []

        while que:
            level = []
            size = len(que)

            for _ in range(size):
                node = que.popleft()

                level.append(node.val)

                if node.left:
                    que.append(node.left)
                
                if node.right:
                    que.append(node.right)
            avg = sum(level) / size
            res.append(avg)
        return res
        