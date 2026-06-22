class Solution:
    
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        currMax = -float("inf")
    
        def checkPathSum(root: Optional[TreeNode]) -> int:
            nonlocal currMax
            if root == None:
                return 0

            maxLeft = checkPathSum(root.left)
            maxRight = checkPathSum(root.right)
            maxLeft = max(maxLeft, 0)
            maxRight = max(maxRight, 0)

            currMax = max(currMax, root.val+maxLeft+maxRight)

            return root.val + max(maxLeft, maxRight) #Return selecting only one path
        
        checkPathSum(root)
        return currMax