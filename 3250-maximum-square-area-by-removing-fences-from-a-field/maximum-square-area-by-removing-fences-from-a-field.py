class Solution:
    def maximizeSquareArea(self, m: int, n: int, hFences: List[int], vFences: List[int]) -> int:

        h=self.get_edge(hFences,m)
        v=self.get_edge(vFences,n)

        max_size=-1
        for i in h:
            if i in v:
                max_size=max(max_size,i)

        if max_size == -1:
            return -1
        return (max_size * max_size) % (10 ** 9 + 7)
        
    def get_edge(self,f,limit):
        f=[1]+f+[limit]
        f.sort()

        s=set()
        n = len(f)
        for i in range(n):
            for j in range(i+1,n):
                s.add(f[j]-f[i])
        return s
