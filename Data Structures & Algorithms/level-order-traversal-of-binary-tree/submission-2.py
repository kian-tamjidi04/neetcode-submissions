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

            # Build sublist level by level
            level = []

            for i in range(qlen):
                # Pop each item on the level and add to sublist
                node = q.popleft()
                if node:
                    level.append(node.val)

                    # Add new nodes to queue
                    q.append(node.left)
                    q.append(node.right)

            # Add list if non-empty
            if level:
                res.append(level)
    
        return res
