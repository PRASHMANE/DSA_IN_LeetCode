# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:

        if not root:
            return []

        res = []
        que = deque([root])

        while que:
            level = []
            size =len(que)

            for _ in range(size):

                node = que.popleft()

                level.append(node.val)

                if node.left:
                    que.append(node.left)
                
                if node.right:
                    que.append(node.right)
            res.append(level)
        
        return res
        