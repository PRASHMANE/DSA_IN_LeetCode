class Solution:
    def eventualSafeNodes(self, graph: list[list[int]]) -> list[int]:
        v = len(graph)
        visited = [False] * v
        path_vis = [False] * v

        def dfs(node):
            visited[node] = True
            path_vis[node] = True
            for neig in graph[node]:
                if not visited[neig]:
                    if not dfs(neig):
                        return False
                elif path_vis[neig]:
                    return False
            path_vis[node] = False
            return True
        ans = []
        for i in range(v):
            if not visited[i]:
                if dfs(i):
                    ans.append(i)
            elif not path_vis[i]:
                ans.append(i)
        return ans
                
        