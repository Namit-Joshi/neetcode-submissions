from typing import List

def read_integers() -> List[int]:
    text = input()
    string_list = text.split(",")

    for i, ch in enumerate(string_list):
        string_list[i] = int(ch)

    return string_list
# do not modify the code below
print(read_integers())
print(read_integers())
print(read_integers())
