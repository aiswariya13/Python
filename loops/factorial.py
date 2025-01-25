num = input("Enter a non-negative integer to calculate its factorial: ")

if num.isdigit():
    num = int(num)
    if num < 0:
        print("Factorial is not defined for negative numbers.")
    else:
        factorial = 1
        for i in range(1, num + 1):
            factorial *= i
        print(f"The factorial of {num} is {factorial}.")
else:
    print("Please enter a valid non-negative integer.")
