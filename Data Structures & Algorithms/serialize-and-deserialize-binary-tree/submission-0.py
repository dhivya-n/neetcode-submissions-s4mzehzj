# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        res = ''
        def convertToString(root):
            nonlocal res
            if root == None:
                res+=',N'
                return 
            res+=','
            res+=str(root.val)
            convertToString(root.left)
            convertToString(root.right)
            return
        convertToString(root)
        print(res)
        return res
                

        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        input = data.split(',')
        i = 0
        def construct():
            nonlocal i, input
            i+=1
            if input[i] == 'N':
                return None
            node = TreeNode(int(input[i]))
            left = construct()
            right = construct()
            node.left = left
            node.right = right
            return node
        return construct()

