def palindrome(str):
    if str == str[::-1]:
        return print(True)
    else:
        return print(False)

str = input("Give me a word: ")
palindrome(str)