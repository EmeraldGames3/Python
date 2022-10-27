def bigStringSum(s1, s2):
    s = ""
    carry = 0
    for i in range(len(s1) - 1, -1, -1):
        s = str((int(s1[i]) + int(s2[i]) + carry) % 10) + s

        if int(s1[i]) + int(s2[i]) + carry > 9:
            carry = 1
        else:
            carry = 0

        print(s)

    if carry == 1:
        s = "1" + s

    return s
