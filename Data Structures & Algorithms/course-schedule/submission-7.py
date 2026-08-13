from typing import List


class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adl = [[] for i in range(numCourses)]
        for requirement in prerequisites:
            adl[requirement[0]].append(requirement[1])

        completedCourse = []
        def dfs(index, visited):
            if index in visited:
                return False
            if index in completedCourse:
                return True
            for course in adl[index]:
                newVisited = set(visited)
                newVisited.add(index)
                if dfs(course, newVisited) is False:
                    return False
            completedCourse.append(index)
            return True
        

        for requirement in prerequisites:
            if requirement[0] in completedCourse:
                continue
            visited = set()
            if dfs(requirement[0], visited) is False:
                return False
        return True
