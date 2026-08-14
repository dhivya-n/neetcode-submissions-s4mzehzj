from typing import List


class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        adl = {i:[] for i in range(n)}
        for edge in edges:
            edge.sort()
            adl[edge[0]].append(edge[1])
            adl[edge[1]].append(edge[0])
        visited = set()
        queue = []
        queue.append([0, 0])
        while len(queue) != 0:
            [ele, prev] = queue.pop()
            if ele in visited:
                return False
            visited.add(ele)
            for edges in adl[ele]:
                if edges != prev:
                    queue.append([edges, ele])
        return n == len(visited)
