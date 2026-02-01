class Solution:
    def largestWordCount(self, messages: List[str], senders: List[str]) -> str:
        hst={}

        for i in range(len(senders)):
            hst[senders[i]] = hst.get(senders[i],0)+len(messages[i].split(" "))
        hst=dict(sorted(hst.items(),key = lambda x:x[1],reverse=True))
        maxi=max(hst.values())
        ans=[]
        for i,j in hst.items():
            if j == maxi:
                ans.append(i)
        return sorted(ans,reverse=True)[0]
