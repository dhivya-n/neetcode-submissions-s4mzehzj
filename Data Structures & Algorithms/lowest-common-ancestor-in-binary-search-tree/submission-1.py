# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        self.lcs = None
        def findLcs(root):
            if self.lcs != None:
                return True
            if root == None:
                return False
            left = findLcs(root.left)
            right = findLcs(root.right)
            if root.val == q.val or root.val == p.val:
                if left or right and self.lcs == None:
                     self.lcs = root
                return True

            if left and right and self.lcs == None:
                self.lcs = root
            return left or right
        findLcs(root)
        return self.lcs

        