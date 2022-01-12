import random, re


POSSIBLE_DICES = ['3', '4', '6', '8', '10', '12', '20', '100']
DICE_PATTERN = re.compile(r"^(\d*)D(\d+)([+-]\d+)?$")


def roll_the_dice(character_string):
    """
    Calculate dice roll from dice pattern.
    xDy + z
    x - number of dice rolls (if you throw once - its negligible)
    y - type of dice to use (e.g. D6)
    z - number to add/subtract to the result of dice rolls

    :param str character_string: e.g. '2D6+5'
    :rtype: int, str
    :return: dice roll value for proper dice patter or 'Wrong input'
    """
    match = DICE_PATTERN.search(character_string)
    if not match:
        return 'Wrong input'

    multiply, dice, modifier = match.groups()
    if dice not in POSSIBLE_DICES:
        return 'Wrong input'

    multiply = int(multiply) if multiply else 1
    modifier = int(modifier) if modifier else 0
    dice = int(dice)

    result = sum([random.randint(1, dice) for _ in range(multiply)]) + modifier  # obliczona wartość
    return f'\nResult: {result}'


if __name__ == '__main__':
    print('You can input e.g.: 2D6+5, 2D10+10, D6, 2D3, D12-1.')
    print(roll_the_dice(input('Your input: ')))
