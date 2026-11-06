# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        # Empty tree is always a subtree
        if not subRoot:
            return True
        if not root:
            return False
        
        # Determine if the subtree is the same tree as what is described from the current root node
        if self.sameTree(root, subRoot):
            return True
        
        # If subtree not the same tree as the current root node, compare the left and right of the main tree
        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)
        
    def sameTree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not root and not subRoot:
            return True
        
        # Check left and right children for equality
        if root and subRoot and root.val == subRoot.val:
            return self.sameTree(root.left, subRoot.left) and self.sameTree(root.right, subRoot.right)
        
        # If (1) only 1 is null or (2) values differ
        return False
