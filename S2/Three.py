def is_palindrome(s: str):
    return s == s[::-1]


def is_palindrome_no_slicing(s: str):
    for i in range(len(s) // 2):
        if s[i] != s[-i - 1]:
            return False

    return True


def is_palindrome_recursive(s: str):
    if len(s) < 2:
        return True

    if s[0] != s[-1]:
        return False

    return is_palindrome(s[1:len(s) - 1])

