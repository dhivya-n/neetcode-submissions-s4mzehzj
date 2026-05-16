# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root == None:
            return []
        q = [root]
        result = []
        while len(q) != 0:
            temp = []
            curr = []
            for i in range(len(q)):
                curr.append(q[i].val)
                if q[i].left != None:
                    temp.append(q[i].left)
                if q[i].right != None:
                    temp.append(q[i].right)
            result.append(curr)
            q = temp
        return result

                
            

    
        