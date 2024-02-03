
# def get_fullname(first_name, last_name, middle_name=" "):
#     if middle_name:
#         full_name = f"{first_name} {last_name} {middle_name} "
#     else:
#         full_name = f"{first_name} {last_name}"
#     return full_name
#
# person_info = input("Enter your first_name, last_name, also you can write your middle name (not a requirement): ")
# first_name, last_name, *middle_name = person_info.split()
#
# full_name = get_fullname(first_name, last_name, middle_name[0] if middle_name else " ")
#
# print(full_name)



def get_fullname(first_name, last_name, *middle_name):
    if middle_name:
        full_name = f"{first_name} {middle_name[0]} {last_name}"
        return full_name
    else:
        middle_name = " " #?
        full_name = f"{first_name} {last_name}"
        return full_name

first_name = "Nina"
last_name = "Moisienko"
middle_name = input()

full_name = get_fullname(first_name, last_name, middle_name)

print(full_name)

