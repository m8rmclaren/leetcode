from collections import deque
from typing import List

class Solution:

    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:

        adj = [[] for _ in range(numCourses)]
        in_degree = [0 for _ in range(numCourses)]

        # build adjacency list
        for edge in prerequisites:
            adj[edge[0]].append(edge[1])
            in_degree[edge[1]] += 1
        
        q = deque()

        # Add all vertices with in-deg 0 to our queue
        for i in range(numCourses):
            if in_degree[i] > 0:
                q.append(i)

        # Keep track of the topo order
        topo_order = []

        # Run BFS while there vertices with in-deg 0
        while len(q) > 0:
            v = q.pop()
            # add this vertex to the topo order
            topo_order.append(v)

            # For each neighbor of v, decrement its in-deg
            for neighbor in adj[v]:
                in_degree[neighbor] -= 1
                if in_degree[neighbor] == 0:
                    q.append(neighbor)

        # If the length of the topo order is less than the number of courses,
        # then we have a cycle in our graph
        print(f"topo_order: {topo_order}")
        if len(topo_order) == numCourses:
            return True
        else:
            return False
        
s = Solution()

print(s.canFinish(2, [[1,0]]))
