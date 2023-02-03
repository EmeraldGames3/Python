def validate(s: str):
    s = s.split("-")
    try:
        assert s[0][0].isalpha()
        assert s[0][1].isalpha()

        assert s[1][0].isnumeric()
        assert s[1][1].isnumeric()

        assert s[2][0].isalpha()
        assert s[2][1].isalpha()
        assert s[2][2].isalpha()

        return True
    except AssertionError:
        return False


print(validate("SB-18-BOG"))
