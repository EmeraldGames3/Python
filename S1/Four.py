def remove_duplicates(s: str):
    s = list(s)
    s = list(dict.fromkeys(s))
    return "".join(s)


print(remove_duplicates("aaaaaaeeeeeeeiiiiiiiiiiiouuu"))
