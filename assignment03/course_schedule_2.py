from typing import List
import collections


class Solution:
    def findOrder(self, numCourses: int,
                  prerequisites: List[List[int]]
                  ) -> List[int]:
        indeg = [0] * numCourses
        to = [[] for _ in range(numCourses)]
        for p in prerequisites:
            to[p[1]].append(p[0])
            indeg[p[0]] += 1
        q = collections.deque([u for u in range(numCourses) if indeg[u] == 0])
        # visited = 0
        result = []
        while q:
            # visited += 1
            u = q.popleft()
            result.append(u)
            for v in to[u]:
                indeg[v] -= 1
                if indeg[v] == 0:
                    q.append(v)
        return result if len(result) == numCourses else []
