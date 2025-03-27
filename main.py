from math import pi


def factorial(x):

    if x == 0 or x == 1:
        return 1
    else:
        return x * factorial(x - 1)


def sine_x(x_deg, n):

    x = pi * x_deg  / 180  
    last = 0
    factorialTerm = lambda i: ((-1)**i) * (x**(2*i + 1)) / factorial(2*i + 1)

    for i in range(n + 1):
        last += factorialTerm(i)

    return last

totalSum = 0

def recursive_sum(n):
    
    global totalSum
    if n == 0:
        return
    totalSum += n
    recursive_sum(n - 1)

print("question 1")
x = 5
print(f"{x}! = {factorial(x)}")

print("\nquestion 2")
x_deg = 30
n = 5
print(f"sin({x_deg}) = {sine_x(x_deg, n)}")

print("\nquestion 3")
n = 10
totalSum = 0  # Reset global variable
recursive_sum(n)
print(f"Toplam {n}'e kadar: {totalSum}")
