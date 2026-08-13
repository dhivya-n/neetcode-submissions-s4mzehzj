from typing import List


class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adl = [[] for i in range(numCourses)]
        indegree = [0 for i in range(numCourses)]
        for requirement in prerequisites:
            adl[requirement[0]].append(requirement[1])
            indegree[requirement[1]]+=1
        queue = []
        for i in range(numCourses):
            if indegree[i] == 0:
                queue.append(i)
        finished = 0
        while len(queue) != 0:
            element = queue.pop()
            finished+=1
            for preReq in adl[element]:
                indegree[preReq]-=1
                if indegree[preReq] == 0:
                    queue.append(preReq)
        if finished == numCourses:
            return True
        else:
            return False
