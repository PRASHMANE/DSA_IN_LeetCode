# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []

        left_to_right = True

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
                

            if not left_to_right:
               res.append(level[::-1])
               left_to_right = True
            else:
                res.append(level)
                left_to_right = False
        
        return res