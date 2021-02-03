# https://www.codewars.com/kata/5b358a1e228d316283001892/train/python


def get_strings(city):
    city = city.lower()
    city = city.replace(" ", "")
    char_dict = {}
    char_string = f""
    for i in city:
        if i not in char_dict:
            char_dict[i] = '*'
        else:
            char_dict[i] += '*'
    i = 0
    for j in char_dict:
        char_string += f"{j}:{char_dict[j]}"
        if (i < len(char_dict) - 1):
            char_string += ','
        i += 1
    return char_string


print(get_strings("Chicago"))  # "c:**,h:*,i:*,a:*,g:*,o:*"
print(get_strings("Bangkok"))  # "b:*,a:*,n:*,g:*,k:**,o:*"
print(get_strings("Las Vegas"))  # "l:*,a:**,s:**,v:*,e:*,g:*"