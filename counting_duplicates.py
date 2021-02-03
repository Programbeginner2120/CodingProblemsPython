# https://www.codewars.com/kata/54bf1c2cd5b56cc47f0007a1/train/python


def duplicate_count(text):
    set_of_occurences = set()
    set_of_dupes = set()
    num_dupes = 0
    for char in text:
        char = char.lower()
        if char not in set_of_occurences:
            set_of_occurences.add(char)
        elif char in set_of_occurences:
            if char not in set_of_dupes:
                set_of_dupes.add(char)
                num_dupes += 1
    return num_dupes


print(duplicate_count(""))  # 0
print(duplicate_count("abcde"))  # 0
print(duplicate_count("abcdeaa"))  # 1
print(duplicate_count("abcdeaB"))  # 2
print(duplicate_count("Indivisibilities"))  # 2