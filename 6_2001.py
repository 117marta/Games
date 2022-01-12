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
    i = 'D6'
    try:
        multiply, modifier = character_string.split(i)
    except ValueError:
        return "Wrong input"
    dice_value = int(i[1:])

    try:
        multiply = int(multiply) if multiply else 1
    except ValueError:
        return "Wrong input"

    try:
        modifier = int(modifier) if modifier else 0
    except ValueError:
        return 'Wrong input!'

    return sum([random.randint(1, dice_value) for _ in range(multiply)]) + modifier


def calculate_points(points):
    """
    Calculate points.

    :param int points:
    :rtype: int
    :return: new result of points
    """
    roll = roll_the_dice('2D6')
    if roll == 7:
        points //= 7
    elif roll == 11:
        points *= 11
    else:
        points += roll
    return points


def game_2001():
    """
    Main function of the game.
    """
    user_points = 0
    computer_points = 0

    # The first roll is unique
    input('Press ENTER to roll the dice.')
    user_points += roll_the_dice('2D6')
    computer_points += roll_the_dice('2D6')

    while user_points < 2001 and computer_points < 2001:
        print(f'User points: {user_points}\nComputer points: {computer_points}')
        input('Press ENTER to roll the dice.\n')
        user_points = calculate_points(user_points)
        computer_points = calculate_points(computer_points)

    print(f'User points: {user_points}\nComputer points: {computer_points}')
    if computer_points > user_points:
        print('Computer won!')
    elif user_points > computer_points:
        print('User won!')
    else:
        print('Draw')


if __name__ == '__main__':
    game_2001()
