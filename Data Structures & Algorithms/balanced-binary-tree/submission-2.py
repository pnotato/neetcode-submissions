# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True

        def traverseTree(root):
            if not root:
                return 0

            return max(traverseTree(root.left), traverseTree(root.right)) + 1

        if abs(traverseTree(root.left) - traverseTree(root.right)) > 1:
            return False

        return self.isBalanced(root.left) and self.isBalanced(root.right)

        