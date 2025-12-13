class Solution(object):
    def validateCoupons(self, code, businessLine, isActive):
        groups = {
            "electronics": [],
            "grocery": [],
            "pharmacy": [],
            "restaurant": []
        }

        for c, b, a in zip(code, businessLine, isActive):
            if (
                a
                and b in groups
                and c
                and all(ch.isalnum() or ch == '_' for ch in c)
            ):
                groups[b].append(c)

        return (
            sorted(groups["electronics"]) +
            sorted(groups["grocery"]) +
            sorted(groups["pharmacy"]) +
            sorted(groups["restaurant"])
        )
