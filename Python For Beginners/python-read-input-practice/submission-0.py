def add_two_numbers() -> int:
    text = input()
    string_list = text.split(",")

    sum = 0
    for item in string_list:
        sum += int(item)
    return sum

# do not modify below this line
print(add_two_numbers())
print(add_two_numbers())
print(add_two_numbers())
print(add_two_numbers())
