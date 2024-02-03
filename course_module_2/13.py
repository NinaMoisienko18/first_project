def factorial(n):
    if n < 2:
        return 1
    else:
        return n * factorial(n - 1)

def number_of_groups(n, k):
    return factorial(n) / (factorial(n - k) * factorial(k))

n = 50
k = 7
print(f"Total count of lists: {factorial(n)}")
print(f"Count of ways: {number_of_groups(n, k)}")

