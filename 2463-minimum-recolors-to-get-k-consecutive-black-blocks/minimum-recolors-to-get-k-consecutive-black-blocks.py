class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:

        count=0
        for i in range(k):
            if blocks[i] == "W":
                count+=1
        
        left=0
        right=k-1
        min_col=count
        n = len(blocks)

        while right < n:
            
            right+=1
            if right < n:
                if blocks[right] == "W":
                    count+=1
            else:
                break

            if blocks[left] == "W":
                count-=1
            left+=1
            

            min_col=min(min_col,count)
        
        return min_col
        
        