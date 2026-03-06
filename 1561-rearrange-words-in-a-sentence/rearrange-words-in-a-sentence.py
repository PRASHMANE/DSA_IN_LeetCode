class Solution:
    def arrangeWords(self, text: str) -> str:
        hsh = defaultdict(list)
        for ch in text.split(" "):
            hsh[len(ch)].append(ch)

        hsh=dict(sorted(hsh.items() , key = lambda x:x[0]))

        
        ans=[]

        for i in hsh:
            ans+=hsh[i]

        for i in range(len(ans)):
            ans[i]=ans[i].lower()
        
        ans[0]=ans[0].capitalize()
        
        return " ".join(ans)
