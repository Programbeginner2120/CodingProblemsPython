def abbrev_name(name):
    index = name.find(' ')
    first_init = name[0]
    name = name[index + 1:]
    second_init = name[0]
    return first_init.upper() + '.' + second_init.upper()