# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        maxT = 0
        def traverseTree(root):
            nonlocal maxT
            if not root:
                return 0
            r = traverseTree(root.right)
            l = traverseTree(root.left)
            maxT = max(maxT, r + l)
            return max(r, l) + 1

        traverseTree(root)
        return maxT