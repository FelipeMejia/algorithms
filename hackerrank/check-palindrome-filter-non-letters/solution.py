#!/bin/python3
#
# Complete the 'isAlphabeticPalindrome' function below.
#
# The function is expected to return a BOOLEAN.
# The function accepts STRING code as parameter.
#


def isAlphabeticPalindrome(code):
    letters = [char.lower() for char in code if char.isalpha()]

    if not len(letters):
        return True

    if len(letters) == 1:
        return True

    i, j = 0, len(letters) - 1
    while j > i:
        if letters[i] != letters[j]:
            return False

        i += 1
        j -= 1

    return True


if __name__ == "__main__":
    code = input()

    result = isAlphabeticPalindrome(code)

    print(int(result))
