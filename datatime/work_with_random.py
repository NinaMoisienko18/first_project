import random

names = ["Nina", "Denis", "Bogdan", "Sophia", "Eva"]
count = len(names)

# Генеруємо унікальні числа для кожного імені
unique_numbers = random.sample(range(1, count + 1), count)
print(unique_numbers)

# Виводимо пари чисел та імена
for i, name in zip(unique_numbers, names):
    print(i, name)