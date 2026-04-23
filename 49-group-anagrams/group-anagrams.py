class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        count = defaultdict(list)

        for ch in strs:
            word = "".join(sorted(ch))
            count[word].append(ch)
        
        return list(count.values())