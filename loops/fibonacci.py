n = input("Enter the number of terms for Fibonacci series: ")

if n.isdigit():
    n = int(n)
    if n <= 0:
        print("Please enter a positive integer.")
    else:
        fib_series = []
        a, b = 0, 1
        for _ in range(n):
            fib_series.append(a)
            a, b = b, a + b
        print("Fibonacci series up to", n, "terms:", fib_series)
else:
    print("Please enter a valid integer.")
