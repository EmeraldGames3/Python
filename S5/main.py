import ex1
import ex2
import ex3
import ex4
import ex5
import ex6


ex = {
    "1": ex1.callPerfectMatrix,
    "2": ex2.call_2,
    "3": ex3.call_isMatrixRow,
    "4": ex4.callReturnLongestWord,
    "5": ex5.call_findPalindrom,
    "6": ex6.call_findPalindrom
}


def test():
    ex1.test_isPerfect()
    ex2.test_2()
    ex3.test()
    ex4.test()
    ex5.test()


def run():
    while True:
        option = input("Enter Exercise ").strip()

        if option in ex:
            ex[option]()
        else:
            break


test()
run()
