def fractional_knapsack():
    weights = [10, 20, 30]
    values = [60, 100, 120]
    capacity = 50
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
