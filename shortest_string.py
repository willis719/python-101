def shortest(str_list):
    return [str for str in str_list if len(str) < len(str)]

print(shortest(["hello", "bye", "hi", "deuces"]))
