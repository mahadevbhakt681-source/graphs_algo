class Solution:
    def findCheapestPrice(self, n: int, flights: list[list[int]], src: int, dst: int, k: int) -> int:
        # Distance array initialized to infinity
        prices = [float('inf')] * n
        prices[src] = 0

        # Perform relaxation at most k + 1 times (k stops = k + 1 flights)
        for _ in range(k + 1):
            # Create a copy to prevent using updated prices from the current iteration
            temp_prices = list(prices)
            
            for u, v, w in flights:
                if prices[u] == float('inf'):
                    continue
                if prices[u] + w < temp_prices[v]:
                    temp_prices[v] = prices[u] + w
                    
            prices = temp_prices
            print(prices)

        return prices[dst] if prices[dst] != float('inf') else -1