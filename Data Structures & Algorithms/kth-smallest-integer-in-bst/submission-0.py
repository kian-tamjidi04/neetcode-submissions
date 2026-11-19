# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        # Inorder traversal (left -> node -> right)

        stack = [] # Traversed nodes
        curr = root

        while stack or curr:
            # Keep traversing left subtree
            while curr:
                stack.append(curr)
                curr = curr.left

            # Pop next smallest value
            curr = stack.pop()
            k -= 1
            if k == 0:
                return curr.val

            # Move to smallest value's right subtree
            curr = curr.right

