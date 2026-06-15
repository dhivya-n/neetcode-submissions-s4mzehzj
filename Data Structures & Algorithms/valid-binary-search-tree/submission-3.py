# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        self.isValid = True
        def returnMinMax(root):
            if root == None:
                return root
            if not self.isValid:
                return None
            leftVal = returnMinMax(root.left)
            rightVal = returnMinMax(root.right)
            currVal = root.val
            minVal, maxVal = None, None
            if leftVal != None:
                if leftVal['minval'] >= currVal or leftVal['maxval']>= currVal:
                    self.isValid = False
                    return None
                else:
                    minVal = leftVal['minval']
            else:
                minVal = root.val

            if rightVal != None:
                if rightVal['minval'] <= currVal or rightVal['maxval']<= currVal:
                    self.isValid = False
                    return None
                else:
                    maxVal = rightVal['maxval']
            else:
                maxVal = root.val
            return {
                'minval': minVal,
                'maxval': maxVal
            }
        returnMinMax(root)
        return self.isValid
        
        