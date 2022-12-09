def switch_info(arg):
    switcher = {
        0: "ZERO",
        1: "ONE",
        2: "TWO",
        3: "THREE",
        4: "FOUR",
        5: "FIVE",
        6: "SIX",
        7: "SIVEN",
        8: "EIGHT",
        9: "NINE"
    }
    return switcher.get(arg,"Not a single digit")

arg = int(input("Enter the digit."))
print(switch_info(arg))