def fractional_knapsack():
    # Get user input for characters and their frequencies
    n = int(input("Enter the number of items: "))
    weights = []
    values = []
    
    # Input weights
    print("Enter the weights of the items:")
    for i in range(n):
        weight = int(input(f"Weight of item {i+1}: "))
        weights.append(weight)

    # Input values
    print("Enter the values of the items:")
    for i in range(n):
        value = int(input(f"Value of item {i+1}: "))
        values.append(value)

    # Input capacity of the knapsack
    capacity = int(input("Enter the capacity of the knapsack: "))
    total_value = 0

    # Pair each item as (weight, value) and sort by value-to-weight ratio in descending order
    items = sorted(zip(weights, values), key=lambda x: x[1] / x[0], reverse=True)

    for weight, value in items:
        if capacity <= 0:  # Knapsack is full
            break
        if weight > capacity:  # Take fraction of the item
            total_value += capacity * (value / weight)
            capacity = 0  # Knapsack is now full
        else:  # Take the entire item
            total_value += value
            capacity -= weight

    print(f"Maximum value that can be obtained: {total_value}")

if __name__ == "__main__":
    fractional_knapsack()
