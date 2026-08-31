# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        # case where there is no subroot
        if not root and not subRoot:
            return True

        if not root and subRoot:
            return False

        # should be the same as the previous problem.
        def isMatch(p, q) -> bool:
            if not p and not q:
                return True

            if p and q and p.val == q.val:
                return isMatch(p.left, q.left) and isMatch(p.right, q.right)
            else:
                return False
            
        if isMatch(root, subRoot):
            return True
        
        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)
            


