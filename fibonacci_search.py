def fibonacci_search(arr, x):
    n = len(arr)

    # Initialize Fibonacci numbers
    fib2 = 0
    fib1 = 1
    fib = fib1 + fib2

    # Find the smallest Fibonacci number >= n
    while fib < n:
        fib2 = fib1
        fib1 = fib
        fib = fib1 + fib2

    offset = -1

    # Search
    while fib > 1:

        i = min(offset + fib2, n - 1)

        if arr[i] < x:
            fib = fib1
            fib1 = fib2
            fib2 = fib - fib1
            offset = i

        elif arr[i] > x:
            fib = fib2
            fib1 = fib1 - fib2
            fib2 = fib - fib1

        else:
            return i

    # Check the last remaining element
    if fib1 and offset + 1 < n and arr[offset + 1] == x:
        return offset + 1

    return -1


# arr = [10, 20, 30, 40, 50, 60, 70, 80]
arr = list(map(int, input().split()))
target = int(input("Enter target value "))
result = fibonacci_search(arr, target)

print("Element found at index:", result)