from exercises import exercise_2, exercise_1, exercise_3, exercise_4, exercise_5

lst = [1, 2, 3, 4, 5, 6]


def run():
    option = input("Exercise: ").strip()

    if option == "1":
        number = int(input("Enter a number ").strip())
        exercise_1.isSumOfTwoElements(lst, number)
    elif option == "2":
        number1 = input("Enter the first number ").strip()
        number2 = input("Enter the second number ").strip()
        print(exercise_2.bigStringSum(number1, number2))
    elif option == "3":
        s = input("Enter a word ").strip()
        print(exercise_3.reverse(s))
    elif option == "4":
        word = input("Enter a word ").strip()
        print(exercise_4.wordExists(word))
    elif option == "5":
        number1 = input("Enter the first number ").strip()
        number2 = input("Enter the second number ").strip()
        print(exercise_5.biggerStringSum(number1, number2))


run()
