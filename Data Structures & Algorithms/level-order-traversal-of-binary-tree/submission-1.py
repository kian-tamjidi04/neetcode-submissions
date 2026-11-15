# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        # Need to implement a BFS
        # Go layer by layer
        # When we go down a layer, add the previous layer to the output list
        res = []

        q = collections.deque()
        q.append(root)

        while q:
            qlen = len(q)
            level = []

            for i in range(qlen):
                node = q.popleft()
                if node:
                    level.append(node.val)
                    q.append(node.left)
                    q.append(node.right)
            if level:
                res.append(level)
    
        return res
