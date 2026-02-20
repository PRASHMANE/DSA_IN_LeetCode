class Solution:
    def maxFreqSum(self, s: str) -> int:

        vowel = "aeiou"
        hsh_vowel={}
        hsh_con={}
        v=0
        c=0

        for i in s:
            if i in vowel:
                hsh_vowel[i] = hsh_vowel.get(i,0)+1
            else:
                hsh_con[i]=hsh_con.get(i,0)+1
        
        if hsh_vowel:
            v=max(list(hsh_vowel.values()))
        if hsh_con:
            c=max(list(hsh_con.values()))

        return v+c

        