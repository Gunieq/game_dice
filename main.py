import random

valid_dices = {
    "D3",
    "D4",
    "D6",
    "D8",
    "D10",
    "D12",
    "D20",
    "D100",
}


def cast_dice():
    dice_formula = str(input("Enter the formula: "))
    for dice in valid_dices:
        if dice in dice_formula:
            try:
                multiply, modifier = dice_formula.split(dice)
            except ValueError:
                return "Wrong input"
            dice_value = int(dice[1:])
            break
    else:
        return "Wrong input"
    try:
        multiply = int(multiply) if multiply else 1
    except ValueError:
        return "Wrong Input"
    try:
        modifier = int(modifier) if modifier else 0
    except ValueError:
        return "Wrong Input"
    return sum([random.randint(1, dice_value) for i in range(multiply)]) + modifier


if __name__ == '__main__':
    print(cast_dice())
