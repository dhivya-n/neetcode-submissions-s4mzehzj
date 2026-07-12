"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        visited = {}
        def clone(node):
            if node == None:
                return None
            if node in visited:
                return visited[node]
            currNode = Node(node.val)
            visited[node] = currNode
            for neighbours in node.neighbors:
                currNode.neighbors.append(clone(neighbours))
           
            return currNode
        return clone(node)
        