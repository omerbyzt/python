def find_first(string):
    index = 0
    for char in string:
        if char != " ":
            break
        index += 1
    return index


def find_last(string):
    index = len(string) - 1
    count = 0
    for char in reversed(string):
        if char != " ":
            break
        index -= 1
        count += 1
    return index, count


def final_string(string, first, last, count):
    final_string = ""

    for i in range(first):
        final_string += " "

    for i in range(first, last + 1):
        if string[i] != " ":
            final_string += string[i]

    for i in range(count):
        final_string += " "

    return final_string


def main():
    string = "  om e  r  "
    first = find_first(string)
    last, count = find_last(string)

    print(final_string(string, first, last, count))


main()
