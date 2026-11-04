# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        # Idea - recursively compare the depths of the left and right nodes

        if not root:
            return 0

        rDepth = 1 + self.maxDepth(root.right)
        lDepth = 1 + self.maxDepth(root.left)

        return max(rDepth, lDepth)