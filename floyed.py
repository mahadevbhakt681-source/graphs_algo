class Solution:
    def findCheapestPrice(self, n: int, flights: list[list[int]], src: int, dst: int, k: int) -> int:
        prices=[float('inf')]*(n+1)
        prices[src]=0
        for _ in range(k+1):
            li=list(prices)
            for u,v,w in flights:
                if prices[u] == float('inf'):
                    continue
                if prices[u] + w < li[v]:
                    li[v] = prices[u] + w
                    
            prices = li
        return prices[dst] if prices[dst]!=float('inf') else -1