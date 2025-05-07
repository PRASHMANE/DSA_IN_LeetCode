from numpy import array,concatenate as concat
class Solution:
    def specialGrid(self, n: int) -> List[List[int]]:

        def dfs(n:int,incr:int)-> array:

            if n==0:
                return array([[0]])
            n-=1
            incr//=4

            upRight=dfs(n,incr)
            dnRight=upRight+incr
            dnLeft=dnRight+incr
            upLeft=dnLeft+incr

            return concat((concat((upLeft,upRight),axis=1),
            concat((dnLeft,dnRight),axis=1)))

        return dfs(n,1 << (2*n)).tolist()