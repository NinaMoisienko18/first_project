def format_string(string, length):
    if len(string) >= length:
        return string
    elif len(string) < length:
        count_t = (length - len(string)) // 2
        return f'{" " * count_t}{string}{" " * count_t}'

print(format_string("прив", 15))




# def format_string(string, length):
#     if len(string) >= length:
#         return string
#     elif len(string) < length:
#         count_t = (length - len(string)) // 2
#         return f'{" " * count_t}{string}'
#
# print(format_string("прив", 15))




