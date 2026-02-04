class Solution:
    def findWords(self, words: List[str]) -> List[str]:

        row = {}
        for ch in "qwertyuiop":
            row[ch] = 1
        for ch in "asdfghjkl":
            row[ch] = 2
        for ch in "zxcvbnm":
            row[ch] = 3

        res = []
        for word in words:
            w = word.lower()
            if all(row[ch] == row[w[0]] for ch in w):
                res.append(word)
        return res