import _1
import _2
import _3
import _4
import _5
import _6
import _7

lst = [12, 14, 16, 18, 12, 13, 25, 25, 25, 48, 69, 42, 21, 61, 98, 87, 76, 12, 36]
print(lst)
key = lst[0]

exercises = {
    "1": _1.removeDuplicates_1,
    "2": _2.countSymmetricNumbers_2,
    "3": _3.generateBigNumber_3,
    "4": _4.encryptElements_4,
    "5": _5.filterNumbers_5,
    "6": _6.findDominoSequence,
    "7": _7.kgV_7,
}

while True:
    option = input("Enter the exercise number: ").strip()

    if option in exercises:
        exercises[option](lst)
    else:
        break

# # 1
# lst = _1.removeDuplicates_1(lst)
# # 2
# _2.countSymmetricNumbers_2(lst)
# # 3
# _3.generateBigNumber_3(lst)
# # 4
# _4.encryptElements_4(lst)
# _4.decryptElements_4(lst)
# # 5
# _5.filterNumbers_5(lst)
# # 6
# _6.findDominoSequence([12, 32, 64, 89, 11])
# # 7
# _7.kgV_7(len(lst) - 1)
