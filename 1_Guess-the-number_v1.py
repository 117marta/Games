from random import randint


def get_number():
    """
    Get the number from user.
    Try until user gives proper number.

    :rtype: int
    :return: given number as int
    """
    while True:  # Infinite loop (True is always True)
        try:
            result = int(input("Guess the number (1 - 10): "))
            break
        except ValueError:
            print("It's not a number! Try again!\n")
    return result


def main_function():
    """
    Main function of the game.
    Guess the number drawn by the computer (1 - 10).
    """
    computer = randint(1, 10)
    guess = get_number()
    while guess != computer:
        if guess < computer:
            print("Too small!\n")
        else:
            print("Too big!\n")
        guess = get_number()  # Inaczej pętla będzie się cały czas wykonywać
    print("You Win!")


if __name__ == '__main__':
    main_function()
