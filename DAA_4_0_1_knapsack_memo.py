def solve_knapsack():
    val = [50, 100, 150, 200]  # value array
    wt = [8, 16, 32, 40]  # Weight array
    W = 64
    n = len(val) - 1

    # Create a memoization table
    memo = [[-1 for _ in range(W + 1)] for _ in range(n + 1)]

    def knapsack(W, n):
        # base case
        if n < 0 or W <= 0:
            return 0
        
        # Check if the value is already calculated
        if memo[n][W] != -1:
            return memo[n][W]
        
        # If the weight of the current item is more than remaining capacity
        if wt[n] > W:
            memo[n][W] = knapsack(W, n - 1)
        else:
            # Take the max of including or excluding the item
            memo[n][W] = max(val[n] + knapsack(W - wt[n], n - 1), knapsack(W, n - 1))
        
        return memo[n][W]
    
    print(knapsack(W, n))

if __name__ == "__main__":
    solve_knapsack()
