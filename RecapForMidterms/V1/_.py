def element_occurrence(s: str, l: str) -> int:
    return s.count(l)


assert element_occurrence("abac", "a") == 2
assert element_occurrence("abac", "a") != 1

vowels = ('a', 'e', 'i', 'o', 'u')


def replace_vowels(s: str) -> str:
    for v in vowels:
        s = s.replace(v, '?')

    return s


assert replace_vowels("Ana are mere") == "An? ?r? m?r?"


def sum_numbers(l: list):
    l = filter(lambda x: type(x) == int, l)
    return sum(l)


assert sum_numbers(['a', 12, [1], 23, 'b']) == 35
