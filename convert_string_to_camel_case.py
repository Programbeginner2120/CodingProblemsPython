def to_camel_case(text):
    text = text.replace("_", " ")
    text = text.replace("-", " ")
    text = text.split(" ")
    arr = []
    arr.append(text[0])
    for word in text[1:]:
        word = word.replace(word[0], word[0].upper(), 1)
        arr.append(word)
    return "".join(arr)