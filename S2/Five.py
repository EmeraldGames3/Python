import string


def caesar_encode(s: str, offset: int) -> str:
    encoded = ""
    for char in s:
        if char.isalpha():
            shifted = ord(char) + offset
            if char.islower():
                if shifted > ord("z"):
                    shifted -= 26
                encoded += chr(shifted)
            else:
                if shifted > ord("Z"):
                    shifted -= 26
                encoded += chr(shifted)
        else:
            encoded += char
    return encoded


def cool_caesar_encode(s: str, offset: int):
    # Create a mapping of the lowercase and uppercase letters to their shifted counterparts
    lower_map = {l: chr((ord(l) - ord('a') + offset) % 26 + ord('a')) for l in string.ascii_lowercase}
    upper_map = {l: chr((ord(l) - ord('A') + offset) % 26 + ord('A')) for l in string.ascii_uppercase}

    # Use the mapping to encode the string by applying the shift to each character
    encoded_str = "".join(map(lambda c: lower_map.get(c, upper_map.get(c, c)), s))
    return encoded_str


print(caesar_encode("Ana are mer", 5))
