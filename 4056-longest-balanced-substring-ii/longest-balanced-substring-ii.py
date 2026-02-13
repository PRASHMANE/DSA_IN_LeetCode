class Solution:
    def longestBalanced(self, s: str) -> int:
        def run_len(s):
            ans = cnt = 0
            prev = ""
            for c in s:
                if c == prev:
                    cnt += 1
                else:
                    prev, cnt = c, 1
                ans = max(ans, cnt)
            return ans

        # Case2: balanced using two characters pairwise
        def two_balanced(s, x, y):
            ans = 0
            diff_pos = {0: -1}
            diff = 0
            for i, c in enumerate(s):
                if c == x:
                    diff += 1
                elif c == y:
                    diff -= 1
                else:
                    diff_pos = {0: i}
                    diff = 0
                    continue
                if diff in diff_pos:
                    ans = max(ans, i - diff_pos[diff])
                else:
                    diff_pos[diff] = i
            return ans

        # Case3: balanced count of a, b, c
        pos = {(0,0): -1}
        cnt = [0, 0, 0]
        ans3 = 0
        for i, c in enumerate(s):
            cnt[ord(c) - 97] += 1
            key = (cnt[0]-cnt[1], cnt[1]-cnt[2])
            if key in pos:
                ans3 = max(ans3, i - pos[key])
            else:
                pos[key] = i

        return max(run_len(s),
                   two_balanced(s, 'a','b'),
                   two_balanced(s, 'b','c'),
                   two_balanced(s, 'a','c'),
                   ans3)