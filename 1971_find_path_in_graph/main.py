from collections import deque

class Solution:
    def edges_to_adj_list(self, vertices, edges) -> list[list[int]]:
        adj = [[] for _ in range(vertices)]

        for edge_pair in edges:
            adj[edge_pair[0]].append(edge_pair[1])
            adj[edge_pair[1]].append(edge_pair[0])
        
        return adj

    def validPath(self, n, edges, source, destination) -> bool:
        # Edge case: if the source is the same as the destination, there's a path
        if source == destination:
            return True

        adj = self.edges_to_adj_list(n, edges)

        # Keep track of the vertices that we've visited
        visited = set()
        # We can call visited.add(any)

        # Use a deque as our queue -> We'll use the BFS algo
        # Deque is O(1) for pop operations
        q = deque()
        
        # We can start from the node that the problem gave us:
        q.append(source)

        # Perform BFS
        while len(q) > 0:
            this = q.pop()
            if this not in visited:
                # Immediately mark the vertex as visited
                visited.add(this)

                for adjacent_vertex in adj[this]:
                    q.append(adjacent_vertex)

                    # We can early return right here if the 
                    # destination is reachable from this node
                    if adjacent_vertex == destination:
                        return True

        return False

s = Solution()

print(s.validPath(6, [[0,1],[0,2],[3,5],[5,4],[4,3]], 0, 5))

        
