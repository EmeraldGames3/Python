from exercises import One, Two, Three, Four, Five, Six, Seven, Eight, Nine, Ten, Eleven, Twelve, Thirteen

while True:
    option = input("Enter a number: ").strip()

    d = {'1': One.run, '2': Two.run, '3': Three.run,
         '4': Four.run, '5': Five.run, '6': Six.run,
         '7': Seven.run, '8': Eight.run, '9': Nine.run,
         '10': Ten.run, '11': Eleven.run, '12': Twelve.run,
         '13': Thirteen.run
         }

    if option in d:
        d[option]()
    elif option == '-1':
        break
    else:
        print("Invalid option")
