class Solution:
    def shortestSubstrings(self, arr: List[str]) -> List[str]:
        freq = defaultdict(int)
        subs = []

        for s in arr:
            seen = set()
            for i in range(len(s)):
                for j in range(i + 1, len(s) + 1):
                    seen.add(s[i:j])
            subs.append(seen)
            for sub in seen:
                freq[sub] += 1

        res = []
        for sset in subs:
            candidates = [sub for sub in sset if freq[sub] == 1]
            if not candidates:
                res.append("")
            else:
                candidates.sort(key=lambda x: (len(x), x))
                res.append(candidates[0])

        return res