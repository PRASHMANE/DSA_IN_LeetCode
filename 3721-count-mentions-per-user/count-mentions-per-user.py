from typing import List

class Solution:
    def countMentions(self, numberOfUsers: int, events: List[List[str]]) -> List[int]:
        # Prepare containers
        online = [True] * numberOfUsers
        reOnlineTime = [0] * numberOfUsers  # time when user will automatically be online again
        mentions = [0] * numberOfUsers

        # Parse events and group them by timestamp preserving input order
        events_by_time = {}
        for ev in events:
            typ, t_str, info = ev
            t = int(t_str)
            events_by_time.setdefault(t, []).append((typ, info))

        # Process timestamps in ascending order
        for t in sorted(events_by_time.keys()):
            # 1) First: bring back users who have their reOnlineTime <= t
            for u in range(numberOfUsers):
                if not online[u] and reOnlineTime[u] <= t:
                    online[u] = True

            # 2) Then: apply all OFFLINE events at this timestamp (in input order)
            for typ, info in events_by_time[t]:
                if typ == "OFFLINE":
                    user = int(info)
                    online[user] = False
                    reOnlineTime[user] = t + 60

            # 3) Finally: process all MESSAGE events at this timestamp (in input order)
            for typ, info in events_by_time[t]:
                if typ != "MESSAGE":
                    continue
                tokens = info.split()

                if "ALL" in tokens:
                    for u in range(numberOfUsers):
                        mentions[u] += 1
                    continue

                if "HERE" in tokens:
                    for u in range(numberOfUsers):
                        if online[u]:
                            mentions[u] += 1
                    continue

                # id<number> tokens (duplicates count)
                for token in tokens:
                    if token.startswith("id"):
                        idx = int(token[2:])
                        mentions[idx] += 1

        return mentions
