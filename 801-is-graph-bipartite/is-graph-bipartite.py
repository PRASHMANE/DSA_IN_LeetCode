class Solution:
    def isBipartite(self, graph: list[list[int]]) -> bool:
        v = len(graph)
        colour = [-1]*v

        def dfs(node):
            for neig in graph[node]:
                if colour[neig] == -1:
                    colour[neig] = 1 - colour[node]
                    if not dfs(neig):
                        return False
                elif colour[neig] == colour[node]:
                    return False
            return True
        for i in range(v):
            if colour[i] == -1:
                colour[i] = 0
                if not dfs(i):
                    return False
        return True