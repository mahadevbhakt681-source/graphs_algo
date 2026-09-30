class Solution:
    def networkDelayTime(self, times: list[list[int]], n: int, k: int) -> int:
        cost=[float('inf')]*(n+1)
        cost[k]=0
        for i in range(n):
            copy=list(cost)
            updated=False
            for u,v,w in times:
                if cost[u]==float('inf'):
                    continue
                if cost[u]+w<copy[v]:
                    copy[v]=cost[u]+w
                    updated=True
            cost=list(copy)
            if not updated:
                break
        max_time = 0
        for i in cost[1:]:
            if i == float('inf'):
                return -1
            max_time = max(max_time, i)
            
        return max_time

        