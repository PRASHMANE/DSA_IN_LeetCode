class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n = len(isConnected)
        vis = [False]*n
        count=0
        def dfs(node):
            vis[node] = True

            for neig in range(n):
                if isConnected[node][neig] == 1 and not vis[neig]:
                    dfs(neig)
            

        for i in range(n):
            if vis[i] == 0:
                count+=1
                dfs(i)
        return count