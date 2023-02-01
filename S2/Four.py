def find_substring(target: str, source: str):
    if source not in target:
        return -1

    for i in range(len(target)):
        if target[i:i+len(source)] == source:
            return i


print(find_substring("testing", "ing"))
