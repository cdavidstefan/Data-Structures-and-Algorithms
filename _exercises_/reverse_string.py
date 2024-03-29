# Create a function that reverses a string:
# "Ana are mere!" -> "!erem era anA"

def reverse_string_1(string):
    """
    Info: This function reverses a string.
    Info2: This is a very useful feature.
    """

    if not string or len(string) < 2 or type(string) is not str:
        print("Something's not right!")
    list_elements = list(string)
    new_list = []
    for i in range(len(list_elements)):
        new_list.insert(0, string[i])
    new_string = "".join(str(element) for element in new_list)
    return new_string


def reverse_string_2(string):
    if not string or len(string) < 2 or type(string) is not str:
        print("Specified input cannot be reversed by this function!")
    chars = list(string)
    chars.reverse()
    reverse_string = ''.join(chars)
    return reverse_string


def reverse_pythonic_way(string):
    if not string or len(string) < 2 or type(string) is not str:
        print("Specified input cannot be reversed by this function!")
    return string[::-1]


def reverse_join(string):
    if not string or len(string) < 2 or type(string) is not str:
        print("Specified input cannot be reversed by this function!")
    return ''.join(reversed(string))


stringus = "Astăzi este 8 martie!"
print(list(stringus))
print(reverse_string_1(stringus))
print(reverse_string_2(stringus))
print(reverse_pythonic_way(stringus))
print(reverse_join(stringus))
# help(reverse_string_1)
print(reverse_string_1.__doc__)
