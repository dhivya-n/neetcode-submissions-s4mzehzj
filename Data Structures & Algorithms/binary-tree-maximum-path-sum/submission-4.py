class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.currMax = -float("inf")
        self.checkPathSum(root)
        return self.currMax
    
    def checkPathSum(self, root: Optional[TreeNode]) -> int:
        if root == None:
            return None
        result = root.val
        maxLeft = self.checkPathSum(root.left)
        select =  -99999
        if maxLeft:
            result+=maxLeft
            self.currMax = max(self.currMax, maxLeft)
            select = max(select, maxLeft)
        maxRight = self.checkPathSum(root.right)
        if maxRight:
            result+=maxRight
            self.currMax = max(self.currMax, maxRight)
            select = max(select, maxRight)
        self.currMax = max(self.currMax, result, root.val) 
        if select > 0 :
            self.currMax = max(self.currMax, select + root.val) 
            return select + root.val
        return root.val