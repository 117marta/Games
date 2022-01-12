import random


POSSIBLE_DICES = ['D3', 'D4', 'D6', 'D8', 'D10', 'D12', 'D20', 'D100']


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
    for i in POSSIBLE_DICES:
        if i in character_string:  # jeżeli dozwolone_kostki są w którejś z kostek użytkownika
            try:
                multiply, modifier = character_string.split(i)  # rozdzielamy POSSIBLE_DICES uzyskując: multiply i modifier
            except ValueError:  # gdy POSSIBLE_DICES jest więcej niż jeden raz (split podzieli na > 2 części)
                return "Wrong input"
            dice_value = int(i[1:])  # wyciągamy drugą wartość z (POSSIBLE_DICES) - liczba po 'D'
            break
    else:  # żadna z kostek nie pasuje do danych wejściowych
        return "Neither of the dices match the input"

    # multiply i modifier są opcjonalne - mogą być pustymi stringami (trzeba je zrzutować na typ int).
    try:  # pusty string -> 1
        multiply = int(multiply) if multiply else 1
    except ValueError:
        return "Wrong input"

    try:  # pusty string -> 0
        modifier = int(modifier) if modifier else 0
    except ValueError:
        return 'Wrong input!'

    result = sum([random.randint(1, dice_value) for _ in range(multiply)]) + modifier  # obliczona wartość
    return f'\nResult: {result}'


if __name__ == '__main__':
    print('You can input e.g.: 2D6+5, 2D10+10, D6, 2D3, D12-1.')
    print(roll_the_dice(input('Your input: ')))
