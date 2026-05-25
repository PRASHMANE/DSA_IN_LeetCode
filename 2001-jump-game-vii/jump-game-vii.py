class Solution:
    def canReach(self, s: str, minJump: int, maxJump: int) -> bool:
        n  = len(s)
        queue = deque([0])
        farthers = 0

        while queue:
            i = queue.popleft()
            if i == n-1:
                return True
            for j in range(max(i+minJump,farthers+1),min(i+maxJump+1,n)):
                if s[j] == '0':
                    queue.append(j)
            farthers = max(farthers,i+maxJump)

        return False