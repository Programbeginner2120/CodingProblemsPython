#


def get_consective_items(items, key):
    num_consec = 0
    highest_iteration = 0
    items = str(items)
    for ch in items:
        if ch == str(key):
            num_consec += 1
            highest_iteration = max(num_consec, highest_iteration)
        else:
            num_consec = 0
    return highest_iteration


print(get_consective_items(90000, 0))  # 4
print(get_consective_items('ascasdaiiiasdacasdiiiiicasdasdiiiiiiiiiiisdasdasdiii', 'i'))  # 11