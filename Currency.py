# CURRENCY – Currency Denomination Breakdown

amount = int(input("Enter the total amount: "))
denom = int(input("Enter the denomination to break down (100, 50, 20, 10, 5, 2, 1): "))

match denom:
    case 100:
        notes = amount // 100
        print("100 Rs notes:", notes)

    case 50:
        notes = amount // 50
        print("50 Rs notes:", notes)

    case 20:
        notes = amount // 20
        print("20 Rs notes:", notes)

    case 10:
        notes = amount // 10
        print("10 Rs notes:", notes)

    case 5:
        notes = amount // 5
        print("5 Rs notes:", notes)

    case 2:
        notes = amount // 2
        print("2 Rs notes:", notes)

    case 1:
        notes = amount // 1
        print("1 Rs notes:", notes)

    case _:
        print("Invalid denomination!")
