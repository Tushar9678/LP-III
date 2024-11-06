def solve_knapsack():
   
    val = list(map(int, input("Enter the values of the items (separated by spaces): ").split()))
    
    wt = list(map(int, input("Enter the weights of the items (separated by spaces): ").split()))
    
    W = int(input("Enter the capacity of the knapsack: "))
    
    if len(val) != len(wt):
        print("Error: The number of values and weights must be the same.")
        return  

    # Number of items
    n = len(val) - 1
    
    # Create a memoization table
    memo = [[-1 for _ in range(W + 1)] for _ in range(n + 1)]

    def knapsack(W, n):
        # Base case
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
    
    # Print the maximum value that can be obtained
    print("Maximum value that can be obtained:", knapsack(W, n))

if __name__ == "__main__":
    solve_knapsack()
