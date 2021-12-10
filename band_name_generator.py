def band_name_generator(name):
    if (name[0].lower() == name[-1]):
        return name[0].upper() + name[1:len(name)] + name[1:]
    return "The " + name[0].upper() + name[1:]