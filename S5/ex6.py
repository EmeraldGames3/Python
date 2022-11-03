import ex5


def call_findPalindrom():
    with(open("ex6_in.txt") as f):
        data = ex5.findPalindrom(f)

    f = open("ex6_out.txt",'w')

    for el in data:
        f.write((el+" ") * data[el] + "\n")

    f.close()
