def recursive_fibonacci(n):
    if n <= 1:
        return n
    else:
        return recursive_fibonacci(n - 1) + recursive_fibonacci(n - 2)

def non_recursive_fibonacci(n):
    first = 0
    second = 1
    print(first)
    print(second)
    while n - 2 > 0:
        third = first + second
        first = second
        second = third
        print(third)
        n -= 1

if __name__ == "__main__":
    # User input for n
    n = int(input("Enter the number of terms in the Fibonacci sequence: "))
    
    print("\nThis series is generated by recursive Fibonacci")
    for i in range(n):
        print(recursive_fibonacci(i))
    
    print("\nThis series is generated by non-recursive Fibonacci")
    non_recursive_fibonacci(n)