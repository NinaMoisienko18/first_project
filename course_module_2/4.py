num = int(input("Enter the integer (0 to 100): "))
sum = 0
numbers = []

while num != 0:
    numbers.append(num)
    num = num - 1

for i in numbers:
    sum += i

print(sum)