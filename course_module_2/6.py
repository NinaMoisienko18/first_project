pool = 1000
quantity = int(input("Enter the number of mailings: "))
try:
    chunk = pool / quantity
    chunk = round(chunk, 0)
    print(f"Size of SMS package: {int(chunk)}")

except ZeroDivisionError:
    print('Divide by zero completed!')

