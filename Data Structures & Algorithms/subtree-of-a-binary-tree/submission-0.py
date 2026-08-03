# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def sameTree(self, root, subRoot):
        if not root and not subRoot: return True

        if root and subRoot and root.val == subRoot.val:
            return (self.sameTree(root.left, subRoot.left) and self.sameTree(root.right, subRoot.right))

    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not subRoot: return True
        if not root: return False

        if self.sameTree(root, subRoot):
            return True
        return (self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot))








        # if not root and not subRoot: return True

        # def checkSubtree(root, subroot):
        #     if not root and not subroot:
        #         return True

        #     if root and subroot and root.val == subroot.val:
        #         return checkSubtree(root.left, subtree.left) and checkSubtree(root.right, subtree.right)
        #     else:
        #         return False

        # if root and subRoot and root.val == subRoot.val:
        #     # am I assuming there's only 1 possible answer?
        #     return self.checkSubtree(root, subRoot)
        # elif root and subRoot:
        #     return self.isSubtree(root.left, subRoot.left) and self.isSubtree(root.right, subRoot.right)
        # else:
        #     return False

        


        