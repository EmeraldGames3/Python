def bigStringSum(s1, s2):
    s = ""
    carry = 0
    for i in range(len(s1)):
        s += str((int(s1[i]) + int(s2[i]) + carry) % 10)

        if int(s1[i]) + int(s2[i]) + carry > 9:
            carry = 1
        else:
            carry = 0

    if carry == 1:
        if int(s[0]) < 9:
            s = str(int(s[0]) + carry) + s[0:]
        else:
            s = "1" + s

    return s
